'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _babelHelperVueJsxMergeProps = require('babel-helper-vue-jsx-merge-props');

var _babelHelperVueJsxMergeProps2 = _interopRequireDefault(_babelHelperVueJsxMergeProps);

var _defineProperty2 = require('babel-runtime/helpers/defineProperty');

var _defineProperty3 = _interopRequireDefault(_defineProperty2);

var _objectWithoutProperties2 = require('babel-runtime/helpers/objectWithoutProperties');

var _objectWithoutProperties3 = _interopRequireDefault(_objectWithoutProperties2);

var _extends2 = require('babel-runtime/helpers/extends');

var _extends3 = _interopRequireDefault(_extends2);

var _classnames = require('classnames');

var _classnames2 = _interopRequireDefault(_classnames);

var _Input = require('./Input');

var _Input2 = _interopRequireDefault(_Input);

var _icon = require('../icon');

var _icon2 = _interopRequireDefault(_icon);

var _inputProps = require('./inputProps');

var _inputProps2 = _interopRequireDefault(_inputProps);

var _button = require('../button');

var _button2 = _interopRequireDefault(_button);

var _vnode = require('../_util/vnode');

var _propsUtil = require('../_util/props-util');

var _vueTypes = require('../_util/vue-types');

var _vueTypes2 = _interopRequireDefault(_vueTypes);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

exports['default'] = {
  name: 'AInputSearch',
  inheritAttrs: false,
  model: {
    prop: 'value',
    event: 'change.value'
  },
  props: (0, _extends3['default'])({}, _inputProps2['default'], {
    prefixCls: {
      'default': 'ant-input-search',
      type: String
    },
    inputPrefixCls: {
      'default': 'ant-input',
      type: String
    },
    enterButton: _vueTypes2['default'].oneOfType([_vueTypes2['default'].bool, _vueTypes2['default'].string, _vueTypes2['default'].object])
  }),
  methods: {
    onSearch: function onSearch(e) {
      this.$emit('search', this.$refs.input.stateValue, e);
      this.$refs.input.focus();
    },
    focus: function focus() {
      this.$refs.input.focus();
    },
    blur: function blur() {
      this.$refs.input.blur();
    },
    getButtonOrIcon: function getButtonOrIcon() {
      var h = this.$createElement;
      var prefixCls = this.prefixCls,
          size = this.size,
          disabled = this.disabled;

      var enterButton = (0, _propsUtil.getComponentFromProp)(this, 'enterButton');
      var enterButtonAsElement = Array.isArray(enterButton) ? enterButton[0] : enterButton;
      var node = void 0;
      if (!enterButton) {
        node = h(_icon2['default'], { 'class': prefixCls + '-icon', attrs: { type: 'search' },
          key: 'searchIcon' });
      } else if (enterButtonAsElement.tag === 'button' || enterButtonAsElement.componentOptions && enterButtonAsElement.componentOptions.Ctor.extendOptions.__ANT_BUTTON) {
        node = (0, _vnode.cloneElement)(enterButtonAsElement, {
          'class': prefixCls + '-button',
          props: { size: size }
        });
      } else {
        node = h(
          _button2['default'],
          {
            'class': prefixCls + '-button',
            attrs: { type: 'primary',
              size: size,
              disabled: disabled
            },
            key: 'enterButton'
          },
          [enterButton === true ? h(_icon2['default'], {
            attrs: { type: 'search' }
          }) : enterButton]
        );
      }
      return (0, _vnode.cloneElement)(node, {
        on: {
          click: this.onSearch
        }
      });
    }
  },
  render: function render() {
    var _classNames;

    var h = arguments[0];

    var _getOptionProps = (0, _propsUtil.getOptionProps)(this),
        prefixCls = _getOptionProps.prefixCls,
        inputPrefixCls = _getOptionProps.inputPrefixCls,
        size = _getOptionProps.size,
        others = (0, _objectWithoutProperties3['default'])(_getOptionProps, ['prefixCls', 'inputPrefixCls', 'size']);

    var suffix = (0, _propsUtil.getComponentFromProp)(this, 'suffix');
    var enterButton = (0, _propsUtil.getComponentFromProp)(this, 'enterButton');
    var addonAfter = (0, _propsUtil.getComponentFromProp)(this, 'addonAfter');
    var addonBefore = (0, _propsUtil.getComponentFromProp)(this, 'addonBefore');
    var buttonOrIcon = this.getButtonOrIcon();
    var searchSuffix = suffix ? [suffix, buttonOrIcon] : buttonOrIcon;
    if (Array.isArray(searchSuffix)) {
      searchSuffix = searchSuffix.map(function (item, index) {
        if (!(0, _propsUtil.isValidElement)(item) || item.key) {
          return item;
        }
        return (0, _vnode.cloneElement)(item, { key: index });
      });
    }
    var inputClassName = (0, _classnames2['default'])(prefixCls, (_classNames = {}, (0, _defineProperty3['default'])(_classNames, prefixCls + '-enter-button', !!enterButton), (0, _defineProperty3['default'])(_classNames, prefixCls + '-' + size, !!size), _classNames));
    var on = (0, _extends3['default'])({}, this.$listeners);
    delete on.search;
    var inputProps = {
      props: (0, _extends3['default'])({}, others, {
        prefixCls: inputPrefixCls,
        size: size,
        suffix: searchSuffix,
        addonAfter: addonAfter,
        addonBefore: addonBefore
      }),
      attrs: this.$attrs,
      on: (0, _extends3['default'])({
        pressEnter: this.onSearch
      }, on)
    };
    return h(_Input2['default'], (0, _babelHelperVueJsxMergeProps2['default'])([inputProps, { 'class': inputClassName, ref: 'input' }]));
  }
};