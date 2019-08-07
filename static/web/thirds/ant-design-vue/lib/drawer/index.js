'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _defineProperty2 = require('babel-runtime/helpers/defineProperty');

var _defineProperty3 = _interopRequireDefault(_defineProperty2);

var _objectWithoutProperties2 = require('babel-runtime/helpers/objectWithoutProperties');

var _objectWithoutProperties3 = _interopRequireDefault(_objectWithoutProperties2);

var _extends2 = require('babel-runtime/helpers/extends');

var _extends3 = _interopRequireDefault(_extends2);

var _classnames2 = require('classnames');

var _classnames3 = _interopRequireDefault(_classnames2);

var _src = require('../vc-drawer/src');

var _src2 = _interopRequireDefault(_src);

var _vueTypes = require('../_util/vue-types');

var _vueTypes2 = _interopRequireDefault(_vueTypes);

var _BaseMixin = require('../_util/BaseMixin');

var _BaseMixin2 = _interopRequireDefault(_BaseMixin);

var _icon = require('../icon');

var _icon2 = _interopRequireDefault(_icon);

var _propsUtil = require('../_util/props-util');

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

var Drawer = {
  name: 'ADrawer',
  props: {
    closable: _vueTypes2['default'].bool.def(true),
    destroyOnClose: _vueTypes2['default'].bool,
    getContainer: _vueTypes2['default'].any,
    maskClosable: _vueTypes2['default'].bool.def(true),
    mask: _vueTypes2['default'].bool.def(true),
    maskStyle: _vueTypes2['default'].object,
    wrapStyle: _vueTypes2['default'].object,
    title: _vueTypes2['default'].any,
    visible: _vueTypes2['default'].bool,
    width: _vueTypes2['default'].oneOfType([_vueTypes2['default'].string, _vueTypes2['default'].number]).def(256),
    height: _vueTypes2['default'].oneOfType([_vueTypes2['default'].string, _vueTypes2['default'].number]).def(256),
    zIndex: _vueTypes2['default'].number,
    prefixCls: _vueTypes2['default'].string.def('ant-drawer'),
    placement: _vueTypes2['default'].oneOf(['top', 'right', 'bottom', 'left']).def('right'),
    level: _vueTypes2['default'].any.def(null),
    wrapClassName: _vueTypes2['default'].string, // not use class like react, vue will add class to root dom
    handle: _vueTypes2['default'].any
  },
  mixins: [_BaseMixin2['default']],
  data: function data() {
    this.destoryClose = false;
    this.preVisible = this.$props.visible;
    return {
      _push: false
    };
  },

  inject: {
    parentDrawer: {
      'default': function _default() {
        return null;
      }
    }
  },
  provide: function provide() {
    return {
      parentDrawer: this
    };
  },
  updated: function updated() {
    var _this = this;

    this.$nextTick(function () {
      if (_this.preVisible !== _this.visible && _this.parentDrawer) {
        if (_this.visible) {
          _this.parentDrawer.push();
        } else {
          _this.parentDrawer.pull();
        }
      }
      _this.preVisible = _this.visible;
    });
  },

  methods: {
    close: function close(e) {
      if (this.visible !== undefined) {
        this.$emit('close', e);
        return;
      }
    },
    onMaskClick: function onMaskClick(e) {
      if (!this.maskClosable) {
        return;
      }
      this.close(e);
    },
    push: function push() {
      this.setState({
        _push: true
      });
    },
    pull: function pull() {
      this.setState({
        _push: false
      });
    },
    onDestoryTransitionEnd: function onDestoryTransitionEnd() {
      var isDestroyOnClose = this.getDestoryOnClose();
      if (!isDestroyOnClose) {
        return;
      }
      if (!this.visible) {
        this.destoryClose = true;
        this.$forceUpdate();
      }
    },
    getDestoryOnClose: function getDestoryOnClose() {
      return this.destroyOnClose && !this.visible;
    },

    // get drawar push width or height
    getPushTransform: function getPushTransform(placement) {
      if (placement === 'left' || placement === 'right') {
        return 'translateX(' + (placement === 'left' ? 180 : -180) + 'px)';
      }
      if (placement === 'top' || placement === 'bottom') {
        return 'translateY(' + (placement === 'top' ? 180 : -180) + 'px)';
      }
    },

    // render drawer body dom
    renderBody: function renderBody() {
      var h = this.$createElement;

      if (this.destoryClose && !this.visible) {
        return null;
      }
      this.destoryClose = false;
      var placement = this.$props.placement;


      var containerStyle = placement === 'left' || placement === 'right' ? {
        overflow: 'auto',
        height: '100%'
      } : {};

      var isDestroyOnClose = this.getDestoryOnClose();
      if (isDestroyOnClose) {
        // Increase the opacity transition, delete children after closing.
        containerStyle.opacity = 0;
        containerStyle.transition = 'opacity .3s';
      }
      var _$props = this.$props,
          prefixCls = _$props.prefixCls,
          closable = _$props.closable;

      var title = (0, _propsUtil.getComponentFromProp)(this, 'title');
      // is have header dom
      var header = void 0;
      if (title) {
        header = h(
          'div',
          { key: 'header', 'class': prefixCls + '-header' },
          [h(
            'div',
            { 'class': prefixCls + '-title' },
            [title]
          )]
        );
      }
      // is have closer button
      var closer = void 0;
      if (closable) {
        closer = h(
          'button',
          { key: 'closer', on: {
              'click': this.close
            },
            attrs: { 'aria-label': 'Close' },
            'class': prefixCls + '-close' },
          [h(
            'span',
            { 'class': prefixCls + '-close-x' },
            [h(_icon2['default'], {
              attrs: { type: 'close' }
            })]
          )]
        );
      }

      return h(
        'div',
        {
          'class': prefixCls + '-wrapper-body',
          style: containerStyle,
          on: {
            'transitionend': this.onDestoryTransitionEnd
          }
        },
        [header, closer, h(
          'div',
          { key: 'body', 'class': prefixCls + '-body' },
          [this.$slots['default']]
        )]
      );
    },
    getRcDrawerStyle: function getRcDrawerStyle() {
      var _$props2 = this.$props,
          zIndex = _$props2.zIndex,
          placement = _$props2.placement,
          maskStyle = _$props2.maskStyle,
          wrapStyle = _$props2.wrapStyle;
      var push = this.$data._push;

      return (0, _extends3['default'])({}, maskStyle, {
        zIndex: zIndex,
        transform: push ? this.getPushTransform(placement) : undefined
      }, wrapStyle);
    }
  },
  render: function render() {
    var _classnames;

    var h = arguments[0];

    var props = (0, _propsUtil.getOptionProps)(this);
    var width = props.width,
        height = props.height,
        visible = props.visible,
        placement = props.placement,
        wrapClassName = props.wrapClassName,
        rest = (0, _objectWithoutProperties3['default'])(props, ['width', 'height', 'visible', 'placement', 'wrapClassName']);

    var haveMask = rest.mask ? '' : 'no-mask';
    var offsetStyle = {};
    if (placement === 'left' || placement === 'right') {
      offsetStyle.width = typeof width === 'number' ? width + 'px' : width;
    } else {
      offsetStyle.height = typeof height === 'number' ? height + 'px' : height;
    }
    var handler = (0, _propsUtil.getComponentFromProp)(this, 'handle') || false;
    var vcDrawerProps = {
      props: (0, _extends3['default'])({}, rest, {
        handler: handler
      }, offsetStyle, {
        open: visible,
        showMask: props.mask,
        placement: placement,
        className: (0, _classnames3['default'])((_classnames = {}, (0, _defineProperty3['default'])(_classnames, wrapClassName, !!wrapClassName), (0, _defineProperty3['default'])(_classnames, haveMask, !!haveMask), _classnames)),
        wrapStyle: this.getRcDrawerStyle()
      }),
      on: (0, _extends3['default'])({
        maskClick: this.onMaskClick
      }, this.$listeners)
    };
    return h(
      _src2['default'],
      vcDrawerProps,
      [this.renderBody()]
    );
  }
};

/* istanbul ignore next */
Drawer.install = function (Vue) {
  Vue.component(Drawer.name, Drawer);
};

exports['default'] = Drawer;