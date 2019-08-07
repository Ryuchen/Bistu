'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _vueTypes = require('../../_util/vue-types');

var _vueTypes2 = _interopRequireDefault(_vueTypes);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

exports['default'] = {
  wrapperClassName: _vueTypes2['default'].string,
  width: _vueTypes2['default'].any,
  height: _vueTypes2['default'].any,
  defaultOpen: _vueTypes2['default'].bool,
  firstEnter: _vueTypes2['default'].bool,
  open: _vueTypes2['default'].bool,
  prefixCls: _vueTypes2['default'].string,
  placement: _vueTypes2['default'].string,
  level: _vueTypes2['default'].oneOfType([_vueTypes2['default'].string, _vueTypes2['default'].array]),
  levelMove: _vueTypes2['default'].oneOfType([_vueTypes2['default'].number, _vueTypes2['default'].func, _vueTypes2['default'].array]),
  ease: _vueTypes2['default'].string,
  duration: _vueTypes2['default'].string,
  getContainer: _vueTypes2['default'].oneOfType([_vueTypes2['default'].string, _vueTypes2['default'].func, _vueTypes2['default'].object, _vueTypes2['default'].bool]),
  handler: _vueTypes2['default'].any,
  showMask: _vueTypes2['default'].bool,
  maskStyle: _vueTypes2['default'].object,
  className: _vueTypes2['default'].string,
  wrapStyle: _vueTypes2['default'].object
};