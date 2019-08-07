'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _Card = require('./Card');

var _Card2 = _interopRequireDefault(_Card);

var _Meta = require('./Meta');

var _Meta2 = _interopRequireDefault(_Meta);

var _Grid = require('./Grid');

var _Grid2 = _interopRequireDefault(_Grid);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

_Card2['default'].Meta = _Meta2['default'];
_Card2['default'].Grid = _Grid2['default'];

/* istanbul ignore next */
_Card2['default'].install = function (Vue) {
  Vue.component(_Card2['default'].name, _Card2['default']);
  Vue.component(_Meta2['default'].name, _Meta2['default']);
  Vue.component(_Grid2['default'].name, _Grid2['default']);
};

exports['default'] = _Card2['default'];