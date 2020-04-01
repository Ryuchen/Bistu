'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _objectWithoutProperties2 = require('babel-runtime/helpers/objectWithoutProperties');

var _objectWithoutProperties3 = _interopRequireDefault(_objectWithoutProperties2);

var _extends2 = require('babel-runtime/helpers/extends');

var _extends3 = _interopRequireDefault(_extends2);

var _Dialog = require('./Dialog');

var _Dialog2 = _interopRequireDefault(_Dialog);

var _ContainerRender = require('../_util/ContainerRender');

var _ContainerRender2 = _interopRequireDefault(_ContainerRender);

var _IDialogPropTypes = require('./IDialogPropTypes');

var _IDialogPropTypes2 = _interopRequireDefault(_IDialogPropTypes);

var _propsUtil = require('../_util/props-util');

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

var IDialogPropTypes = (0, _IDialogPropTypes2['default'])();
var openCount = 0;
var DialogWrap = {
  inheritAttrs: false,
  props: (0, _extends3['default'])({}, IDialogPropTypes, {
    visible: IDialogPropTypes.visible.def(false)
  }),
  data: function data() {
    openCount = this.visible ? openCount + 1 : openCount;
    this.renderComponent = function () {};
    this.removeContainer = function () {};
    return {};
  },

  watch: {
    visible: function visible(val, preVal) {
      openCount = val && !preVal ? openCount + 1 : openCount - 1;
    }
  },
  beforeDestroy: function beforeDestroy() {
    if (this.visible) {
      openCount = openCount ? openCount - 1 : openCount;
      this.renderComponent({
        afterClose: this.removeContainer,
        visible: false,
        on: {
          close: function close() {}
        }
      });
    } else {
      this.removeContainer();
    }
  },

  methods: {
    getComponent: function getComponent() {
      var extra = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : {};
      var h = this.$createElement;
      var $attrs = this.$attrs,
          $props = this.$props,
          $slots = this.$slots,
          getContainer = this.getContainer;
      var on = extra.on,
          otherProps = (0, _objectWithoutProperties3['default'])(extra, ['on']);

      var dialogProps = {
        props: (0, _extends3['default'])({}, $props, {
          dialogClass: (0, _propsUtil.getClass)(this),
          dialogStyle: (0, _propsUtil.getStyle)(this)
        }, otherProps, {
          getOpenCount: getContainer === false ? function () {
            return 2;
          } : function () {
            return openCount;
          }
        }),
        attrs: $attrs,
        ref: '_component',
        key: 'dialog',
        on: (0, _extends3['default'])({}, (0, _propsUtil.getListeners)(this), on)
      };
      return h(
        _Dialog2['default'],
        dialogProps,
        [$slots['default']]
      );
    },
    getContainer2: function getContainer2() {
      var container = document.createElement('div');
      if (this.getContainer) {
        this.getContainer().appendChild(container);
      } else {
        document.body.appendChild(container);
      }
      return container;
    }
  },

  render: function render() {
    var _this = this;

    var h = arguments[0];
    var visible = this.visible;

    return h(_ContainerRender2['default'], {
      attrs: {
        parent: this,
        visible: visible,
        autoDestroy: false,
        getComponent: this.getComponent,
        getContainer: this.getContainer2,
        children: function children(_ref) {
          var renderComponent = _ref.renderComponent,
              removeContainer = _ref.removeContainer;

          _this.renderComponent = renderComponent;
          _this.removeContainer = removeContainer;
          return null;
        }
      }
    });
  }
};

exports['default'] = DialogWrap;