'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _antInputDirective = require('./antInputDirective');

var _FormDecoratorDirective = require('./FormDecoratorDirective');

exports['default'] = {
  install: function install(Vue) {
    (0, _antInputDirective.antInput)(Vue);
    (0, _FormDecoratorDirective.antDecorator)(Vue);
  }
};