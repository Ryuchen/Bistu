'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _extends2 = require('babel-runtime/helpers/extends');

var _extends3 = _interopRequireDefault(_extends2);

var _Radio = require('./Radio');

var _Radio2 = _interopRequireDefault(_Radio);

var _propsUtil = require('../_util/props-util');

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

exports['default'] = {
  name: 'ARadioButton',
  props: (0, _extends3['default'])({}, _Radio2['default'].props, {
    prefixCls: {
      'default': 'ant-radio-button',
      type: String
    }
  }),
  inject: {
    radioGroupContext: { 'default': undefined }
  },
  render: function render() {
    var h = arguments[0];

    var props = (0, _propsUtil.getOptionProps)(this);
    var radioProps = { props: props, on: (0, _extends3['default'])({}, this.$listeners) };
    if (this.radioGroupContext) {
      radioProps.on.change = this.radioGroupContext.onRadioChange;
      radioProps.props.checked = props.value === this.radioGroupContext.stateValue;
      radioProps.props.disabled = props.disabled || this.radioGroupContext.disabled;
    }
    return h(
      _Radio2['default'],
      radioProps,
      [this.$slots['default']]
    );
  }
};