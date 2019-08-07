'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _Avatar = require('./Avatar');

var _Avatar2 = _interopRequireDefault(_Avatar);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

/* istanbul ignore next */
_Avatar2['default'].install = function (Vue) {
  Vue.component(_Avatar2['default'].name, _Avatar2['default']);
};

exports['default'] = _Avatar2['default'];