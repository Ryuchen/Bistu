'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.DropdownButtonProps = undefined;

var _babelHelperVueJsxMergeProps = require('babel-helper-vue-jsx-merge-props');

var _babelHelperVueJsxMergeProps2 = _interopRequireDefault(_babelHelperVueJsxMergeProps);

var _objectWithoutProperties2 = require('babel-runtime/helpers/objectWithoutProperties');

var _objectWithoutProperties3 = _interopRequireDefault(_objectWithoutProperties2);

var _extends2 = require('babel-runtime/helpers/extends');

var _extends3 = _interopRequireDefault(_extends2);

var _button = require('../button');

var _button2 = _interopRequireDefault(_button);

var _buttonTypes = require('../button/buttonTypes');

var _buttonTypes2 = _interopRequireDefault(_buttonTypes);

var _buttonGroup = require('../button/button-group');

var _dropdown = require('./dropdown');

var _dropdown2 = _interopRequireDefault(_dropdown);

var _vueTypes = require('../_util/vue-types');

var _vueTypes2 = _interopRequireDefault(_vueTypes);

var _propsUtil = require('../_util/props-util');

var _getDropdownProps = require('./getDropdownProps');

var _getDropdownProps2 = _interopRequireDefault(_getDropdownProps);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

var ButtonTypesProps = (0, _buttonTypes2['default'])();
var DropdownProps = (0, _getDropdownProps2['default'])();
var ButtonGroup = _button2['default'].Group;
var DropdownButtonProps = (0, _extends3['default'])({}, _buttonGroup.ButtonGroupProps, DropdownProps, {
  type: _vueTypes2['default'].oneOf(['primary', 'ghost', 'dashed', 'danger', 'default']).def('default'),
  htmlType: ButtonTypesProps.htmlType,
  disabled: _vueTypes2['default'].bool,
  prefixCls: _vueTypes2['default'].string.def('ant-dropdown-button'),
  placement: DropdownProps.placement.def('bottomRight')
});
exports.DropdownButtonProps = DropdownButtonProps;
exports['default'] = {
  name: 'ADropdownButton',
  model: {
    prop: 'visible',
    event: 'visibleChange'
  },
  props: DropdownButtonProps,
  provide: function provide() {
    return {
      savePopupRef: this.savePopupRef
    };
  },

  inject: {
    configProvider: { 'default': function _default() {
        return {};
      } }
  },
  methods: {
    savePopupRef: function savePopupRef(ref) {
      this.popupRef = ref;
    },
    onClick: function onClick(e) {
      this.$emit('click', e);
    },
    onVisibleChange: function onVisibleChange(val) {
      this.$emit('visibleChange', val);
    }
  },
  render: function render() {
    var h = arguments[0];
    var _$props = this.$props,
        type = _$props.type,
        disabled = _$props.disabled,
        htmlType = _$props.htmlType,
        prefixCls = _$props.prefixCls,
        trigger = _$props.trigger,
        align = _$props.align,
        visible = _$props.visible,
        placement = _$props.placement,
        getPopupContainer = _$props.getPopupContainer,
        restProps = (0, _objectWithoutProperties3['default'])(_$props, ['type', 'disabled', 'htmlType', 'prefixCls', 'trigger', 'align', 'visible', 'placement', 'getPopupContainer']);
    var getContextPopupContainer = this.configProvider.getPopupContainer;

    var dropdownProps = {
      props: {
        align: align,
        disabled: disabled,
        trigger: disabled ? [] : trigger,
        placement: placement,
        getPopupContainer: getPopupContainer || getContextPopupContainer
      },
      on: {
        visibleChange: this.onVisibleChange
      }
    };
    if ((0, _propsUtil.hasProp)(this, 'visible')) {
      dropdownProps.props.visible = visible;
    }

    return h(
      ButtonGroup,
      (0, _babelHelperVueJsxMergeProps2['default'])([restProps, { 'class': prefixCls }]),
      [h(
        _button2['default'],
        {
          attrs: { type: type, disabled: disabled, htmlType: htmlType },
          on: {
            'click': this.onClick
          }
        },
        [this.$slots['default']]
      ), h(
        _dropdown2['default'],
        dropdownProps,
        [h(
          'template',
          { slot: 'overlay' },
          [(0, _propsUtil.getComponentFromProp)(this, 'overlay')]
        ), h(_button2['default'], {
          attrs: { type: type, disabled: disabled, icon: 'ellipsis' }
        })]
      )]
    );
  }
};