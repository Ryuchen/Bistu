'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _defineProperty2 = require('babel-runtime/helpers/defineProperty');

var _defineProperty3 = _interopRequireDefault(_defineProperty2);

var _toConsumableArray2 = require('babel-runtime/helpers/toConsumableArray');

var _toConsumableArray3 = _interopRequireDefault(_toConsumableArray2);

var _vueTypes = require('../../_util/vue-types');

var _vueTypes2 = _interopRequireDefault(_vueTypes);

var _BaseMixin = require('../../_util/BaseMixin');

var _BaseMixin2 = _interopRequireDefault(_BaseMixin);

var _propsUtil = require('../../_util/props-util');

var _classnames = require('classnames');

var _classnames2 = _interopRequireDefault(_classnames);

var _isNegativeZero = require('is-negative-zero');

var _isNegativeZero2 = _interopRequireDefault(_isNegativeZero);

var _KeyCode = require('../../_util/KeyCode');

var _KeyCode2 = _interopRequireDefault(_KeyCode);

var _InputHandler = require('./InputHandler');

var _InputHandler2 = _interopRequireDefault(_InputHandler);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

function noop() {} // based on rc-input-number 4.3.8


function preventDefault(e) {
  e.preventDefault();
}

function defaultParser(input) {
  return input.replace(/[^\w\.-]+/g, '');
}

/**
 * When click and hold on a button - the speed of auto changin the value.
 */
var SPEED = 200;

/**
 * When click and hold on a button - the delay before auto changin the value.
 */
var DELAY = 600;

/**
 * Max Safe Integer -- on IE this is not available, so manually set the number in that case.
 * The reason this is used, instead of Infinity is because numbers above the MSI are unstable
 */
var MAX_SAFE_INTEGER = Number.MAX_SAFE_INTEGER || Math.pow(2, 53) - 1;
var inputNumberProps = {
  value: _vueTypes2['default'].oneOfType([_vueTypes2['default'].number, _vueTypes2['default'].string]),
  defaultValue: _vueTypes2['default'].oneOfType([_vueTypes2['default'].number, _vueTypes2['default'].string]),
  focusOnUpDown: _vueTypes2['default'].bool,
  autoFocus: _vueTypes2['default'].bool,
  // onChange: PropTypes.func,
  // onKeyDown: PropTypes.func,
  // onKeyUp: PropTypes.func,
  prefixCls: _vueTypes2['default'].string,
  tabIndex: _vueTypes2['default'].oneOfType([_vueTypes2['default'].string, _vueTypes2['default'].number]),
  placeholder: _vueTypes2['default'].string,
  disabled: _vueTypes2['default'].bool,
  // onFocus: PropTypes.func,
  // onBlur: PropTypes.func,
  readOnly: _vueTypes2['default'].bool,
  max: _vueTypes2['default'].number,
  min: _vueTypes2['default'].number,
  step: _vueTypes2['default'].oneOfType([_vueTypes2['default'].number, _vueTypes2['default'].string]),
  upHandler: _vueTypes2['default'].any,
  downHandler: _vueTypes2['default'].any,
  useTouch: _vueTypes2['default'].bool,
  formatter: _vueTypes2['default'].func,
  parser: _vueTypes2['default'].func,
  // onMouseEnter: PropTypes.func,
  // onMouseLeave: PropTypes.func,
  // onMouseOver: PropTypes.func,
  // onMouseOut: PropTypes.func,
  precision: _vueTypes2['default'].number,
  required: _vueTypes2['default'].bool,
  pattern: _vueTypes2['default'].string,
  decimalSeparator: _vueTypes2['default'].string,
  autoComplete: _vueTypes2['default'].string,
  title: _vueTypes2['default'].string
};

exports['default'] = {
  name: 'InputNumber',
  mixins: [_BaseMixin2['default']],
  model: {
    prop: 'value',
    event: 'change'
  },
  props: (0, _propsUtil.initDefaultProps)(inputNumberProps, {
    focusOnUpDown: true,
    useTouch: false,
    prefixCls: 'rc-input-number',
    min: -MAX_SAFE_INTEGER,
    step: 1,
    parser: defaultParser,
    required: false,
    autoComplete: 'off'
  }),
  data: function data() {
    var value = void 0;
    if ((0, _propsUtil.hasProp)(this, 'value')) {
      value = this.value;
    } else {
      value = this.defaultValue;
    }
    value = this.toNumber(value);

    return {
      inputValue: this.toPrecisionAsStep(value),
      sValue: value,
      focused: this.autoFocus
    };
  },
  mounted: function mounted() {
    var _this = this;

    this.$nextTick(function () {
      if (_this.autoFocus && !_this.disabled) {
        _this.focus();
      }
      _this.updatedFunc();
    });
  },
  beforeUpdate: function beforeUpdate() {
    var _this2 = this;

    this.$nextTick(function () {
      try {
        _this2.start = _this2.$refs.inputRef.selectionStart;
        _this2.end = _this2.$refs.inputRef.selectionEnd;
      } catch (e) {
        // Fix error in Chrome:
        // Failed to read the 'selectionStart' property from 'HTMLInputElement'
        // http://stackoverflow.com/q/21177489/3040605
      }
    });
  },
  updated: function updated() {
    var _this3 = this;

    this.$nextTick(function () {
      _this3.updatedFunc();
    });
  },
  beforeDestroy: function beforeDestroy() {
    this.stop();
  },

  watch: {
    value: function value(val) {
      var value = this.focused ? val : this.getValidValue(val, this.min, this.max);
      this.setState({
        sValue: val,
        inputValue: this.inputting ? value : this.toPrecisionAsStep(value)
      });
    },
    max: function max(val) {
      var props = (0, _propsUtil.getOptionProps)(this);
      // Trigger onChange when max or min change
      // https://github.com/ant-design/ant-design/issues/11574
      var nextValue = 'value' in props ? props.value : this.sValue;
      // ref: null < 20 === true
      // https://github.com/ant-design/ant-design/issues/14277
      if (typeof nextValue === 'number' && nextValue > val) {
        this.__emit('change', val);
      }
    },
    min: function min(val) {
      var props = (0, _propsUtil.getOptionProps)(this);
      var nextValue = 'value' in props ? props.value : this.sValue;
      if (typeof nextValue === 'number' && nextValue < val) {
        this.__emit('change', val);
      }
    }
  },
  methods: {
    updatedFunc: function updatedFunc() {
      var inputElem = this.$refs.inputRef;
      // Restore cursor
      try {
        // Firefox set the input cursor after it get focused.
        // This caused that if an input didn't init with the selection,
        // set will cause cursor not correct when first focus.
        // Safari will focus input if set selection. We need skip this.
        if (this.cursorStart !== undefined && this.focused) {
          // In most cases, the string after cursor is stable.
          // We can move the cursor before it

          if (
          // If not match full str, try to match part of str
          !this.partRestoreByAfter(this.cursorAfter) && this.sValue !== this.value) {
            // If not match any of then, let's just keep the position
            // TODO: Logic should not reach here, need check if happens
            var pos = this.cursorStart + 1;

            // If not have last string, just position to the end
            if (!this.cursorAfter) {
              pos = inputElem.value.length;
            } else if (this.lastKeyCode === _KeyCode2['default'].BACKSPACE) {
              pos = this.cursorStart - 1;
            } else if (this.lastKeyCode === _KeyCode2['default'].DELETE) {
              pos = this.cursorStart;
            }
            this.fixCaret(pos, pos);
          } else if (this.currentValue === inputElem.value) {
            // Handle some special key code
            switch (this.lastKeyCode) {
              case _KeyCode2['default'].BACKSPACE:
                this.fixCaret(this.cursorStart - 1, this.cursorStart - 1);
                break;
              case _KeyCode2['default'].DELETE:
                this.fixCaret(this.cursorStart + 1, this.cursorStart + 1);
                break;
              default:
              // Do nothing
            }
          }
        }
      } catch (e) {}
      // Do nothing

      // Reset last key
      this.lastKeyCode = null;

      // pressingUpOrDown is true means that someone just click up or down button
      if (!this.pressingUpOrDown) {
        return;
      }
      if (this.focusOnUpDown && this.focused) {
        if (document.activeElement !== inputElem) {
          this.focus();
        }
      }

      this.pressingUpOrDown = false;
    },
    onKeyDown: function onKeyDown(e) {
      if (e.keyCode === _KeyCode2['default'].UP) {
        var ratio = this.getRatio(e);
        this.up(e, ratio);
        this.stop();
      } else if (e.keyCode === _KeyCode2['default'].DOWN) {
        var _ratio = this.getRatio(e);
        this.down(e, _ratio);
        this.stop();
      }
      // Trigger user key down
      this.recordCursorPosition();
      this.lastKeyCode = e.keyCode;

      for (var _len = arguments.length, args = Array(_len > 1 ? _len - 1 : 0), _key = 1; _key < _len; _key++) {
        args[_key - 1] = arguments[_key];
      }

      this.$emit.apply(this, ['keydown', e].concat((0, _toConsumableArray3['default'])(args)));
    },
    onKeyUp: function onKeyUp(e) {
      this.stop();

      this.recordCursorPosition();

      for (var _len2 = arguments.length, args = Array(_len2 > 1 ? _len2 - 1 : 0), _key2 = 1; _key2 < _len2; _key2++) {
        args[_key2 - 1] = arguments[_key2];
      }

      this.$emit.apply(this, ['keyup', e].concat((0, _toConsumableArray3['default'])(args)));
    },
    onChange: function onChange(e) {
      if (this.focused) {
        this.inputting = true;
      }
      var input = this.parser(this.getValueFromEvent(e));
      this.setState({ inputValue: input });
      this.$emit('change', this.toNumberWhenUserInput(input)); // valid number or invalid string
    },
    onFocus: function onFocus() {
      this.setState({
        focused: true
      });

      for (var _len3 = arguments.length, args = Array(_len3), _key3 = 0; _key3 < _len3; _key3++) {
        args[_key3] = arguments[_key3];
      }

      this.$emit.apply(this, ['focus'].concat((0, _toConsumableArray3['default'])(args)));
    },
    onBlur: function onBlur(e) {
      var _this4 = this;

      for (var _len4 = arguments.length, args = Array(_len4 > 1 ? _len4 - 1 : 0), _key4 = 1; _key4 < _len4; _key4++) {
        args[_key4 - 1] = arguments[_key4];
      }

      this.inputting = false;
      this.setState({
        focused: false
      });
      var value = this.getCurrentValidValue(this.inputValue);
      // todo
      // e.persist() // fix https://github.com/react-component/input-number/issues/51
      this.setValue(value, function () {
        _this4.$emit.apply(_this4, ['blur', e].concat((0, _toConsumableArray3['default'])(args)));
      });
    },
    getCurrentValidValue: function getCurrentValidValue(value) {
      var val = value;
      if (val === '') {
        val = '';
      } else if (!this.isNotCompleteNumber(parseFloat(val, 10))) {
        val = this.getValidValue(val);
      } else {
        val = this.sValue;
      }
      return this.toNumber(val);
    },
    getRatio: function getRatio(e) {
      var ratio = 1;
      if (e.metaKey || e.ctrlKey) {
        ratio = 0.1;
      } else if (e.shiftKey) {
        ratio = 10;
      }
      return ratio;
    },
    getValueFromEvent: function getValueFromEvent(e) {
      // optimize for chinese input expierence
      // https://github.com/ant-design/ant-design/issues/8196
      var value = e.target.value.trim().replace(/。/g, '.');

      if (this.decimalSeparator !== undefined) {
        value = value.replace(this.decimalSeparator, '.');
      }

      return value;
    },
    getValidValue: function getValidValue(value) {
      var min = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : this.min;
      var max = arguments.length > 2 && arguments[2] !== undefined ? arguments[2] : this.max;

      var val = parseFloat(value, 10);
      // https://github.com/ant-design/ant-design/issues/7358
      if (isNaN(val)) {
        return value;
      }
      if (val < min) {
        val = min;
      }
      if (val > max) {
        val = max;
      }
      return val;
    },
    setValue: function setValue(v, callback) {
      // trigger onChange
      var newValue = this.isNotCompleteNumber(parseFloat(v, 10)) ? undefined : parseFloat(v, 10);
      var changed = newValue !== this.sValue || '' + newValue !== '' + this.inputValue; // https://github.com/ant-design/ant-design/issues/7363
      if (!(0, _propsUtil.hasProp)(this, 'value')) {
        this.setState({
          sValue: newValue,
          inputValue: this.toPrecisionAsStep(v)
        }, callback);
      } else {
        // always set input value same as value
        this.setState({
          inputValue: this.toPrecisionAsStep(this.sValue)
        }, callback);
      }
      if (changed) {
        this.$emit('change', newValue);
      }
    },
    getPrecision: function getPrecision(value) {
      if ((0, _propsUtil.hasProp)(this, 'precision')) {
        return this.precision;
      }
      var valueString = value.toString();
      if (valueString.indexOf('e-') >= 0) {
        return parseInt(valueString.slice(valueString.indexOf('e-') + 2), 10);
      }
      var precision = 0;
      if (valueString.indexOf('.') >= 0) {
        precision = valueString.length - valueString.indexOf('.') - 1;
      }
      return precision;
    },

    // step={1.0} value={1.51}
    // press +
    // then value should be 2.51, rather than 2.5
    // if this.props.precision is undefined
    // https://github.com/react-component/input-number/issues/39
    getMaxPrecision: function getMaxPrecision(currentValue) {
      var ratio = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : 1;

      if ((0, _propsUtil.hasProp)(this, 'precision')) {
        return this.precision;
      }
      var step = this.step;

      var ratioPrecision = this.getPrecision(ratio);
      var stepPrecision = this.getPrecision(step);
      var currentValuePrecision = this.getPrecision(currentValue);
      if (!currentValue) {
        return ratioPrecision + stepPrecision;
      }
      return Math.max(currentValuePrecision, ratioPrecision + stepPrecision);
    },
    getPrecisionFactor: function getPrecisionFactor(currentValue) {
      var ratio = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : 1;

      var precision = this.getMaxPrecision(currentValue, ratio);
      return Math.pow(10, precision);
    },
    getInputDisplayValue: function getInputDisplayValue() {
      var focused = this.focused,
          inputValue = this.inputValue,
          sValue = this.sValue;

      var inputDisplayValue = void 0;
      if (focused) {
        inputDisplayValue = inputValue;
      } else {
        inputDisplayValue = this.toPrecisionAsStep(sValue);
      }

      if (inputDisplayValue === undefined || inputDisplayValue === null) {
        inputDisplayValue = '';
      }

      return inputDisplayValue;
    },
    recordCursorPosition: function recordCursorPosition() {
      // Record position
      try {
        var inputElem = this.$refs.inputRef;
        this.cursorStart = inputElem.selectionStart;
        this.cursorEnd = inputElem.selectionEnd;
        this.currentValue = inputElem.value;
        this.cursorBefore = inputElem.value.substring(0, this.cursorStart);
        this.cursorAfter = inputElem.value.substring(this.cursorEnd);
      } catch (e) {
        // Fix error in Chrome:
        // Failed to read the 'selectionStart' property from 'HTMLInputElement'
        // http://stackoverflow.com/q/21177489/3040605
      }
    },
    fixCaret: function fixCaret(start, end) {
      if (start === undefined || end === undefined || !this.input || !this.input.value) {
        return;
      }

      try {
        var inputElem = this.$refs.inputRef;
        var currentStart = inputElem.selectionStart;
        var currentEnd = inputElem.selectionEnd;

        if (start !== currentStart || end !== currentEnd) {
          inputElem.setSelectionRange(start, end);
        }
      } catch (e) {
        // Fix error in Chrome:
        // Failed to read the 'selectionStart' property from 'HTMLInputElement'
        // http://stackoverflow.com/q/21177489/3040605
      }
    },
    restoreByAfter: function restoreByAfter(str) {
      if (str === undefined) return false;

      var fullStr = this.$refs.inputRef.value;
      var index = fullStr.lastIndexOf(str);

      if (index === -1) return false;

      if (index + str.length === fullStr.length) {
        this.fixCaret(index, index);

        return true;
      }
      return false;
    },
    partRestoreByAfter: function partRestoreByAfter(str) {
      var _this5 = this;

      if (str === undefined) return false;

      // For loop from full str to the str with last char to map. e.g. 123
      // -> 123
      // -> 23
      // -> 3
      return Array.prototype.some.call(str, function (_, start) {
        var partStr = str.substring(start);

        return _this5.restoreByAfter(partStr);
      });
    },
    focus: function focus() {
      this.$refs.inputRef.focus();
      this.recordCursorPosition();
    },
    blur: function blur() {
      this.$refs.inputRef.blur();
    },
    formatWrapper: function formatWrapper(num) {
      // http://2ality.com/2012/03/signedzero.html
      // https://github.com/ant-design/ant-design/issues/9439
      if ((0, _isNegativeZero2['default'])(num)) {
        return '-0';
      }
      if (this.formatter) {
        return this.formatter(num);
      }
      return num;
    },
    toPrecisionAsStep: function toPrecisionAsStep(num) {
      if (this.isNotCompleteNumber(num) || num === '') {
        return num;
      }
      var precision = Math.abs(this.getMaxPrecision(num));
      if (precision === 0) {
        return num.toString();
      }
      if (!isNaN(precision)) {
        return Number(num).toFixed(precision);
      }
      return num.toString();
    },

    // '1.' '1x' 'xx' '' => are not complete numbers
    isNotCompleteNumber: function isNotCompleteNumber(num) {
      return isNaN(num) || num === '' || num === null || num && num.toString().indexOf('.') === num.toString().length - 1;
    },
    toNumber: function toNumber(num) {
      if (this.isNotCompleteNumber(num)) {
        return num;
      }
      if ((0, _propsUtil.hasProp)(this, 'precision')) {
        return Number(Number(num).toFixed(this.precision));
      }
      return Number(num);
    },

    // '1.0' '1.00'  => may be a inputing number
    toNumberWhenUserInput: function toNumberWhenUserInput(num) {
      // num.length > 16 => prevent input large number will became Infinity
      if ((/\.\d*0$/.test(num) || num.length > 16) && this.focused) {
        return num;
      }
      return this.toNumber(num);
    },
    upStep: function upStep(val, rat) {
      var step = this.step,
          min = this.min;

      var precisionFactor = this.getPrecisionFactor(val, rat);
      var precision = Math.abs(this.getMaxPrecision(val, rat));
      var result = void 0;
      if (typeof val === 'number') {
        result = ((precisionFactor * val + precisionFactor * step * rat) / precisionFactor).toFixed(precision);
      } else {
        result = min === -Infinity ? step : min;
      }
      return this.toNumber(result);
    },
    downStep: function downStep(val, rat) {
      var step = this.step,
          min = this.min;

      var precisionFactor = this.getPrecisionFactor(val, rat);
      var precision = Math.abs(this.getMaxPrecision(val, rat));
      var result = void 0;
      if (typeof val === 'number') {
        result = ((precisionFactor * val - precisionFactor * step * rat) / precisionFactor).toFixed(precision);
      } else {
        result = min === -Infinity ? -step : min;
      }
      return this.toNumber(result);
    },
    stepFn: function stepFn(type, e) {
      var _this6 = this;

      var ratio = arguments.length > 2 && arguments[2] !== undefined ? arguments[2] : 1;
      var recursive = arguments[3];

      this.stop();
      if (e) {
        // e.persist()
        e.preventDefault();
      }
      if (this.disabled) {
        return;
      }
      var max = this.max,
          min = this.min;

      var value = this.getCurrentValidValue(this.inputValue) || 0;
      if (this.isNotCompleteNumber(value)) {
        return;
      }
      var val = this[type + 'Step'](value, ratio);
      var outOfRange = val > max || val < min;
      if (val > max) {
        val = max;
      } else if (val < min) {
        val = min;
      }
      this.setValue(val);
      this.setState({
        focused: true
      });
      if (outOfRange) {
        return;
      }
      this.autoStepTimer = setTimeout(function () {
        _this6[type](e, ratio, true);
      }, recursive ? SPEED : DELAY);
    },
    stop: function stop() {
      if (this.autoStepTimer) {
        clearTimeout(this.autoStepTimer);
      }
    },
    down: function down(e, ratio, recursive) {
      this.pressingUpOrDown = true;
      this.stepFn('down', e, ratio, recursive);
    },
    up: function up(e, ratio, recursive) {
      this.pressingUpOrDown = true;
      this.stepFn('up', e, ratio, recursive);
    },
    handleInputClick: function handleInputClick() {
      this.$emit('click');
    }
  },
  render: function render() {
    var _classNames;

    var h = arguments[0];
    var _$props = this.$props,
        prefixCls = _$props.prefixCls,
        disabled = _$props.disabled,
        readOnly = _$props.readOnly,
        useTouch = _$props.useTouch,
        autoComplete = _$props.autoComplete,
        upHandler = _$props.upHandler,
        downHandler = _$props.downHandler;

    var classes = (0, _classnames2['default'])((_classNames = {}, (0, _defineProperty3['default'])(_classNames, prefixCls, true), (0, _defineProperty3['default'])(_classNames, prefixCls + '-disabled', disabled), (0, _defineProperty3['default'])(_classNames, prefixCls + '-focused', this.focused), _classNames));
    var upDisabledClass = '';
    var downDisabledClass = '';
    var sValue = this.sValue;

    if (sValue || sValue === 0) {
      if (!isNaN(sValue)) {
        var val = Number(sValue);
        if (val >= this.max) {
          upDisabledClass = prefixCls + '-handler-up-disabled';
        }
        if (val <= this.min) {
          downDisabledClass = prefixCls + '-handler-down-disabled';
        }
      } else {
        upDisabledClass = prefixCls + '-handler-up-disabled';
        downDisabledClass = prefixCls + '-handler-down-disabled';
      }
    }

    var editable = !this.readOnly && !this.disabled;

    // focus state, show input value
    // unfocus state, show valid value
    var inputDisplayValue = void 0;
    if (this.focused) {
      inputDisplayValue = this.inputValue;
    } else {
      inputDisplayValue = this.toPrecisionAsStep(this.sValue);
    }

    if (inputDisplayValue === undefined || inputDisplayValue === null) {
      inputDisplayValue = '';
    }

    var upEvents = void 0;
    var downEvents = void 0;
    if (useTouch) {
      upEvents = {
        touchstart: editable && !upDisabledClass ? this.up : noop,
        touchend: this.stop
      };
      downEvents = {
        touchstart: editable && !downDisabledClass ? this.down : noop,
        touchend: this.stop
      };
    } else {
      upEvents = {
        mousedown: editable && !upDisabledClass ? this.up : noop,
        mouseup: this.stop,
        mouseleave: this.stop
      };
      downEvents = {
        mousedown: editable && !downDisabledClass ? this.down : noop,
        mouseup: this.stop,
        mouseleave: this.stop
      };
    }
    var inputDisplayValueFormat = this.formatWrapper(inputDisplayValue);
    if (this.decimalSeparator !== undefined) {
      inputDisplayValueFormat = inputDisplayValueFormat.toString().replace('.', this.decimalSeparator);
    }
    var isUpDisabled = !!upDisabledClass || disabled || readOnly;
    var isDownDisabled = !!downDisabledClass || disabled || readOnly;
    var _$listeners = this.$listeners,
        _$listeners$mouseente = _$listeners.mouseenter,
        mouseenter = _$listeners$mouseente === undefined ? noop : _$listeners$mouseente,
        _$listeners$mouseleav = _$listeners.mouseleave,
        mouseleave = _$listeners$mouseleav === undefined ? noop : _$listeners$mouseleav,
        _$listeners$mouseover = _$listeners.mouseover,
        mouseover = _$listeners$mouseover === undefined ? noop : _$listeners$mouseover,
        _$listeners$mouseout = _$listeners.mouseout,
        mouseout = _$listeners$mouseout === undefined ? noop : _$listeners$mouseout;

    var contentProps = {
      on: { mouseenter: mouseenter, mouseleave: mouseleave, mouseover: mouseover, mouseout: mouseout },
      'class': classes,
      attrs: { title: this.$props.title }
    };
    var upHandlerProps = {
      props: {
        disabled: isUpDisabled,
        prefixCls: prefixCls
      },
      attrs: {
        unselectable: 'unselectable',
        role: 'button',
        'aria-label': 'Increase Value',
        'aria-disabled': !!isUpDisabled
      },
      'class': prefixCls + '-handler ' + prefixCls + '-handler-up ' + upDisabledClass,
      on: upEvents,
      ref: 'up'
    };
    var downHandlerProps = {
      props: {
        disabled: isDownDisabled,
        prefixCls: prefixCls
      },
      attrs: {
        unselectable: 'unselectable',
        role: 'button',
        'aria-label': 'Decrease Value',
        'aria-disabled': !!isDownDisabled
      },
      'class': prefixCls + '-handler ' + prefixCls + '-handler-down ' + downDisabledClass,
      on: downEvents,
      ref: 'down'
    };
    // ref for test
    return h(
      'div',
      contentProps,
      [h(
        'div',
        { 'class': prefixCls + '-handler-wrap' },
        [h(
          _InputHandler2['default'],
          upHandlerProps,
          [upHandler || h('span', {
            attrs: {
              unselectable: 'unselectable'
            },
            'class': prefixCls + '-handler-up-inner',
            on: {
              'click': preventDefault
            }
          })]
        ), h(
          _InputHandler2['default'],
          downHandlerProps,
          [downHandler || h('span', {
            attrs: {
              unselectable: 'unselectable'
            },
            'class': prefixCls + '-handler-down-inner',
            on: {
              'click': preventDefault
            }
          })]
        )]
      ), h(
        'div',
        {
          'class': prefixCls + '-input-wrap',
          attrs: { role: 'spinbutton',
            'aria-valuemin': this.min,
            'aria-valuemax': this.max,
            'aria-valuenow': sValue
          }
        },
        [h('input', {
          attrs: {
            required: this.required,
            type: this.type,
            placeholder: this.placeholder,

            tabIndex: this.tabIndex,
            autoComplete: autoComplete,

            maxLength: this.maxLength,
            readOnly: this.readOnly,
            disabled: this.disabled,
            max: this.max,
            min: this.min,
            step: this.step,
            name: this.name,
            id: this.id,

            pattern: this.pattern
          },
          on: {
            'click': this.handleInputClick,
            'focus': this.onFocus,
            'blur': this.onBlur,
            'keydown': editable ? this.onKeyDown : noop,
            'keyup': editable ? this.onKeyUp : noop,
            'input': this.onChange
          },

          'class': prefixCls + '-input',
          ref: 'inputRef',
          domProps: {
            'value': inputDisplayValueFormat
          }
        })]
      )]
    );
  }
};