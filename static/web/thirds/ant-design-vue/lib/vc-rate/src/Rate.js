'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _vueTypes = require('../../_util/vue-types');

var _vueTypes2 = _interopRequireDefault(_vueTypes);

var _classnames = require('classnames');

var _classnames2 = _interopRequireDefault(_classnames);

var _KeyCode = require('../../_util/KeyCode');

var _KeyCode2 = _interopRequireDefault(_KeyCode);

var _propsUtil = require('../../_util/props-util');

var _BaseMixin = require('../../_util/BaseMixin');

var _BaseMixin2 = _interopRequireDefault(_BaseMixin);

var _util = require('./util');

var _Star = require('./Star');

var _Star2 = _interopRequireDefault(_Star);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

var rateProps = {
  disabled: _vueTypes2['default'].bool,
  value: _vueTypes2['default'].number,
  defaultValue: _vueTypes2['default'].number,
  count: _vueTypes2['default'].number,
  allowHalf: _vueTypes2['default'].bool,
  allowClear: _vueTypes2['default'].bool,
  prefixCls: _vueTypes2['default'].string,
  character: _vueTypes2['default'].any,
  tabIndex: _vueTypes2['default'].number,
  autoFocus: _vueTypes2['default'].bool
};

function noop() {}

exports['default'] = {
  name: 'Rate',
  mixins: [_BaseMixin2['default']],
  model: {
    prop: 'value',
    event: 'change'
  },
  props: (0, _propsUtil.initDefaultProps)(rateProps, {
    defaultValue: 0,
    count: 5,
    allowHalf: false,
    allowClear: true,
    prefixCls: 'rc-rate',
    tabIndex: 0,
    character: '★'
  }),
  data: function data() {
    var value = this.value;
    if (!(0, _propsUtil.hasProp)(this, 'value')) {
      value = this.defaultValue;
    }
    return {
      sValue: value,
      focused: false,
      cleanedValue: null,
      hoverValue: undefined
    };
  },

  watch: {
    value: function value(val) {
      this.setState({
        sValue: val
      });
    }
  },
  mounted: function mounted() {
    var _this = this;

    this.$nextTick(function () {
      if (_this.autoFocus && !_this.disabled) {
        _this.focus();
      }
    });
  },

  methods: {
    onHover: function onHover(event, index) {
      var hoverValue = this.getStarValue(index, event.pageX);
      var cleanedValue = this.cleanedValue;

      if (hoverValue !== cleanedValue) {
        this.setState({
          hoverValue: hoverValue,
          cleanedValue: null
        });
      }
      this.$emit('hoverChange', hoverValue);
    },
    onMouseLeave: function onMouseLeave() {
      this.setState({
        hoverValue: undefined,
        cleanedValue: null
      });
      this.$emit('hoverChange', undefined);
    },
    onClick: function onClick(event, index) {
      var value = this.getStarValue(index, event.pageX);
      var isReset = false;
      if (this.allowClear) {
        isReset = value === this.sValue;
      }
      this.onMouseLeave(true);
      this.changeValue(isReset ? 0 : value);
      this.setState({
        cleanedValue: isReset ? value : null
      });
    },
    onFocus: function onFocus() {
      this.setState({
        focused: true
      });
      this.$emit('focus');
    },
    onBlur: function onBlur() {
      this.setState({
        focused: false
      });
      this.$emit('blur');
    },
    onKeyDown: function onKeyDown(event) {
      var keyCode = event.keyCode;
      var count = this.count,
          allowHalf = this.allowHalf;
      var sValue = this.sValue;

      if (keyCode === _KeyCode2['default'].RIGHT && sValue < count) {
        if (allowHalf) {
          sValue += 0.5;
        } else {
          sValue += 1;
        }
        this.changeValue(sValue);
        event.preventDefault();
      } else if (keyCode === _KeyCode2['default'].LEFT && sValue > 0) {
        if (allowHalf) {
          sValue -= 0.5;
        } else {
          sValue -= 1;
        }
        this.changeValue(sValue);
        event.preventDefault();
      }
      this.$emit('keydown', event);
    },
    getStarDOM: function getStarDOM(index) {
      return this.$refs['stars' + index].$el;
    },
    getStarValue: function getStarValue(index, x) {
      var value = index + 1;
      if (this.allowHalf) {
        var starEle = this.getStarDOM(index);
        var leftDis = (0, _util.getOffsetLeft)(starEle);
        var width = starEle.clientWidth;
        if (x - leftDis < width / 2) {
          value -= 0.5;
        }
      }
      return value;
    },
    focus: function focus() {
      if (!this.disabled) {
        this.$refs.rateRef.focus();
      }
    },
    blur: function blur() {
      if (!this.disabled) {
        this.$refs.rateRef.blur();
      }
    },
    changeValue: function changeValue(value) {
      if (!(0, _propsUtil.hasProp)(this, 'value')) {
        this.setState({
          sValue: value
        });
      }
      this.$emit('change', value);
    }
  },
  render: function render() {
    var h = arguments[0];

    var _getOptionProps = (0, _propsUtil.getOptionProps)(this),
        count = _getOptionProps.count,
        allowHalf = _getOptionProps.allowHalf,
        prefixCls = _getOptionProps.prefixCls,
        disabled = _getOptionProps.disabled,
        tabIndex = _getOptionProps.tabIndex;

    var sValue = this.sValue,
        hoverValue = this.hoverValue,
        focused = this.focused;

    var stars = [];
    var disabledClass = disabled ? prefixCls + '-disabled' : '';
    var character = (0, _propsUtil.getComponentFromProp)(this, 'character');
    for (var index = 0; index < count; index++) {
      var starProps = {
        props: {
          index: index,
          count: count,
          disabled: disabled,
          prefixCls: prefixCls + '-star',
          allowHalf: allowHalf,
          value: hoverValue === undefined ? sValue : hoverValue,
          character: character,
          focused: focused
        },
        on: {
          click: this.onClick,
          hover: this.onHover
        },
        key: index,
        ref: 'stars' + index
      };
      stars.push(h(_Star2['default'], starProps));
    }
    return h(
      'ul',
      {
        'class': (0, _classnames2['default'])(prefixCls, disabledClass),
        on: {
          'mouseleave': disabled ? noop : this.onMouseLeave,
          'focus': disabled ? noop : this.onFocus,
          'blur': disabled ? noop : this.onBlur,
          'keydown': disabled ? noop : this.onKeyDown
        },
        attrs: {
          tabIndex: disabled ? -1 : tabIndex,

          role: 'radiogroup'
        },

        ref: 'rateRef' },
      [stars]
    );
  }
};