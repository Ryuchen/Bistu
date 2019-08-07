'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _babelHelperVueJsxMergeProps = require('babel-helper-vue-jsx-merge-props');

var _babelHelperVueJsxMergeProps2 = _interopRequireDefault(_babelHelperVueJsxMergeProps);

var _extends2 = require('babel-runtime/helpers/extends');

var _extends3 = _interopRequireDefault(_extends2);

var _defineProperty2 = require('babel-runtime/helpers/defineProperty');

var _defineProperty3 = _interopRequireDefault(_defineProperty2);

var _wave = require('../_util/wave');

var _wave2 = _interopRequireDefault(_wave);

var _icon = require('../icon');

var _icon2 = _interopRequireDefault(_icon);

var _buttonTypes = require('./buttonTypes');

var _buttonTypes2 = _interopRequireDefault(_buttonTypes);

var _propsUtil = require('../_util/props-util');

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

var rxTwoCNChar = /^[\u4e00-\u9fa5]{2}$/;
var isTwoCNChar = rxTwoCNChar.test.bind(rxTwoCNChar);

var props = (0, _buttonTypes2['default'])();
exports['default'] = {
  name: 'AButton',
  inheritAttrs: false,
  __ANT_BUTTON: true,
  props: props,
  data: function data() {
    return {
      sizeMap: {
        large: 'lg',
        small: 'sm'
      },
      // clicked: false,
      sLoading: !!this.loading,
      hasTwoCNChar: false
    };
  },

  computed: {
    classes: function classes() {
      var _ref;

      var prefixCls = this.prefixCls,
          type = this.type,
          shape = this.shape,
          size = this.size,
          hasTwoCNChar = this.hasTwoCNChar,
          sLoading = this.sLoading,
          ghost = this.ghost,
          block = this.block,
          sizeMap = this.sizeMap,
          icon = this.icon,
          $slots = this.$slots;

      var sizeCls = sizeMap[size] || '';
      var children = (0, _propsUtil.filterEmpty)($slots['default']);
      return _ref = {}, (0, _defineProperty3['default'])(_ref, '' + prefixCls, true), (0, _defineProperty3['default'])(_ref, prefixCls + '-' + type, type), (0, _defineProperty3['default'])(_ref, prefixCls + '-' + shape, shape), (0, _defineProperty3['default'])(_ref, prefixCls + '-' + sizeCls, sizeCls), (0, _defineProperty3['default'])(_ref, prefixCls + '-icon-only', !children && children !== 0 && icon), (0, _defineProperty3['default'])(_ref, prefixCls + '-loading', sLoading), (0, _defineProperty3['default'])(_ref, prefixCls + '-background-ghost', ghost || type === 'ghost'), (0, _defineProperty3['default'])(_ref, prefixCls + '-two-chinese-chars', hasTwoCNChar), (0, _defineProperty3['default'])(_ref, prefixCls + '-block', block), _ref;
    }
  },
  watch: {
    loading: function loading(val) {
      var _this = this;

      clearTimeout(this.delayTimeout);
      if (typeof val !== 'boolean' && val && val.delay) {
        this.delayTimeout = setTimeout(function () {
          _this.sLoading = !!val;
        }, val.delay);
      } else {
        this.sLoading = !!val;
      }
    }
  },
  mounted: function mounted() {
    this.fixTwoCNChar();
  },
  updated: function updated() {
    this.fixTwoCNChar();
  },
  beforeDestroy: function beforeDestroy() {
    // if (this.timeout) {
    //   clearTimeout(this.timeout)
    // }
    if (this.delayTimeout) {
      clearTimeout(this.delayTimeout);
    }
  },

  methods: {
    fixTwoCNChar: function fixTwoCNChar() {
      // Fix for HOC usage like <FormatMessage />
      var node = this.$refs.buttonNode;
      if (!node) {
        return;
      }
      var buttonText = node.textContent || node.innerText;
      if (this.isNeedInserted() && isTwoCNChar(buttonText)) {
        if (!this.hasTwoCNChar) {
          this.hasTwoCNChar = true;
        }
      } else if (this.hasTwoCNChar) {
        this.hasTwoCNChar = false;
      }
    },
    handleClick: function handleClick(event) {
      var sLoading = this.$data.sLoading;

      if (sLoading) {
        return;
      }
      this.$emit('click', event);
    },
    insertSpace: function insertSpace(child, needInserted) {
      var h = this.$createElement;

      var SPACE = needInserted ? ' ' : '';
      if (typeof child.text === 'string') {
        var text = child.text.trim();
        if (isTwoCNChar(text)) {
          text = text.split('').join(SPACE);
        }
        return h('span', [text]);
      }
      return child;
    },
    isNeedInserted: function isNeedInserted() {
      var icon = this.icon,
          $slots = this.$slots;

      return $slots['default'] && $slots['default'].length === 1 && !icon;
    }
  },
  render: function render() {
    var _this2 = this;

    var h = arguments[0];
    var htmlType = this.htmlType,
        classes = this.classes,
        icon = this.icon,
        disabled = this.disabled,
        handleClick = this.handleClick,
        sLoading = this.sLoading,
        $slots = this.$slots,
        $attrs = this.$attrs,
        $listeners = this.$listeners;

    var buttonProps = {
      attrs: (0, _extends3['default'])({}, $attrs, {
        disabled: disabled
      }),
      'class': classes,
      on: (0, _extends3['default'])({}, $listeners, {
        click: handleClick
      })
    };
    var iconType = sLoading ? 'loading' : icon;
    var iconNode = iconType ? h(_icon2['default'], {
      attrs: { type: iconType }
    }) : null;
    var children = (0, _propsUtil.filterEmpty)($slots['default']);
    var kids = children.map(function (child) {
      return _this2.insertSpace(child, _this2.isNeedInserted());
    });

    if ($attrs.href !== undefined) {
      return h(
        'a',
        (0, _babelHelperVueJsxMergeProps2['default'])([buttonProps, { ref: 'buttonNode' }]),
        [iconNode, kids]
      );
    } else {
      return h(_wave2['default'], [h(
        'button',
        (0, _babelHelperVueJsxMergeProps2['default'])([buttonProps, { ref: 'buttonNode', attrs: { type: htmlType || 'button' }
        }]),
        [iconNode, kids]
      )]);
    }
  }
};