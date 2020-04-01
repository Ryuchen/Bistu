'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _PropTypes = require('./PropTypes');

exports['default'] = {
  name: 'StoreProvider',
  props: {
    store: _PropTypes.storeShape.isRequired
  },
  provide: function provide() {
    return {
      storeContext: this.$props
    };
  },
  render: function render() {
    return this.$slots['default'][0];
  }
};