'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _Breadcrumb = require('./Breadcrumb');

var _Breadcrumb2 = _interopRequireDefault(_Breadcrumb);

var _BreadcrumbItem = require('./BreadcrumbItem');

var _BreadcrumbItem2 = _interopRequireDefault(_BreadcrumbItem);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

_Breadcrumb2['default'].Item = _BreadcrumbItem2['default'];

/* istanbul ignore next */
_Breadcrumb2['default'].install = function (Vue) {
  Vue.component(_Breadcrumb2['default'].name, _Breadcrumb2['default']);
  Vue.component(_BreadcrumbItem2['default'].name, _BreadcrumbItem2['default']);
};

exports['default'] = _Breadcrumb2['default'];