'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.AnchorLinkProps = undefined;

var _defineProperty2 = require('babel-runtime/helpers/defineProperty');

var _defineProperty3 = _interopRequireDefault(_defineProperty2);

var _vueTypes = require('../_util/vue-types');

var _vueTypes2 = _interopRequireDefault(_vueTypes);

var _propsUtil = require('../_util/props-util');

var _classnames = require('classnames');

var _classnames2 = _interopRequireDefault(_classnames);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

var AnchorLinkProps = exports.AnchorLinkProps = {
  prefixCls: _vueTypes2['default'].string,
  href: _vueTypes2['default'].string,
  title: _vueTypes2['default'].any
};

exports['default'] = {
  name: 'AAnchorLink',
  props: (0, _propsUtil.initDefaultProps)(AnchorLinkProps, {
    prefixCls: 'ant-anchor',
    href: '#'
  }),
  inject: {
    antAnchor: { 'default': function _default() {
        return {};
      } },
    antAnchorContext: { 'default': function _default() {
        return {};
      } }
  },
  watch: {
    href: function href(val, oldVal) {
      this.antAnchor.unregisterLink(oldVal);
      this.antAnchor.registerLink(val);
    }
  },

  mounted: function mounted() {
    this.antAnchor.registerLink(this.href);
  },
  beforeDestroy: function beforeDestroy() {
    this.antAnchor.unregisterLink(this.href);
  },

  methods: {
    handleClick: function handleClick(e) {
      this.antAnchor.scrollTo(this.href);
      var scrollTo = this.antAnchor.scrollTo;
      var _$props = this.$props,
          href = _$props.href,
          title = _$props.title;

      if (this.antAnchorContext.$emit) {
        this.antAnchorContext.$emit('click', e, { title: title, href: href });
      }
      scrollTo(href);
    }
  },
  render: function render() {
    var h = arguments[0];
    var prefixCls = this.prefixCls,
        href = this.href,
        $slots = this.$slots;

    var title = (0, _propsUtil.getComponentFromProp)(this, 'title');
    var active = this.antAnchor.$data.activeLink === href;
    var wrapperClassName = (0, _classnames2['default'])(prefixCls + '-link', (0, _defineProperty3['default'])({}, prefixCls + '-link-active', active));
    var titleClassName = (0, _classnames2['default'])(prefixCls + '-link-title', (0, _defineProperty3['default'])({}, prefixCls + '-link-title-active', active));
    return h(
      'div',
      { 'class': wrapperClassName },
      [h(
        'a',
        {
          'class': titleClassName,
          attrs: { href: href,
            title: typeof title === 'string' ? title : ''
          },
          on: {
            'click': this.handleClick
          }
        },
        [title]
      ), $slots['default']]
    );
  }
};