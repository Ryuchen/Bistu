import _objectWithoutProperties from 'babel-runtime/helpers/objectWithoutProperties';
import _extends from 'babel-runtime/helpers/extends';
import Dialog from './Dialog';
import ContainerRender from '../_util/ContainerRender';
import getDialogPropTypes from './IDialogPropTypes';
import { getStyle, getClass, getListeners } from '../_util/props-util';
var IDialogPropTypes = getDialogPropTypes();
var openCount = 0;
var DialogWrap = {
  inheritAttrs: false,
  props: _extends({}, IDialogPropTypes, {
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
          otherProps = _objectWithoutProperties(extra, ['on']);

      var dialogProps = {
        props: _extends({}, $props, {
          dialogClass: getClass(this),
          dialogStyle: getStyle(this)
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
        on: _extends({}, getListeners(this), on)
      };
      return h(
        Dialog,
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

    return h(ContainerRender, {
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

export default DialogWrap;