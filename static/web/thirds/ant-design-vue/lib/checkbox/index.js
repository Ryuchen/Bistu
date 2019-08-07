'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _Checkbox = require('./Checkbox');

var _Checkbox2 = _interopRequireDefault(_Checkbox);

var _Group = require('./Group');

var _Group2 = _interopRequireDefault(_Group);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

_Checkbox2['default'].Group = _Group2['default'];

/* istanbul ignore next */
_Checkbox2['default'].install = function (Vue) {
  Vue.component(_Checkbox2['default'].name, _Checkbox2['default']);
  Vue.component(_Group2['default'].name, _Group2['default']);
};

exports['default'] = _Checkbox2['default'];