'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _grid = require('../grid');

/* istanbul ignore next */
_grid.Row.install = function (Vue) {
  Vue.component(_grid.Row.name, _grid.Row);
};

exports['default'] = _grid.Row;