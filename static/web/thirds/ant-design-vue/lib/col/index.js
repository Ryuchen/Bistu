'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _grid = require('../grid');

/* istanbul ignore next */
_grid.Col.install = function (Vue) {
  Vue.component(_grid.Col.name, _grid.Col);
};

exports['default'] = _grid.Col;