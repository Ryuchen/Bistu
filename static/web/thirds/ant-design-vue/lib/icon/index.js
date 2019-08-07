'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _babelHelperVueJsxMergeProps = require('babel-helper-vue-jsx-merge-props');

var _babelHelperVueJsxMergeProps2 = _interopRequireDefault(_babelHelperVueJsxMergeProps);

var _defineProperty2 = require('babel-runtime/helpers/defineProperty');

var _defineProperty3 = _interopRequireDefault(_defineProperty2);

var _extends3 = require('babel-runtime/helpers/extends');

var _extends4 = _interopRequireDefault(_extends3);

var _toConsumableArray2 = require('babel-runtime/helpers/toConsumableArray');

var _toConsumableArray3 = _interopRequireDefault(_toConsumableArray2);

var _classnames = require('classnames');

var _classnames2 = _interopRequireDefault(_classnames);

var _dist = require('@ant-design/icons/lib/dist');

var allIcons = _interopRequireWildcard(_dist);

var _iconsVue = require('@ant-design/icons-vue');

var _iconsVue2 = _interopRequireDefault(_iconsVue);

var _vueTypes = require('../_util/vue-types');

var _vueTypes2 = _interopRequireDefault(_vueTypes);

var _IconFont = require('./IconFont');

var _IconFont2 = _interopRequireDefault(_IconFont);

var _utils = require('./utils');

var _warning = require('../_util/warning');

var _warning2 = _interopRequireDefault(_warning);

var _twoTonePrimaryColor = require('./twoTonePrimaryColor');

var _propsUtil = require('../_util/props-util');

function _interopRequireWildcard(obj) { if (obj && obj.__esModule) { return obj; } else { var newObj = {}; if (obj != null) { for (var key in obj) { if (Object.prototype.hasOwnProperty.call(obj, key)) newObj[key] = obj[key]; } } newObj['default'] = obj; return newObj; } }

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

// Initial setting
_iconsVue2['default'].add.apply(_iconsVue2['default'], (0, _toConsumableArray3['default'])(Object.keys(allIcons).map(function (key) {
  return allIcons[key];
})));
(0, _twoTonePrimaryColor.setTwoToneColor)('#1890ff');
var defaultTheme = 'outlined';
var dangerousTheme = void 0;

var Icon = {
  functional: true,
  name: 'AIcon',
  props: {
    type: _vueTypes2['default'].string,
    component: _vueTypes2['default'].any,
    viewBox: _vueTypes2['default'].any,
    spin: _vueTypes2['default'].bool.def(false),
    theme: _vueTypes2['default'].oneOf(['filled', 'outlined', 'twoTone']),
    twoToneColor: _vueTypes2['default'].string
  },
  render: function render(h, context) {
    var _extends2;

    var props = context.props,
        slots = context.slots,
        listeners = context.listeners,
        data = context.data;
    var type = props.type,
        Component = props.component,
        viewBox = props.viewBox,
        spin = props.spin,
        theme = props.theme,
        twoToneColor = props.twoToneColor;

    var slotsMap = slots();
    var children = (0, _propsUtil.filterEmpty)(slotsMap['default']);
    children = children.length === 0 ? undefined : children;
    (0, _warning2['default'])(Boolean(type || Component || children), 'Icon should have `type` prop or `component` prop or `children`.');

    var classString = (0, _classnames2['default'])((0, _extends4['default'])({}, (0, _propsUtil.getClass)(context), (_extends2 = {}, (0, _defineProperty3['default'])(_extends2, 'anticon', true), (0, _defineProperty3['default'])(_extends2, 'anticon-' + type, !!type), _extends2)));

    var svgClassString = (0, _classnames2['default'])((0, _defineProperty3['default'])({}, 'anticon-spin', !!spin || type === 'loading'));

    var innerNode = void 0;

    // component > children > type
    if (Component) {
      var innerSvgProps = {
        attrs: (0, _extends4['default'])({}, _utils.svgBaseProps, {
          viewBox: viewBox
        }),
        'class': svgClassString
      };
      if (!viewBox) {
        delete innerSvgProps.attrs.viewBox;
      }

      innerNode = h(
        Component,
        innerSvgProps,
        [children]
      );
    }
    if (children) {
      (0, _warning2['default'])(Boolean(viewBox) || children.length === 1 && children[0].tag === 'use', 'Make sure that you provide correct `viewBox`' + ' prop (default `0 0 1024 1024`) to the icon.');
      var _innerSvgProps = {
        attrs: (0, _extends4['default'])({}, _utils.svgBaseProps),
        'class': svgClassString
      };
      innerNode = h(
        'svg',
        (0, _babelHelperVueJsxMergeProps2['default'])([_innerSvgProps, {
          attrs: { viewBox: viewBox }
        }]),
        [children]
      );
    }

    if (typeof type === 'string') {
      var computedType = type;
      if (theme) {
        var themeInName = (0, _utils.getThemeFromTypeName)(type);
        (0, _warning2['default'])(!themeInName || theme === themeInName, 'The icon name \'' + type + '\' already specify a theme \'' + themeInName + '\',' + (' the \'theme\' prop \'' + theme + '\' will be ignored.'));
      }
      computedType = (0, _utils.withThemeSuffix)((0, _utils.removeTypeTheme)((0, _utils.alias)(computedType)), dangerousTheme || theme || defaultTheme);
      innerNode = h(_iconsVue2['default'], {
        attrs: {
          focusable: 'false',

          type: computedType,
          primaryColor: twoToneColor
        },
        'class': svgClassString });
    }
    // functional component not support nativeOn，https://github.com/vuejs/vue/issues/7526
    var iProps = (0, _extends4['default'])({}, data, {
      on: (0, _extends4['default'])({}, listeners, data.nativeOn),
      'class': classString,
      staticClass: ''
    });
    return h(
      'i',
      iProps,
      [innerNode]
    );
  }
};

Icon.createFromIconfontCN = _IconFont2['default'];
Icon.getTwoToneColor = _twoTonePrimaryColor.getTwoToneColor;
Icon.setTwoToneColor = _twoTonePrimaryColor.setTwoToneColor;

/* istanbul ignore next */
Icon.install = function (Vue) {
  Vue.component(Icon.name, Icon);
};

exports['default'] = Icon;