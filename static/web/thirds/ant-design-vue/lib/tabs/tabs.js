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

var _src = require('../vc-tabs/src');

var _src2 = _interopRequireDefault(_src);

var _TabContent = require('../vc-tabs/src/TabContent');

var _TabContent2 = _interopRequireDefault(_TabContent);

var _isFlexSupported = require('../_util/isFlexSupported');

var _isFlexSupported2 = _interopRequireDefault(_isFlexSupported);

var _vueTypes = require('../_util/vue-types');

var _vueTypes2 = _interopRequireDefault(_vueTypes);

var _propsUtil = require('../_util/props-util');

var _vnode = require('../_util/vnode');

var _TabBar = require('./TabBar');

var _TabBar2 = _interopRequireDefault(_TabBar);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

exports['default'] = {
  TabPane: _src.TabPane,
  name: 'ATabs',
  model: {
    prop: 'activeKey',
    event: 'change'
  },
  props: {
    prefixCls: _vueTypes2['default'].string.def('ant-tabs'),
    activeKey: _vueTypes2['default'].oneOfType([_vueTypes2['default'].string, _vueTypes2['default'].number]),
    defaultActiveKey: _vueTypes2['default'].oneOfType([_vueTypes2['default'].string, _vueTypes2['default'].number]),
    hideAdd: _vueTypes2['default'].bool.def(false),
    tabBarStyle: _vueTypes2['default'].object,
    tabBarExtraContent: _vueTypes2['default'].oneOfType([_vueTypes2['default'].string, _vueTypes2['default'].number, _vueTypes2['default'].func]),
    destroyInactiveTabPane: _vueTypes2['default'].bool.def(false),
    type: _vueTypes2['default'].oneOf(['line', 'card', 'editable-card']),
    tabPosition: _vueTypes2['default'].oneOf(['top', 'right', 'bottom', 'left']).def('top'),
    size: _vueTypes2['default'].oneOf(['default', 'small', 'large']),
    animated: _vueTypes2['default'].oneOfType([_vueTypes2['default'].bool, _vueTypes2['default'].object]),
    tabBarGutter: _vueTypes2['default'].number,
    renderTabBar: _vueTypes2['default'].func
  },
  mounted: function mounted() {
    var NO_FLEX = ' no-flex';
    var tabNode = this.$el;
    if (tabNode && !(0, _isFlexSupported2['default'])() && tabNode.className.indexOf(NO_FLEX) === -1) {
      tabNode.className += NO_FLEX;
    }
  },

  methods: {
    removeTab: function removeTab(targetKey, e) {
      e.stopPropagation();
      if (!targetKey) {
        return;
      }
      this.$emit('edit', targetKey, 'remove');
    },
    handleChange: function handleChange(activeKey) {
      this.$emit('change', activeKey);
    },
    createNewTab: function createNewTab(targetKey) {
      this.$emit('edit', targetKey, 'add');
    },
    onTabClick: function onTabClick(val) {
      this.$emit('tabClick', val);
    },
    onPrevClick: function onPrevClick(val) {
      this.$emit('prevClick', val);
    },
    onNextClick: function onNextClick(val) {
      this.$emit('nextClick', val);
    }
  },

  render: function render() {
    var _cls,
        _this = this,
        _contentCls;

    var h = arguments[0];

    var props = (0, _propsUtil.getOptionProps)(this);
    var prefixCls = props.prefixCls,
        size = props.size,
        _props$type = props.type,
        type = _props$type === undefined ? 'line' : _props$type,
        tabPosition = props.tabPosition,
        _props$animated = props.animated,
        animated = _props$animated === undefined ? true : _props$animated,
        hideAdd = props.hideAdd,
        renderTabBar = props.renderTabBar;

    var children = (0, _propsUtil.filterEmpty)(this.$slots['default']);

    var tabBarExtraContent = (0, _propsUtil.getComponentFromProp)(this, 'tabBarExtraContent');
    var tabPaneAnimated = (typeof animated === 'undefined' ? 'undefined' : (0, _typeof3['default'])(animated)) === 'object' ? animated.tabPane : animated;

    // card tabs should not have animation
    if (type !== 'line') {
      tabPaneAnimated = 'animated' in props ? tabPaneAnimated : false;
    }
    var cls = (_cls = {}, (0, _defineProperty3['default'])(_cls, prefixCls + '-vertical', tabPosition === 'left' || tabPosition === 'right'), (0, _defineProperty3['default'])(_cls, prefixCls + '-' + size, !!size), (0, _defineProperty3['default'])(_cls, prefixCls + '-card', type.indexOf('card') >= 0), (0, _defineProperty3['default'])(_cls, prefixCls + '-' + type, true), (0, _defineProperty3['default'])(_cls, prefixCls + '-no-animation', !tabPaneAnimated), _cls);
    // only card type tabs can be added and closed
    var childrenWithClose = [];
    if (type === 'editable-card') {
      childrenWithClose = [];
      children.forEach(function (child, index) {
        var props = (0, _propsUtil.getOptionProps)(child);
        var closable = props.closable;
        closable = typeof closable === 'undefined' ? true : closable;
        var closeIcon = closable ? h(_icon2['default'], {
          attrs: {
            type: 'close'
          },
          'class': prefixCls + '-close-x',
          on: {
            'click': function click(e) {
              return _this.removeTab(child.key, e);
            }
          }
        }) : null;
        childrenWithClose.push((0, _vnode.cloneElement)(child, {
          props: {
            tab: h(
              'div',
              { 'class': closable ? undefined : prefixCls + '-tab-unclosable' },
              [(0, _propsUtil.getComponentFromProp)(child, 'tab'), closeIcon]
            )
          },
          key: child.key || index
        }));
      });
      // Add new tab handler
      if (!hideAdd) {
        tabBarExtraContent = h('span', [h(_icon2['default'], {
          attrs: { type: 'plus' },
          'class': prefixCls + '-new-tab', on: {
            'click': this.createNewTab
          }
        }), tabBarExtraContent]);
      }
    }

    tabBarExtraContent = tabBarExtraContent ? h(
      'div',
      { 'class': prefixCls + '-extra-content' },
      [tabBarExtraContent]
    ) : null;

    var renderTabBarSlot = renderTabBar || this.$scopedSlots.renderTabBar;
    var tabBarProps = {
      props: (0, _extends3['default'])({}, this.$props, {
        tabBarExtraContent: tabBarExtraContent,
        renderTabBar: renderTabBarSlot
      }),
      on: this.$listeners
    };
    var contentCls = (_contentCls = {}, (0, _defineProperty3['default'])(_contentCls, prefixCls + '-' + tabPosition + '-content', true), (0, _defineProperty3['default'])(_contentCls, prefixCls + '-card-content', type.indexOf('card') >= 0), _contentCls);
    var tabsProps = {
      props: (0, _extends3['default'])({}, (0, _propsUtil.getOptionProps)(this), {
        tabBarPosition: tabPosition,
        renderTabBar: function renderTabBar() {
          return h(_TabBar2['default'], tabBarProps);
        },
        renderTabContent: function renderTabContent() {
          return h(_TabContent2['default'], { 'class': contentCls, attrs: { animated: tabPaneAnimated, animatedWithMargin: true }
          });
        },
        children: childrenWithClose.length > 0 ? childrenWithClose : children,
        __propsSymbol__: Symbol()
      }),
      on: (0, _extends3['default'])({}, this.$listeners, {
        change: this.handleChange
      }),
      'class': cls
    };
    return h(_src2['default'], tabsProps);
  }
};