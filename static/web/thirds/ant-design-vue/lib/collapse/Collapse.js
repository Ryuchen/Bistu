'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _extends2 = require('babel-runtime/helpers/extends');

var _extends3 = _interopRequireDefault(_extends2);

var _defineProperty2 = require('babel-runtime/helpers/defineProperty');

var _defineProperty3 = _interopRequireDefault(_defineProperty2);

var _openAnimation = require('../_util/openAnimation');

var _openAnimation2 = _interopRequireDefault(_openAnimation);

var _propsUtil = require('../_util/props-util');

var _vcCollapse = require('../vc-collapse');

var _vcCollapse2 = _interopRequireDefault(_vcCollapse);

var _icon = require('../icon');

var _icon2 = _interopRequireDefault(_icon);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

exports['default'] = {
  name: 'ACollapse',
  model: {
    prop: 'activeKey',
    event: 'change'
  },
  props: (0, _propsUtil.initDefaultProps)(_vcCollapse.collapseProps, {
    prefixCls: 'ant-collapse',
    bordered: true,
    openAnimation: _openAnimation2['default']
  }),
  methods: {
    renderExpandIcon: function renderExpandIcon() {
      var h = this.$createElement;

      return h(_icon2['default'], {
        attrs: { type: 'right' },
        'class': 'arrow' });
    }
  },
  render: function render() {
    var h = arguments[0];
    var prefixCls = this.prefixCls,
        bordered = this.bordered,
        $listeners = this.$listeners;

    var collapseClassName = (0, _defineProperty3['default'])({}, prefixCls + '-borderless', !bordered);
    var rcCollapeProps = {
      props: (0, _extends3['default'])({}, (0, _propsUtil.getOptionProps)(this), {
        expandIcon: this.renderExpandIcon
      }),
      'class': collapseClassName,
      on: $listeners
    };
    return h(
      _vcCollapse2['default'],
      rcCollapeProps,
      [this.$slots['default']]
    );
  }
};