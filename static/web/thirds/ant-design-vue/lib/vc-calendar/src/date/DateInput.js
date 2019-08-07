'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _vueTypes = require('../../../_util/vue-types');

var _vueTypes2 = _interopRequireDefault(_vueTypes);

var _BaseMixin = require('../../../_util/BaseMixin');

var _BaseMixin2 = _interopRequireDefault(_BaseMixin);

var _propsUtil = require('../../../_util/props-util');

var _moment = require('moment');

var _moment2 = _interopRequireDefault(_moment);

var _util = require('../util');

var _env = require('../../../_util/env');

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

var DateInput = {
  mixins: [_BaseMixin2['default']],
  props: {
    prefixCls: _vueTypes2['default'].string,
    timePicker: _vueTypes2['default'].object,
    value: _vueTypes2['default'].object,
    disabledTime: _vueTypes2['default'].any,
    format: _vueTypes2['default'].oneOfType([_vueTypes2['default'].string, _vueTypes2['default'].arrayOf(_vueTypes2['default'].string)]),
    locale: _vueTypes2['default'].object,
    disabledDate: _vueTypes2['default'].func,
    // onChange: PropTypes.func,
    // onClear: PropTypes.func,
    placeholder: _vueTypes2['default'].string,
    // onSelect: PropTypes.func,
    selectedValue: _vueTypes2['default'].object,
    clearIcon: _vueTypes2['default'].any
  },

  data: function data() {
    var selectedValue = this.selectedValue;
    return {
      str: (0, _util.formatDate)(selectedValue, this.format),
      invalid: false,
      hasFocus: false
    };
  },

  watch: {
    selectedValue: function selectedValue() {
      this.updateState();
    },
    format: function format() {
      this.updateState();
    }
  },

  updated: function updated() {
    var _this = this;

    this.$nextTick(function () {
      if (_this.$data.hasFocus && !_this.invalid && !(_this.cachedSelectionStart === 0 && _this.cachedSelectionEnd === 0)) {
        _this.$refs.dateInputInstance.setSelectionRange(_this.cachedSelectionStart, _this.cachedSelectionEnd);
      }
    });
  },

  methods: {
    updateState: function updateState() {
      this.cachedSelectionStart = this.$refs.dateInputInstance.selectionStart;
      this.cachedSelectionEnd = this.$refs.dateInputInstance.selectionEnd;
      // when popup show, click body will call this, bug!
      var selectedValue = this.selectedValue;
      if (!this.$data.hasFocus) {
        this.setState({
          str: (0, _util.formatDate)(selectedValue, this.format),
          invalid: false
        });
      }
    },
    onInputChange: function onInputChange(event) {
      var str = event.target.value;
      // https://github.com/vueComponent/ant-design-vue/issues/92
      if (_env.isIE && !_env.isIE9 && this.str === str) {
        return;
      }
      var _$props = this.$props,
          disabledDate = _$props.disabledDate,
          format = _$props.format,
          selectedValue = _$props.selectedValue;

      // 没有内容，合法并直接退出

      if (!str) {
        this.__emit('change', null);
        this.setState({
          invalid: false,
          str: str
        });
        return;
      }

      var parsed = (0, _moment2['default'])(str, format, true);
      if (!parsed.isValid()) {
        this.setState({
          invalid: true,
          str: str
        });
        return;
      }
      var value = this.value.clone();
      value.year(parsed.year()).month(parsed.month()).date(parsed.date()).hour(parsed.hour()).minute(parsed.minute()).second(parsed.second());

      if (!value || disabledDate && disabledDate(value)) {
        this.setState({
          invalid: true,
          str: str
        });
        return;
      }

      if (selectedValue !== value || selectedValue && value && !selectedValue.isSame(value)) {
        this.setState({
          str: str
        });
        this.__emit('change', value);
      }
    },
    onClear: function onClear() {
      this.setState({
        str: ''
      });
      this.__emit('clear', null);
    },
    getRootDOMNode: function getRootDOMNode() {
      return this.$el;
    },
    focus: function focus() {
      if (this.$refs.dateInputInstance) {
        this.$refs.dateInputInstance.focus();
      }
    },
    onFocus: function onFocus() {
      this.setState({ hasFocus: true });
    },
    onBlur: function onBlur() {
      this.setState(function (prevState, prevProps) {
        return {
          hasFocus: false,
          str: (0, _util.formatDate)(prevProps.value, prevProps.format)
        };
      });
    }
  },

  render: function render() {
    var h = arguments[0];
    var invalid = this.invalid,
        str = this.str,
        locale = this.locale,
        prefixCls = this.prefixCls,
        placeholder = this.placeholder,
        disabled = this.disabled,
        showClear = this.showClear;

    var clearIcon = (0, _propsUtil.getComponentFromProp)(this, 'clearIcon');
    var invalidClass = invalid ? prefixCls + '-input-invalid' : '';
    return h(
      'div',
      { 'class': prefixCls + '-input-wrap' },
      [h(
        'div',
        { 'class': prefixCls + '-date-input-wrap' },
        [h('input', {
          ref: 'dateInputInstance',
          'class': prefixCls + '-input ' + invalidClass,
          domProps: {
            'value': str
          },
          attrs: {
            disabled: disabled,
            placeholder: placeholder
          },
          on: {
            'input': this.onInputChange,
            'focus': this.onFocus,
            'blur': this.onBlur
          }
        })]
      ), showClear ? h(
        'a',
        {
          attrs: { role: 'button', title: locale.clear },
          on: {
            'click': this.onClear
          }
        },
        [clearIcon || h('span', { 'class': prefixCls + '-clear-btn' })]
      ) : null]
    );
  }
};

exports['default'] = DateInput;