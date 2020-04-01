'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _babelHelperVueJsxMergeProps = require('babel-helper-vue-jsx-merge-props');

var _babelHelperVueJsxMergeProps2 = _interopRequireDefault(_babelHelperVueJsxMergeProps);

var _defineProperty2 = require('babel-runtime/helpers/defineProperty');

var _defineProperty3 = _interopRequireDefault(_defineProperty2);

var _toConsumableArray2 = require('babel-runtime/helpers/toConsumableArray');

var _toConsumableArray3 = _interopRequireDefault(_toConsumableArray2);

var _slicedToArray2 = require('babel-runtime/helpers/slicedToArray');

var _slicedToArray3 = _interopRequireDefault(_slicedToArray2);

var _vueTypes = require('../../_util/vue-types');

var _vueTypes2 = _interopRequireDefault(_vueTypes);

var _BaseMixin = require('../../_util/BaseMixin');

var _BaseMixin2 = _interopRequireDefault(_BaseMixin);

var _propsUtil = require('../../_util/props-util');

var _moment = require('moment');

var _moment2 = _interopRequireDefault(_moment);

var _KeyCode = require('../../_util/KeyCode');

var _KeyCode2 = _interopRequireDefault(_KeyCode);

var _CalendarPart = require('./range-calendar/CalendarPart');

var _CalendarPart2 = _interopRequireDefault(_CalendarPart);

var _TodayButton = require('./calendar/TodayButton');

var _TodayButton2 = _interopRequireDefault(_TodayButton);

var _OkButton = require('./calendar/OkButton');

var _OkButton2 = _interopRequireDefault(_OkButton);

var _TimePickerButton = require('./calendar/TimePickerButton');

var _TimePickerButton2 = _interopRequireDefault(_TimePickerButton);

var _CommonMixin = require('./mixin/CommonMixin');

var _CommonMixin2 = _interopRequireDefault(_CommonMixin);

var _en_US = require('./locale/en_US');

var _en_US2 = _interopRequireDefault(_en_US);

var _util = require('./util/');

var _toTime = require('./util/toTime');

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

function noop() {}

function isEmptyArray(arr) {
  return Array.isArray(arr) && (arr.length === 0 || arr.every(function (i) {
    return !i;
  }));
}

function isArraysEqual(a, b) {
  if (a === b) return true;
  if (a === null || typeof a === 'undefined' || b === null || typeof b === 'undefined') {
    return false;
  }
  if (a.length !== b.length) return false;

  for (var i = 0; i < a.length; ++i) {
    if (a[i] !== b[i]) return false;
  }
  return true;
}

function getValueFromSelectedValue(selectedValue) {
  var _selectedValue = (0, _slicedToArray3['default'])(selectedValue, 2),
      start = _selectedValue[0],
      end = _selectedValue[1];

  if (end && (start === undefined || start === null)) {
    start = end.clone().subtract(1, 'month');
  }

  if (start && (end === undefined || end === null)) {
    end = start.clone().add(1, 'month');
  }
  return [start, end];
}

function normalizeAnchor(props, init) {
  var selectedValue = props.selectedValue || init && props.defaultSelectedValue;
  var value = props.value || init && props.defaultValue;
  var normalizedValue = value ? getValueFromSelectedValue(value) : getValueFromSelectedValue(selectedValue);
  return !isEmptyArray(normalizedValue) ? normalizedValue : init && [(0, _moment2['default'])(), (0, _moment2['default'])().add(1, 'months')];
}

function generateOptions(length, extraOptionGen) {
  var arr = extraOptionGen ? extraOptionGen().concat() : [];
  for (var value = 0; value < length; value++) {
    if (arr.indexOf(value) === -1) {
      arr.push(value);
    }
  }
  return arr;
}

function onInputSelect(direction, value, cause) {
  if (!value) {
    return;
  }
  var originalValue = this.sSelectedValue;
  var selectedValue = originalValue.concat();
  var index = direction === 'left' ? 0 : 1;
  selectedValue[index] = value;
  if (selectedValue[0] && this.compare(selectedValue[0], selectedValue[1]) > 0) {
    selectedValue[1 - index] = this.sShowTimePicker ? selectedValue[index] : undefined;
  }
  this.__emit('inputSelect', selectedValue);
  this.fireSelectValueChange(selectedValue, null, cause || { source: 'dateInput' });
}

var RangeCalendar = {
  props: {
    locale: _vueTypes2['default'].object.def(_en_US2['default']),
    visible: _vueTypes2['default'].bool.def(true),
    prefixCls: _vueTypes2['default'].string.def('rc-calendar'),
    dateInputPlaceholder: _vueTypes2['default'].any,
    seperator: _vueTypes2['default'].string.def('~'),
    defaultValue: _vueTypes2['default'].any,
    value: _vueTypes2['default'].any,
    hoverValue: _vueTypes2['default'].any,
    mode: _vueTypes2['default'].arrayOf(_vueTypes2['default'].oneOf(['time', 'date', 'month', 'year', 'decade'])),
    showDateInput: _vueTypes2['default'].bool.def(true),
    timePicker: _vueTypes2['default'].any,
    showOk: _vueTypes2['default'].bool,
    showToday: _vueTypes2['default'].bool.def(true),
    defaultSelectedValue: _vueTypes2['default'].array.def([]),
    selectedValue: _vueTypes2['default'].array,
    showClear: _vueTypes2['default'].bool,
    showWeekNumber: _vueTypes2['default'].bool,
    // locale: PropTypes.object,
    // onChange: PropTypes.func,
    // onSelect: PropTypes.func,
    // onValueChange: PropTypes.func,
    // onHoverChange: PropTypes.func,
    // onPanelChange: PropTypes.func,
    format: _vueTypes2['default'].oneOfType([_vueTypes2['default'].string, _vueTypes2['default'].arrayOf(_vueTypes2['default'].string)]),
    // onClear: PropTypes.func,
    type: _vueTypes2['default'].any.def('both'),
    disabledDate: _vueTypes2['default'].func,
    disabledTime: _vueTypes2['default'].func.def(noop),
    renderFooter: _vueTypes2['default'].func.def(function () {
      return null;
    }),
    renderSidebar: _vueTypes2['default'].func.def(function () {
      return null;
    }),
    dateRender: _vueTypes2['default'].func,
    clearIcon: _vueTypes2['default'].any
  },

  mixins: [_BaseMixin2['default'], _CommonMixin2['default']],

  data: function data() {
    var props = this.$props;
    var selectedValue = props.selectedValue || props.defaultSelectedValue;
    var value = normalizeAnchor(props, 1);
    return {
      sSelectedValue: selectedValue,
      prevSelectedValue: selectedValue,
      firstSelectedValue: null,
      sHoverValue: props.hoverValue || [],
      sValue: value,
      sShowTimePicker: false,
      sMode: props.mode || ['date', 'date'],
      sPanelTriggerSource: '' // Trigger by which picker panel: 'start' & 'end'
    };
  },

  watch: {
    value: function value() {
      var newState = {};
      newState.sValue = normalizeAnchor(this.$props, 0);
      this.setState(newState);
    },
    hoverValue: function hoverValue(val) {
      if (!isArraysEqual(this.sHoverValue, val)) {
        this.setState({ sHoverValue: val });
      }
    },
    selectedValue: function selectedValue(val) {
      var newState = {};
      newState.sSelectedValue = val;
      newState.prevSelectedValue = val;
      this.setState(newState);
    },
    mode: function mode(val) {
      if (!isArraysEqual(this.sMode, val)) {
        this.setState({ sMode: val });
      }
    }
  },

  methods: {
    onDatePanelEnter: function onDatePanelEnter() {
      if (this.hasSelectedValue()) {
        this.fireHoverValueChange(this.sSelectedValue.concat());
      }
    },
    onDatePanelLeave: function onDatePanelLeave() {
      if (this.hasSelectedValue()) {
        this.fireHoverValueChange([]);
      }
    },
    onSelect: function onSelect(value) {
      var type = this.type,
          sSelectedValue = this.sSelectedValue,
          prevSelectedValue = this.prevSelectedValue,
          firstSelectedValue = this.firstSelectedValue;

      var nextSelectedValue = void 0;
      if (type === 'both') {
        if (!firstSelectedValue) {
          (0, _util.syncTime)(prevSelectedValue[0], value);
          nextSelectedValue = [value];
        } else if (this.compare(firstSelectedValue, value) < 0) {
          (0, _util.syncTime)(prevSelectedValue[1], value);
          nextSelectedValue = [firstSelectedValue, value];
        } else {
          (0, _util.syncTime)(prevSelectedValue[0], value);
          (0, _util.syncTime)(prevSelectedValue[1], firstSelectedValue);
          nextSelectedValue = [value, firstSelectedValue];
        }
      } else if (type === 'start') {
        (0, _util.syncTime)(prevSelectedValue[0], value);
        var endValue = sSelectedValue[1];
        nextSelectedValue = endValue && this.compare(endValue, value) > 0 ? [value, endValue] : [value];
      } else {
        // type === 'end'
        var startValue = sSelectedValue[0];
        if (startValue && this.compare(startValue, value) <= 0) {
          (0, _util.syncTime)(prevSelectedValue[1], value);
          nextSelectedValue = [startValue, value];
        } else {
          (0, _util.syncTime)(prevSelectedValue[0], value);
          nextSelectedValue = [value];
        }
      }

      this.fireSelectValueChange(nextSelectedValue);
    },
    onKeyDown: function onKeyDown(event) {
      var _this = this;

      if (event.target.nodeName.toLowerCase() === 'input') {
        return;
      }

      var keyCode = event.keyCode;

      var ctrlKey = event.ctrlKey || event.metaKey;

      var _$data = this.$data,
          selectedValue = _$data.sSelectedValue,
          hoverValue = _$data.sHoverValue,
          firstSelectedValue = _$data.firstSelectedValue,
          value = _$data.sValue;
      var disabledDate = this.$props.disabledDate;

      // Update last time of the picker

      var updateHoverPoint = function updateHoverPoint(func) {
        // Change hover to make focus in UI
        var currentHoverTime = void 0;
        var nextHoverTime = void 0;
        var nextHoverValue = void 0;

        if (!firstSelectedValue) {
          currentHoverTime = hoverValue[0] || selectedValue[0] || value[0] || (0, _moment2['default'])();
          nextHoverTime = func(currentHoverTime);
          nextHoverValue = [nextHoverTime];
          _this.fireHoverValueChange(nextHoverValue);
        } else {
          if (hoverValue.length === 1) {
            currentHoverTime = hoverValue[0].clone();
            nextHoverTime = func(currentHoverTime);
            nextHoverValue = _this.onDayHover(nextHoverTime);
          } else {
            currentHoverTime = hoverValue[0].isSame(firstSelectedValue, 'day') ? hoverValue[1] : hoverValue[0];
            nextHoverTime = func(currentHoverTime);
            nextHoverValue = _this.onDayHover(nextHoverTime);
          }
        }

        // Find origin hover time on value index
        if (nextHoverValue.length >= 2) {
          var miss = nextHoverValue.some(function (ht) {
            return !(0, _toTime.includesTime)(value, ht, 'month');
          });
          if (miss) {
            var newValue = nextHoverValue.slice().sort(function (t1, t2) {
              return t1.valueOf() - t2.valueOf();
            });
            if (newValue[0].isSame(newValue[1], 'month')) {
              newValue[1] = newValue[0].clone().add(1, 'month');
            }
            _this.fireValueChange(newValue);
          }
        } else if (nextHoverValue.length === 1) {
          // If only one value, let's keep the origin panel
          var oriValueIndex = value.findIndex(function (time) {
            return time.isSame(currentHoverTime, 'month');
          });
          if (oriValueIndex === -1) oriValueIndex = 0;

          if (value.every(function (time) {
            return !time.isSame(nextHoverTime, 'month');
          })) {
            var _newValue = value.slice();
            _newValue[oriValueIndex] = nextHoverTime.clone();
            _this.fireValueChange(_newValue);
          }
        }

        event.preventDefault();

        return nextHoverTime;
      };

      switch (keyCode) {
        case _KeyCode2['default'].DOWN:
          updateHoverPoint(function (time) {
            return (0, _toTime.goTime)(time, 1, 'weeks');
          });
          return;
        case _KeyCode2['default'].UP:
          updateHoverPoint(function (time) {
            return (0, _toTime.goTime)(time, -1, 'weeks');
          });
          return;
        case _KeyCode2['default'].LEFT:
          if (ctrlKey) {
            updateHoverPoint(function (time) {
              return (0, _toTime.goTime)(time, -1, 'years');
            });
          } else {
            updateHoverPoint(function (time) {
              return (0, _toTime.goTime)(time, -1, 'days');
            });
          }
          return;
        case _KeyCode2['default'].RIGHT:
          if (ctrlKey) {
            updateHoverPoint(function (time) {
              return (0, _toTime.goTime)(time, 1, 'years');
            });
          } else {
            updateHoverPoint(function (time) {
              return (0, _toTime.goTime)(time, 1, 'days');
            });
          }
          return;
        case _KeyCode2['default'].HOME:
          updateHoverPoint(function (time) {
            return (0, _toTime.goStartMonth)(time);
          });
          return;
        case _KeyCode2['default'].END:
          updateHoverPoint(function (time) {
            return (0, _toTime.goEndMonth)(time);
          });
          return;
        case _KeyCode2['default'].PAGE_DOWN:
          updateHoverPoint(function (time) {
            return (0, _toTime.goTime)(time, 1, 'month');
          });
          return;
        case _KeyCode2['default'].PAGE_UP:
          updateHoverPoint(function (time) {
            return (0, _toTime.goTime)(time, -1, 'month');
          });
          return;
        case _KeyCode2['default'].ENTER:
          {
            var lastValue = void 0;
            if (hoverValue.length === 0) {
              lastValue = updateHoverPoint(function (time) {
                return time;
              });
            } else if (hoverValue.length === 1) {
              lastValue = hoverValue[0];
            } else {
              lastValue = hoverValue[0].isSame(firstSelectedValue, 'day') ? hoverValue[1] : hoverValue[0];
            }
            if (lastValue && (!disabledDate || !disabledDate(lastValue))) {
              this.onSelect(lastValue);
            }
            event.preventDefault();
            return;
          }
        default:
          this.__emit('keydown', event);
      }
    },
    onDayHover: function onDayHover(value) {
      var hoverValue = [];
      var sSelectedValue = this.sSelectedValue,
          firstSelectedValue = this.firstSelectedValue,
          type = this.type;

      if (type === 'start' && sSelectedValue[1]) {
        hoverValue = this.compare(value, sSelectedValue[1]) < 0 ? [value, sSelectedValue[1]] : [value];
      } else if (type === 'end' && sSelectedValue[0]) {
        hoverValue = this.compare(value, sSelectedValue[0]) > 0 ? [sSelectedValue[0], value] : [];
      } else {
        if (!firstSelectedValue) {
          if (this.sHoverValue.length) {
            this.setState({ sHoverValue: [] });
          }
          return hoverValue;
        }
        hoverValue = this.compare(value, firstSelectedValue) < 0 ? [value, firstSelectedValue] : [firstSelectedValue, value];
      }
      this.fireHoverValueChange(hoverValue);
      return hoverValue;
    },
    onToday: function onToday() {
      var startValue = (0, _util.getTodayTime)(this.sValue[0]);
      var endValue = startValue.clone().add(1, 'months');
      this.setState({ sValue: [startValue, endValue] });
    },
    onOpenTimePicker: function onOpenTimePicker() {
      this.setState({
        sShowTimePicker: true
      });
    },
    onCloseTimePicker: function onCloseTimePicker() {
      this.setState({
        sShowTimePicker: false
      });
    },
    onOk: function onOk() {
      var sSelectedValue = this.sSelectedValue;

      if (this.isAllowedDateAndTime(sSelectedValue)) {
        this.__emit('ok', sSelectedValue);
      }
    },
    onStartInputChange: function onStartInputChange() {
      for (var _len = arguments.length, oargs = Array(_len), _key = 0; _key < _len; _key++) {
        oargs[_key] = arguments[_key];
      }

      var args = ['left'].concat(oargs);
      return onInputSelect.apply(this, args);
    },
    onEndInputChange: function onEndInputChange() {
      for (var _len2 = arguments.length, oargs = Array(_len2), _key2 = 0; _key2 < _len2; _key2++) {
        oargs[_key2] = arguments[_key2];
      }

      var args = ['right'].concat(oargs);
      return onInputSelect.apply(this, args);
    },
    onStartInputSelect: function onStartInputSelect(value) {
      var args = ['left', value, { source: 'dateInputSelect' }];
      return onInputSelect.apply(this, args);
    },
    onEndInputSelect: function onEndInputSelect(value) {
      var args = ['right', value, { source: 'dateInputSelect' }];
      return onInputSelect.apply(this, args);
    },
    onStartValueChange: function onStartValueChange(leftValue) {
      var value = [].concat((0, _toConsumableArray3['default'])(this.sValue));
      value[0] = leftValue;
      return this.fireValueChange(value);
    },
    onEndValueChange: function onEndValueChange(rightValue) {
      var value = [].concat((0, _toConsumableArray3['default'])(this.sValue));
      value[1] = rightValue;
      return this.fireValueChange(value);
    },
    onStartPanelChange: function onStartPanelChange(value, mode) {
      var sMode = this.sMode,
          sValue = this.sValue;

      var newMode = [mode, sMode[1]];
      var newValue = [value || sValue[0], sValue[1]];
      this.__emit('panelChange', newValue, newMode);
      var newState = {
        sPanelTriggerSource: 'start'
      };
      if (!(0, _propsUtil.hasProp)(this, 'mode')) {
        newState.sMode = newMode;
      }
      this.setState(newState);
    },
    onEndPanelChange: function onEndPanelChange(value, mode) {
      var sMode = this.sMode,
          sValue = this.sValue;

      var newMode = [sMode[0], mode];
      var newValue = [sValue[0], value || sValue[1]];
      this.__emit('panelChange', newValue, newMode);
      var newState = {
        sPanelTriggerSource: 'start'
      };
      if (!(0, _propsUtil.hasProp)(this, 'mode')) {
        newState.sMode = newMode;
      }
      this.setState(newState);
    },
    getStartValue: function getStartValue() {
      var _$data2 = this.$data,
          selectedValue = _$data2.sSelectedValue,
          showTimePicker = _$data2.sShowTimePicker,
          value = _$data2.sValue,
          mode = _$data2.sMode,
          panelTriggerSource = _$data2.sPanelTriggerSource;

      var startValue = value[0];
      // keep selectedTime when select date
      if (selectedValue[0] && this.$props.timePicker) {
        startValue = startValue.clone();
        (0, _util.syncTime)(selectedValue[0], startValue);
      }
      if (showTimePicker && selectedValue[0]) {
        startValue = selectedValue[0];
      }

      // Adjust month if date not align
      if (panelTriggerSource === 'end' && mode[0] === 'date' && mode[1] === 'date' && startValue.isSame(value[1], 'month')) {
        startValue = startValue.clone().subtract(1, 'month');
      }

      return startValue;
    },
    getEndValue: function getEndValue() {
      var _$data3 = this.$data,
          selectedValue = _$data3.sSelectedValue,
          showTimePicker = _$data3.sShowTimePicker,
          value = _$data3.sValue,
          mode = _$data3.sMode,
          panelTriggerSource = _$data3.sPanelTriggerSource;

      var endValue = value[1] ? value[1].clone() : value[0].clone().add(1, 'month');
      // keep selectedTime when select date
      if (selectedValue[1] && this.$props.timePicker) {
        (0, _util.syncTime)(selectedValue[1], endValue);
      }
      if (showTimePicker) {
        endValue = selectedValue[1] ? selectedValue[1] : this.getStartValue();
      }

      // Adjust month if date not align
      if (!showTimePicker && panelTriggerSource !== 'end' && mode[0] === 'date' && mode[1] === 'date' && endValue.isSame(value[0], 'month')) {
        endValue = endValue.clone().add(1, 'month');
      }

      return endValue;
    },

    // get disabled hours for second picker
    getEndDisableTime: function getEndDisableTime() {
      var sSelectedValue = this.sSelectedValue,
          sValue = this.sValue,
          disabledTime = this.disabledTime;

      var userSettingDisabledTime = disabledTime(sSelectedValue, 'end') || {};
      var startValue = sSelectedValue && sSelectedValue[0] || sValue[0].clone();
      // if startTime and endTime is same day..
      // the second time picker will not able to pick time before first time picker
      if (!sSelectedValue[1] || startValue.isSame(sSelectedValue[1], 'day')) {
        var hours = startValue.hour();
        var minutes = startValue.minute();
        var second = startValue.second();
        var _disabledHours = userSettingDisabledTime.disabledHours,
            _disabledMinutes = userSettingDisabledTime.disabledMinutes,
            _disabledSeconds = userSettingDisabledTime.disabledSeconds;

        var oldDisabledMinutes = _disabledMinutes ? _disabledMinutes() : [];
        var olddisabledSeconds = _disabledSeconds ? _disabledSeconds() : [];
        _disabledHours = generateOptions(hours, _disabledHours);
        _disabledMinutes = generateOptions(minutes, _disabledMinutes);
        _disabledSeconds = generateOptions(second, _disabledSeconds);
        return {
          disabledHours: function disabledHours() {
            return _disabledHours;
          },
          disabledMinutes: function disabledMinutes(hour) {
            if (hour === hours) {
              return _disabledMinutes;
            }
            return oldDisabledMinutes;
          },
          disabledSeconds: function disabledSeconds(hour, minute) {
            if (hour === hours && minute === minutes) {
              return _disabledSeconds;
            }
            return olddisabledSeconds;
          }
        };
      }
      return userSettingDisabledTime;
    },
    isAllowedDateAndTime: function isAllowedDateAndTime(selectedValue) {
      return (0, _util.isAllowedDate)(selectedValue[0], this.disabledDate, this.disabledStartTime) && (0, _util.isAllowedDate)(selectedValue[1], this.disabledDate, this.disabledEndTime);
    },
    isMonthYearPanelShow: function isMonthYearPanelShow(mode) {
      return ['month', 'year', 'decade'].indexOf(mode) > -1;
    },
    hasSelectedValue: function hasSelectedValue() {
      var sSelectedValue = this.sSelectedValue;

      return !!sSelectedValue[1] && !!sSelectedValue[0];
    },
    compare: function compare(v1, v2) {
      if (this.timePicker) {
        return v1.diff(v2);
      }
      return v1.diff(v2, 'days');
    },
    fireSelectValueChange: function fireSelectValueChange(selectedValue, direct, cause) {
      var timePicker = this.timePicker,
          prevSelectedValue = this.prevSelectedValue;

      if (timePicker) {
        var timePickerProps = (0, _propsUtil.getOptionProps)(timePicker);
        if (timePickerProps.defaultValue) {
          var timePickerDefaultValue = timePickerProps.defaultValue;
          if (!prevSelectedValue[0] && selectedValue[0]) {
            (0, _util.syncTime)(timePickerDefaultValue[0], selectedValue[0]);
          }
          if (!prevSelectedValue[1] && selectedValue[1]) {
            (0, _util.syncTime)(timePickerDefaultValue[1], selectedValue[1]);
          }
        }
      }
      // 尚未选择过时间，直接输入的话
      if (!this.sSelectedValue[0] || !this.sSelectedValue[1]) {
        var startValue = selectedValue[0] || (0, _moment2['default'])();
        var endValue = selectedValue[1] || startValue.clone().add(1, 'months');
        this.setState({
          sSelectedValue: selectedValue,
          sValue: selectedValue && selectedValue.length === 2 ? getValueFromSelectedValue([startValue, endValue]) : this.sValue
        });
      }

      if (selectedValue[0] && !selectedValue[1]) {
        this.setState({ firstSelectedValue: selectedValue[0] });
        this.fireHoverValueChange(selectedValue.concat());
      }
      this.__emit('change', selectedValue);
      if (direct || selectedValue[0] && selectedValue[1]) {
        this.setState({
          prevSelectedValue: selectedValue,
          firstSelectedValue: null
        });
        this.fireHoverValueChange([]);
        this.__emit('select', selectedValue, cause);
      }
      if (!(0, _propsUtil.hasProp)(this, 'selectedValue')) {
        this.setState({
          sSelectedValue: selectedValue
        });
      }
    },
    fireValueChange: function fireValueChange(value) {
      if (!(0, _propsUtil.hasProp)(this, 'value')) {
        this.setState({
          sValue: value
        });
      }
      this.__emit('valueChange', value);
    },
    fireHoverValueChange: function fireHoverValueChange(hoverValue) {
      if (!(0, _propsUtil.hasProp)(this, 'hoverValue')) {
        this.setState({ sHoverValue: hoverValue });
      }
      this.__emit('hoverChange', hoverValue);
    },
    clear: function clear() {
      this.fireSelectValueChange([], true);
      this.__emit('clear');
    },
    disabledStartTime: function disabledStartTime(time) {
      return this.disabledTime(time, 'start');
    },
    disabledEndTime: function disabledEndTime(time) {
      return this.disabledTime(time, 'end');
    },
    disabledStartMonth: function disabledStartMonth(month) {
      var sValue = this.sValue;

      return month.isAfter(sValue[1], 'month');
    },
    disabledEndMonth: function disabledEndMonth(month) {
      var sValue = this.sValue;

      return month.isBefore(sValue[0], 'month');
    }
  },

  render: function render() {
    var _className, _cls;

    var h = arguments[0];

    var props = (0, _propsUtil.getOptionProps)(this);
    var prefixCls = props.prefixCls,
        dateInputPlaceholder = props.dateInputPlaceholder,
        timePicker = props.timePicker,
        showOk = props.showOk,
        locale = props.locale,
        showClear = props.showClear,
        showToday = props.showToday,
        type = props.type,
        seperator = props.seperator;

    var clearIcon = (0, _propsUtil.getComponentFromProp)(this, 'clearIcon');
    var sHoverValue = this.sHoverValue,
        sSelectedValue = this.sSelectedValue,
        mode = this.sMode,
        sShowTimePicker = this.sShowTimePicker,
        sValue = this.sValue;

    var className = (_className = {}, (0, _defineProperty3['default'])(_className, prefixCls, 1), (0, _defineProperty3['default'])(_className, prefixCls + '-hidden', !props.visible), (0, _defineProperty3['default'])(_className, prefixCls + '-range', 1), (0, _defineProperty3['default'])(_className, prefixCls + '-show-time-picker', sShowTimePicker), (0, _defineProperty3['default'])(_className, prefixCls + '-week-number', props.showWeekNumber), _className);
    var baseProps = {
      props: props,
      on: (0, _propsUtil.getListeners)(this)
    };
    var newProps = {
      props: {
        selectedValue: sSelectedValue
      },
      on: {
        select: this.onSelect,
        dayHover: type === 'start' && sSelectedValue[1] || type === 'end' && sSelectedValue[0] || !!sHoverValue.length ? this.onDayHover : noop
      }
    };

    var placeholder1 = void 0;
    var placeholder2 = void 0;

    if (dateInputPlaceholder) {
      if (Array.isArray(dateInputPlaceholder)) {
        var _dateInputPlaceholder = (0, _slicedToArray3['default'])(dateInputPlaceholder, 2);

        placeholder1 = _dateInputPlaceholder[0];
        placeholder2 = _dateInputPlaceholder[1];
      } else {
        placeholder1 = placeholder2 = dateInputPlaceholder;
      }
    }
    var showOkButton = showOk === true || showOk !== false && !!timePicker;
    var cls = (_cls = {}, (0, _defineProperty3['default'])(_cls, prefixCls + '-footer', true), (0, _defineProperty3['default'])(_cls, prefixCls + '-range-bottom', true), (0, _defineProperty3['default'])(_cls, prefixCls + '-footer-show-ok', showOkButton), _cls);

    var startValue = this.getStartValue();
    var endValue = this.getEndValue();
    var todayTime = (0, _util.getTodayTime)(startValue);
    var thisMonth = todayTime.month();
    var thisYear = todayTime.year();
    var isTodayInView = startValue.year() === thisYear && startValue.month() === thisMonth || endValue.year() === thisYear && endValue.month() === thisMonth;
    var nextMonthOfStart = startValue.clone().add(1, 'months');
    var isClosestMonths = nextMonthOfStart.year() === endValue.year() && nextMonthOfStart.month() === endValue.month();
    var leftPartProps = (0, _propsUtil.mergeProps)(baseProps, newProps, {
      props: {
        hoverValue: sHoverValue,
        direction: 'left',
        disabledTime: this.disabledStartTime,
        disabledMonth: this.disabledStartMonth,
        format: this.getFormat(),
        value: startValue,
        mode: mode[0],
        placeholder: placeholder1,
        showDateInput: this.showDateInput,
        timePicker: timePicker,
        showTimePicker: sShowTimePicker || mode[0] === 'time',
        enablePrev: true,
        enableNext: !isClosestMonths || this.isMonthYearPanelShow(mode[1]),
        clearIcon: clearIcon
      },
      on: {
        inputChange: this.onStartInputChange,
        inputSelect: this.onStartInputSelect,
        valueChange: this.onStartValueChange,
        panelChange: this.onStartPanelChange
      }
    });
    var rightPartProps = (0, _propsUtil.mergeProps)(baseProps, newProps, {
      props: {
        hoverValue: sHoverValue,
        direction: 'right',
        format: this.getFormat(),
        timePickerDisabledTime: this.getEndDisableTime(),
        placeholder: placeholder2,
        value: endValue,
        mode: mode[1],
        showDateInput: this.showDateInput,
        timePicker: timePicker,
        showTimePicker: sShowTimePicker || mode[1] === 'time',
        disabledTime: this.disabledEndTime,
        disabledMonth: this.disabledEndMonth,
        enablePrev: !isClosestMonths || this.isMonthYearPanelShow(mode[0]),
        enableNext: true,
        clearIcon: clearIcon
      },
      on: {
        inputChange: this.onEndInputChange,
        inputSelect: this.onEndInputSelect,
        valueChange: this.onEndValueChange,
        panelChange: this.onEndPanelChange
      }
    });
    var TodayButtonNode = null;
    if (showToday) {
      var todayButtonProps = (0, _propsUtil.mergeProps)(baseProps, {
        props: {
          disabled: isTodayInView,
          value: sValue[0],
          text: locale.backToToday
        },
        on: {
          today: this.onToday
        }
      });
      TodayButtonNode = h(_TodayButton2['default'], (0, _babelHelperVueJsxMergeProps2['default'])([{ key: 'todayButton' }, todayButtonProps]));
    }

    var TimePickerButtonNode = null;
    if (props.timePicker) {
      var timePickerButtonProps = (0, _propsUtil.mergeProps)(baseProps, {
        props: {
          showTimePicker: sShowTimePicker || mode[0] === 'time' && mode[1] === 'time',
          timePickerDisabled: !this.hasSelectedValue() || sHoverValue.length
        },
        on: {
          openTimePicker: this.onOpenTimePicker,
          closeTimePicker: this.onCloseTimePicker
        }
      });
      TimePickerButtonNode = h(_TimePickerButton2['default'], (0, _babelHelperVueJsxMergeProps2['default'])([{ key: 'timePickerButton' }, timePickerButtonProps]));
    }

    var OkButtonNode = null;
    if (showOkButton) {
      var okButtonProps = (0, _propsUtil.mergeProps)(baseProps, {
        props: {
          okDisabled: !this.isAllowedDateAndTime(sSelectedValue) || !this.hasSelectedValue() || sHoverValue.length
        },
        on: {
          ok: this.onOk
        }
      });
      OkButtonNode = h(_OkButton2['default'], (0, _babelHelperVueJsxMergeProps2['default'])([{ key: 'okButtonNode' }, okButtonProps]));
    }
    var extraFooter = this.renderFooter(mode);
    return h(
      'div',
      { ref: 'rootInstance', 'class': className, attrs: { tabIndex: '0' },
        on: {
          'keydown': this.onKeyDown
        }
      },
      [props.renderSidebar(), h(
        'div',
        { 'class': prefixCls + '-panel' },
        [showClear && sSelectedValue[0] && sSelectedValue[1] ? h(
          'a',
          {
            attrs: { role: 'button', title: locale.clear },
            on: {
              'click': this.clear
            }
          },
          [clearIcon || h('span', { 'class': prefixCls + '-clear-btn' })]
        ) : null, h(
          'div',
          {
            'class': prefixCls + '-date-panel',
            on: {
              'mouseleave': type !== 'both' ? this.onDatePanelLeave : noop,
              'mouseenter': type !== 'both' ? this.onDatePanelEnter : noop
            }
          },
          [h(_CalendarPart2['default'], leftPartProps), h(
            'span',
            { 'class': prefixCls + '-range-middle' },
            [seperator]
          ), h(_CalendarPart2['default'], rightPartProps)]
        ), h(
          'div',
          { 'class': cls },
          [showToday || props.timePicker || showOkButton || extraFooter ? h(
            'div',
            { 'class': prefixCls + '-footer-btn' },
            [extraFooter, TodayButtonNode, TimePickerButtonNode, OkButtonNode]
          ) : null]
        )]
      )]
    );
  }
};

exports['default'] = RangeCalendar;