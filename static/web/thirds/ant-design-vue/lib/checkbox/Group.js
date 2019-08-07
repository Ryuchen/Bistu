'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _toConsumableArray2 = require('babel-runtime/helpers/toConsumableArray');

var _toConsumableArray3 = _interopRequireDefault(_toConsumableArray2);

var _extends2 = require('babel-runtime/helpers/extends');

var _extends3 = _interopRequireDefault(_extends2);

var _Checkbox = require('./Checkbox');

var _Checkbox2 = _interopRequireDefault(_Checkbox);

var _propsUtil = require('../_util/props-util');

var _propsUtil2 = _interopRequireDefault(_propsUtil);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

function noop() {}
exports['default'] = {
  name: 'ACheckboxGroup',
  model: {
    prop: 'value'
  },
  props: {
    prefixCls: {
      'default': 'ant-checkbox',
      type: String
    },
    defaultValue: {
      'default': undefined,
      type: Array
    },
    value: {
      'default': undefined,
      type: Array
    },
    options: {
      'default': function _default() {
        return [];
      },
      type: Array
    },
    disabled: Boolean
  },
  provide: function provide() {
    return {
      checkboxGroupContext: this
    };
  },
  data: function data() {
    var value = this.value,
        defaultValue = this.defaultValue;

    return {
      sValue: value || defaultValue || []
    };
  },

  watch: {
    value: function value(val) {
      this.sValue = val;
    }
  },
  methods: {
    getOptions: function getOptions() {
      var options = this.options,
          $scopedSlots = this.$scopedSlots;

      return options.map(function (option) {
        if (typeof option === 'string') {
          return {
            label: option,
            value: option
          };
        }
        var label = option.label;
        if (label === undefined && $scopedSlots.label) {
          label = $scopedSlots.label(option);
        }
        return (0, _extends3['default'])({}, option, { label: label });
      });
    },
    toggleOption: function toggleOption(option) {
      var optionIndex = this.sValue.indexOf(option.value);
      var value = [].concat((0, _toConsumableArray3['default'])(this.sValue));
      if (optionIndex === -1) {
        value.push(option.value);
      } else {
        value.splice(optionIndex, 1);
      }
      if (!(0, _propsUtil2['default'])(this, 'value')) {
        this.sValue = value;
      }
      this.$emit('input', value);
      this.$emit('change', value);
    }
  },
  render: function render() {
    var h = arguments[0];
    var props = this.$props,
        state = this.$data,
        $slots = this.$slots;
    var prefixCls = props.prefixCls,
        options = props.options;

    var children = $slots['default'];
    var groupPrefixCls = prefixCls + '-group';
    if (options && options.length > 0) {
      children = this.getOptions().map(function (option) {
        return h(
          _Checkbox2['default'],
          {
            attrs: {
              prefixCls: prefixCls,

              disabled: 'disabled' in option ? option.disabled : props.disabled,
              value: option.value,
              checked: state.sValue.indexOf(option.value) !== -1
            },
            key: option.value.toString(), on: {
              'change': option.onChange || noop
            },

            'class': groupPrefixCls + '-item'
          },
          [option.label]
        );
      });
    }
    return h(
      'div',
      { 'class': groupPrefixCls },
      [children]
    );
  }
};