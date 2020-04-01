'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _objectWithoutProperties2 = require('babel-runtime/helpers/objectWithoutProperties');

var _objectWithoutProperties3 = _interopRequireDefault(_objectWithoutProperties2);

var _defineProperty2 = require('babel-runtime/helpers/defineProperty');

var _defineProperty3 = _interopRequireDefault(_defineProperty2);

var _extends2 = require('babel-runtime/helpers/extends');

var _extends3 = _interopRequireDefault(_extends2);

var _classnames = require('classnames');

var _classnames2 = _interopRequireDefault(_classnames);

var _propsUtil = require('../_util/props-util');

var _Input = require('./Input');

var _Input2 = _interopRequireDefault(_Input);

var _icon = require('../icon');

var _icon2 = _interopRequireDefault(_icon);

var _inputProps = require('./inputProps');

var _inputProps2 = _interopRequireDefault(_inputProps);

var _vueTypes = require('../_util/vue-types');

var _vueTypes2 = _interopRequireDefault(_vueTypes);

var _BaseMixin = require('../_util/BaseMixin');

var _BaseMixin2 = _interopRequireDefault(_BaseMixin);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

var ActionMap = {
  click: 'click',
  hover: 'mouseover'
};

exports['default'] = {
  name: 'AInputPassword',
  mixins: [_BaseMixin2['default']],
  inheritAttrs: false,
  model: {
    prop: 'value',
    event: 'change.value'
  },
  props: (0, _extends3['default'])({}, _inputProps2['default'], {
    prefixCls: _vueTypes2['default'].string.def('ant-input-password'),
    inputPrefixCls: _vueTypes2['default'].string.def('ant-input'),
    action: _vueTypes2['default'].string.def('click'),
    visibilityToggle: _vueTypes2['default'].bool.def(true)
  }),
  data: function data() {
    return {
      visible: false
    };
  },

  methods: {
    focus: function focus() {
      this.$refs.input.focus();
    },
    blur: function blur() {
      this.$refs.input.blur();
    },
    onVisibleChange: function onVisibleChange() {
      if (this.disabled) {
        return;
      }
      this.setState({
        visible: !this.visible
      });
    },
    getIcon: function getIcon() {
      var _on;

      var h = this.$createElement;
      var _$props = this.$props,
          prefixCls = _$props.prefixCls,
          action = _$props.action;

      var iconTrigger = ActionMap[action] || '';
      var iconProps = {
        props: {
          type: this.visible ? 'eye' : 'eye-invisible'
        },
        on: (_on = {}, (0, _defineProperty3['default'])(_on, iconTrigger, this.onVisibleChange), (0, _defineProperty3['default'])(_on, 'mousedown', function mousedown(e) {
          // Prevent focused state lost
          // https://github.com/ant-design/ant-design/issues/15173
          e.preventDefault();
        }), _on),
        'class': prefixCls + '-icon',
        key: 'passwordIcon'
      };
      return h(_icon2['default'], iconProps);
    }
  },
  render: function render() {
    var h = arguments[0];

    var _getOptionProps = (0, _propsUtil.getOptionProps)(this),
        prefixCls = _getOptionProps.prefixCls,
        inputPrefixCls = _getOptionProps.inputPrefixCls,
        size = _getOptionProps.size,
        suffix = _getOptionProps.suffix,
        visibilityToggle = _getOptionProps.visibilityToggle,
        restProps = (0, _objectWithoutProperties3['default'])(_getOptionProps, ['prefixCls', 'inputPrefixCls', 'size', 'suffix', 'visibilityToggle']);

    var suffixIcon = visibilityToggle && this.getIcon();
    var inputClassName = (0, _classnames2['default'])(prefixCls, (0, _defineProperty3['default'])({}, prefixCls + '-' + size, !!size));
    var inputProps = {
      props: (0, _extends3['default'])({}, restProps, {
        prefixCls: inputPrefixCls,
        size: size,
        suffix: suffixIcon,
        prefix: (0, _propsUtil.getComponentFromProp)(this, 'prefix'),
        addonAfter: (0, _propsUtil.getComponentFromProp)(this, 'addonAfter'),
        addonBefore: (0, _propsUtil.getComponentFromProp)(this, 'addonBefore')
      }),
      attrs: (0, _extends3['default'])({}, this.$attrs, {
        type: this.visible ? 'text' : 'password'
      }),
      'class': inputClassName,
      ref: 'input',
      on: (0, _propsUtil.getListeners)(this)
    };
    return h(_Input2['default'], inputProps);
  }
};