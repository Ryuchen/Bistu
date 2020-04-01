'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _extends2 = require('babel-runtime/helpers/extends');

var _extends3 = _interopRequireDefault(_extends2);

var _tooltip = require('../tooltip');

var _tooltip2 = _interopRequireDefault(_tooltip);

var _abstractTooltipProps = require('../tooltip/abstractTooltipProps');

var _abstractTooltipProps2 = _interopRequireDefault(_abstractTooltipProps);

var _vueTypes = require('../_util/vue-types');

var _vueTypes2 = _interopRequireDefault(_vueTypes);

var _propsUtil = require('../_util/props-util');

var _configProvider = require('../config-provider');

var _base = require('../base');

var _base2 = _interopRequireDefault(_base);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

var props = (0, _abstractTooltipProps2['default'])();
var Popover = {
  name: 'APopover',
  props: (0, _extends3['default'])({}, props, {
    prefixCls: _vueTypes2['default'].string,
    transitionName: _vueTypes2['default'].string.def('zoom-big'),
    content: _vueTypes2['default'].any,
    title: _vueTypes2['default'].any
  }),
  model: {
    prop: 'visible',
    event: 'visibleChange'
  },
  inject: {
    configProvider: { 'default': function _default() {
        return _configProvider.ConfigConsumerProps;
      } }
  },
  methods: {
    getPopupDomNode: function getPopupDomNode() {
      return this.$refs.tooltip.getPopupDomNode();
    }
  },

  render: function render() {
    var h = arguments[0];
    var title = this.title,
        customizePrefixCls = this.prefixCls,
        $slots = this.$slots;

    var getPrefixCls = this.configProvider.getPrefixCls;
    var prefixCls = getPrefixCls('popover', customizePrefixCls);

    var props = (0, _propsUtil.getOptionProps)(this);
    delete props.title;
    delete props.content;
    var tooltipProps = {
      props: (0, _extends3['default'])({}, props, {
        prefixCls: prefixCls
      }),
      ref: 'tooltip',
      on: (0, _propsUtil.getListeners)(this)
    };
    return h(
      _tooltip2['default'],
      tooltipProps,
      [h(
        'template',
        { slot: 'title' },
        [h('div', [(title || $slots.title) && h(
          'div',
          { 'class': prefixCls + '-title' },
          [(0, _propsUtil.getComponentFromProp)(this, 'title')]
        ), h(
          'div',
          { 'class': prefixCls + '-inner-content' },
          [(0, _propsUtil.getComponentFromProp)(this, 'content')]
        )])]
      ), this.$slots['default']]
    );
  }
};

/* istanbul ignore next */
Popover.install = function (Vue) {
  Vue.use(_base2['default']);
  Vue.component(Popover.name, Popover);
};

exports['default'] = Popover;