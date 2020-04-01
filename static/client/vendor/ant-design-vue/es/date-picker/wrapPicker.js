import _defineProperty from 'babel-runtime/helpers/defineProperty';
import _extends from 'babel-runtime/helpers/extends';
import TimePickerPanel from '../vc-time-picker/Panel';
import classNames from 'classnames';
import * as moment from 'moment';
import LocaleReceiver from '../locale-provider/LocaleReceiver';
import { generateShowHourMinuteSecond } from '../time-picker';
import enUS from './locale/en_US';
import interopDefault from '../_util/interopDefault';
import { getOptionProps, initDefaultProps, getListeners } from '../_util/props-util';
import { ConfigConsumerProps } from '../config-provider';
import warning from '../_util/warning';

function checkValidate(value, propName) {
  var values = Array.isArray(value) ? value : [value];
  values.forEach(function (val) {
    if (!val) return;

    warning(!interopDefault(moment).isMoment(val) || val.isValid(), 'DatePicker', '`' + propName + '` provides invalidate moment time. If you want to set empty value, use `null` instead.');
  });
}

var DEFAULT_FORMAT = {
  date: 'YYYY-MM-DD',
  dateTime: 'YYYY-MM-DD HH:mm:ss',
  week: 'gggg-wo',
  month: 'YYYY-MM'
};

var LOCALE_FORMAT_MAPPING = {
  date: 'dateFormat',
  dateTime: 'dateTimeFormat',
  week: 'weekFormat',
  month: 'monthFormat'
};

function getColumns(_ref) {
  var showHour = _ref.showHour,
      showMinute = _ref.showMinute,
      showSecond = _ref.showSecond,
      use12Hours = _ref.use12Hours;

  var column = 0;
  if (showHour) {
    column += 1;
  }
  if (showMinute) {
    column += 1;
  }
  if (showSecond) {
    column += 1;
  }
  if (use12Hours) {
    column += 1;
  }
  return column;
}

export default function wrapPicker(Picker, props, pickerType) {
  return {
    name: Picker.name,
    props: initDefaultProps(props, {
      transitionName: 'slide-up',
      popupStyle: {},
      locale: {}
    }),
    model: {
      prop: 'value',
      event: 'change'
    },
    inject: {
      configProvider: { 'default': function _default() {
          return ConfigConsumerProps;
        } }
    },
    provide: function provide() {
      return {
        savePopupRef: this.savePopupRef
      };
    },
    mounted: function mounted() {
      var _this = this;

      var autoFocus = this.autoFocus,
          disabled = this.disabled,
          value = this.value,
          defaultValue = this.defaultValue;

      checkValidate(defaultValue, 'defaultValue');
      checkValidate(value, 'value');
      if (autoFocus && !disabled) {
        this.$nextTick(function () {
          _this.focus();
        });
      }
    },

    watch: {
      value: function value(val) {
        checkValidate(val, 'value');
      }
    },
    methods: {
      getDefaultLocale: function getDefaultLocale() {
        var result = _extends({}, enUS, this.locale);
        result.lang = _extends({}, result.lang, (this.locale || {}).lang);
        return result;
      },
      savePopupRef: function savePopupRef(ref) {
        this.popupRef = ref;
      },
      handleOpenChange: function handleOpenChange(open) {
        this.$emit('openChange', open);
      },
      handleFocus: function handleFocus(e) {
        this.$emit('focus', e);
      },
      handleBlur: function handleBlur(e) {
        this.$emit('blur', e);
      },
      handleMouseEnter: function handleMouseEnter(e) {
        this.$emit('mouseenter', e);
      },
      handleMouseLeave: function handleMouseLeave(e) {
        this.$emit('mouseleave', e);
      },
      focus: function focus() {
        this.$refs.picker.focus();
      },
      blur: function blur() {
        this.$refs.picker.blur();
      },
      renderPicker: function renderPicker(locale, localeCode) {
        var _classNames2,
            _this2 = this;

        var h = this.$createElement;

        var props = getOptionProps(this);
        var customizePrefixCls = props.prefixCls,
            customizeInputPrefixCls = props.inputPrefixCls,
            getCalendarContainer = props.getCalendarContainer,
            size = props.size,
            showTime = props.showTime,
            disabled = props.disabled,
            format = props.format;

        var mergedPickerType = showTime ? pickerType + 'Time' : pickerType;
        var mergedFormat = format || locale[LOCALE_FORMAT_MAPPING[mergedPickerType]] || DEFAULT_FORMAT[mergedPickerType];

        var _configProvider = this.configProvider,
            getPrefixCls = _configProvider.getPrefixCls,
            getContextPopupContainer = _configProvider.getPopupContainer;

        var getPopupContainer = getCalendarContainer || getContextPopupContainer;
        var prefixCls = getPrefixCls('calendar', customizePrefixCls);
        var inputPrefixCls = getPrefixCls('input', customizeInputPrefixCls);

        var pickerClass = classNames(prefixCls + '-picker', _defineProperty({}, prefixCls + '-picker-' + size, !!size));
        var pickerInputClass = classNames(prefixCls + '-picker-input', inputPrefixCls, (_classNames2 = {}, _defineProperty(_classNames2, inputPrefixCls + '-lg', size === 'large'), _defineProperty(_classNames2, inputPrefixCls + '-sm', size === 'small'), _defineProperty(_classNames2, inputPrefixCls + '-disabled', disabled), _classNames2));

        var timeFormat = showTime && showTime.format || 'HH:mm:ss';
        var vcTimePickerProps = _extends({}, generateShowHourMinuteSecond(timeFormat), {
          format: timeFormat,
          use12Hours: showTime && showTime.use12Hours
        });
        var columns = getColumns(vcTimePickerProps);
        var timePickerCls = prefixCls + '-time-picker-column-' + columns;
        var timePickerPanelProps = {
          props: _extends({}, vcTimePickerProps, showTime, {
            prefixCls: prefixCls + '-time-picker',
            placeholder: locale.timePickerLocale.placeholder,
            transitionName: 'slide-up'
          }),
          'class': timePickerCls,
          on: {
            esc: function esc() {}
          }
        };
        var timePicker = showTime ? h(TimePickerPanel, timePickerPanelProps) : null;
        var pickerProps = {
          props: _extends({}, props, {
            getCalendarContainer: getPopupContainer,
            format: mergedFormat,
            pickerClass: pickerClass,
            pickerInputClass: pickerInputClass,
            locale: locale,
            localeCode: localeCode,
            timePicker: timePicker
          }),
          on: _extends({}, getListeners(this), {
            openChange: this.handleOpenChange,
            focus: this.handleFocus,
            blur: this.handleBlur,
            mouseenter: this.handleMouseEnter,
            mouseleave: this.handleMouseLeave
          }),
          ref: 'picker',
          scopedSlots: this.$scopedSlots || {}
        };
        return h(
          Picker,
          pickerProps,
          [this.$slots && Object.keys(this.$slots).map(function (key) {
            return h(
              'template',
              { slot: key, key: key },
              [_this2.$slots[key]]
            );
          })]
        );
      }
    },

    render: function render() {
      var h = arguments[0];

      return h(LocaleReceiver, {
        attrs: {
          componentName: 'DatePicker',
          defaultLocale: this.getDefaultLocale
        },
        scopedSlots: { 'default': this.renderPicker }
      });
    }
  };
}