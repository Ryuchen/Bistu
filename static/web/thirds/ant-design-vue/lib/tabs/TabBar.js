'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _extends2 = require('babel-runtime/helpers/extends');

var _extends3 = _interopRequireDefault(_extends2);

var _defineProperty2 = require('babel-runtime/helpers/defineProperty');

var _defineProperty3 = _interopRequireDefault(_defineProperty2);

var _typeof2 = require('babel-runtime/helpers/typeof');

var _typeof3 = _interopRequireDefault(_typeof2);

var _icon = require('../icon');

var _icon2 = _interopRequireDefault(_icon);

var _ScrollableInkTabBar = require('../vc-tabs/src/ScrollableInkTabBar');

var _ScrollableInkTabBar2 = _interopRequireDefault(_ScrollableInkTabBar);

var _vnode = require('../_util/vnode');

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

var TabBar = {
  functional: true,
  render: function render(h, context) {
    var _cls;

    var _context$props = context.props,
        tabBarStyle = _context$props.tabBarStyle,
        _context$props$animat = _context$props.animated,
        animated = _context$props$animat === undefined ? true : _context$props$animat,
        renderTabBar = _context$props.renderTabBar,
        tabBarExtraContent = _context$props.tabBarExtraContent,
        tabPosition = _context$props.tabPosition,
        prefixCls = _context$props.prefixCls,
        _context$props$type = _context$props.type,
        type = _context$props$type === undefined ? 'line' : _context$props$type,
        size = _context$props.size;

    var inkBarAnimated = (typeof animated === 'undefined' ? 'undefined' : (0, _typeof3['default'])(animated)) === 'object' ? animated.inkBar : animated;

    var isVertical = tabPosition === 'left' || tabPosition === 'right';
    var prevIconType = isVertical ? 'up' : 'left';
    var nextIconType = isVertical ? 'down' : 'right';
    var prevIcon = h(
      'span',
      { 'class': prefixCls + '-tab-prev-icon' },
      [h(_icon2['default'], {
        attrs: { type: prevIconType },
        'class': prefixCls + '-tab-prev-icon-target' })]
    );
    var nextIcon = h(
      'span',
      { 'class': prefixCls + '-tab-next-icon' },
      [h(_icon2['default'], {
        attrs: { type: nextIconType },
        'class': prefixCls + '-tab-next-icon-target' })]
    );

    // Additional className for style usage
    var cls = (_cls = {}, (0, _defineProperty3['default'])(_cls, prefixCls + '-' + tabPosition + '-bar', true), (0, _defineProperty3['default'])(_cls, prefixCls + '-' + size + '-bar', !!size), (0, _defineProperty3['default'])(_cls, prefixCls + '-card-bar', type && type.indexOf('card') >= 0), _cls);

    var renderProps = {
      props: (0, _extends3['default'])({}, context.props, {
        inkBarAnimated: inkBarAnimated,
        extraContent: tabBarExtraContent,
        prevIcon: prevIcon,
        nextIcon: nextIcon
      }),
      style: tabBarStyle,
      on: context.listeners,
      'class': cls
    };

    var RenderTabBar = void 0;

    if (renderTabBar) {
      RenderTabBar = renderTabBar(renderProps, _ScrollableInkTabBar2['default']);
    } else {
      RenderTabBar = h(_ScrollableInkTabBar2['default'], renderProps);
    }

    return (0, _vnode.cloneElement)(RenderTabBar, renderProps);
  }
};

exports['default'] = TabBar;