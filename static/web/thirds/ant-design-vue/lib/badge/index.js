'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _Badge = require('./Badge');

var _Badge2 = _interopRequireDefault(_Badge);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

/* istanbul ignore next */
_Badge2['default'].install = function (Vue) {
  Vue.component(_Badge2['default'].name, _Badge2['default']);
};

exports['default'] = _Badge2['default'];