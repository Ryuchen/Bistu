'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports['default'] = wrapperRaf;

var _raf = require('raf');

var _raf2 = _interopRequireDefault(_raf);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

var id = 0;
var ids = {};

// Support call raf with delay specified frame
function wrapperRaf(callback) {
  var delayFrames = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : 1;

  var myId = id++;
  var restFrames = delayFrames;

  function internalCallback() {
    restFrames -= 1;

    if (restFrames <= 0) {
      callback();
      delete ids[id];
    } else {
      ids[id] = (0, _raf2['default'])(internalCallback);
    }
  }

  ids[id] = (0, _raf2['default'])(internalCallback);

  return myId;
}

wrapperRaf.cancel = function (id) {
  _raf2['default'].cancel(ids[id]);
  delete ids[id];
};