'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _defineProperty2 = require('babel-runtime/helpers/defineProperty');

var _defineProperty3 = _interopRequireDefault(_defineProperty2);

var _extends2 = require('babel-runtime/helpers/extends');

var _extends3 = _interopRequireDefault(_extends2);

var _classnames = require('classnames');

var _classnames2 = _interopRequireDefault(_classnames);

var _vueTypes = require('../_util/vue-types');

var _vueTypes2 = _interopRequireDefault(_vueTypes);

var _Radio = require('./Radio');

var _Radio2 = _interopRequireDefault(_Radio);

var _propsUtil = require('../_util/props-util');

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

function noop() {}

exports['default'] = {
  name: 'ARadioGroup',
  model: {
    prop: 'value'
  },
  props: {
    prefixCls: {
      'default': 'ant-radio',
      type: String
    },
    defaultValue: _vueTypes2['default'].any,
    value: _vueTypes2['default'].any,
    size: {
      'default': 'default',
      validator: function validator(value) {
        return ['large', 'default', 'small'].includes(value);
      }
    },
    options: {
      'default': function _default() {
        return [];
      },
      type: Array
    },
    disabled: Boolean,
    name: String,
    buttonStyle: _vueTypes2['default'].string.def('outline')
  },
  data: function data() {
    var value = this.value,
        defaultValue = this.defaultValue;

    return {
      stateValue: value === undefined ? defaultValue : value
    };
  },
  provide: function provide() {
    return {
      radioGroupContext: this
    };
  },

  computed: {
    radioOptions: function radioOptions() {
      var disabled = this.disabled;

      return this.options.map(function (option) {
        return typeof option === 'string' ? { label: option, value: option } : (0, _extends3['default'])({}, option, { disabled: option.disabled === undefined ? disabled : option.disabled });
      });
    },
    classes: function classes() {
      var _ref;

      var prefixCls = this.prefixCls,
          size = this.size;

      return _ref = {}, (0, _defineProperty3['default'])(_ref, '' + prefixCls, true), (0, _defineProperty3['default'])(_ref, prefixCls + '-' + size, size), _ref;
    }
  },
  watch: {
    value: function value(val) {
      this.stateValue = val;
    }
  },
  methods: {
    onRadioChange: function onRadioChange(ev) {
      var lastValue = this.stateValue;
      var value = ev.target.value;

      if (!(0, _propsUtil.hasProp)(this, 'value')) {
        this.stateValue = value;
      }
      if (value !== lastValue) {
        this.$emit('input', value);
        this.$emit('change', ev);
      }
    }
  },
  render: function render() {
    var _this = this;

    var h = arguments[0];
    var _$listeners = this.$listeners,
        _$listeners$mouseente = _$listeners.mouseenter,
        mouseenter = _$listeners$mouseente === undefined ? noop : _$listeners$mouseente,
        _$listeners$mouseleav = _$listeners.mouseleave,
        mouseleave = _$listeners$mouseleav === undefined ? noop : _$listeners$mouseleav;

    var props = (0, _propsUtil.getOptionProps)(this);
    var prefixCls = props.prefixCls,
        options = props.options,
        buttonStyle = props.buttonStyle;

    var groupPrefixCls = prefixCls + '-group';
    var classString = (0, _classnames2['default'])(groupPrefixCls, groupPrefixCls + '-' + buttonStyle, (0, _defineProperty3['default'])({}, groupPrefixCls + '-' + props.size, props.size));

    var children = (0, _propsUtil.filterEmpty)(this.$slots['default']);

    // 如果存在 options, 优先使用
    if (options && options.length > 0) {
      children = options.map(function (option, index) {
        if (typeof option === 'string') {
          return h(
            _Radio2['default'],
            {
              key: index,
              attrs: { prefixCls: prefixCls,
                disabled: props.disabled,
                value: option,

                checked: _this.stateValue === option
              },
              on: {
                'change': _this.onRadioChange
              }
            },
            [option]
          );
        } else {
          return h(
            _Radio2['default'],
            {
              key: index,
              attrs: { prefixCls: prefixCls,
                disabled: option.disabled || props.disabled,
                value: option.value,

                checked: _this.stateValue === option.value
              },
              on: {
                'change': _this.onRadioChange
              }
            },
            [option.label]
          );
        }
      });
    }

    return h(
      'div',
      { 'class': classString, on: {
          'mouseenter': mouseenter,
          'mouseleave': mouseleave
        }
      },
      [children]
    );
  }
};