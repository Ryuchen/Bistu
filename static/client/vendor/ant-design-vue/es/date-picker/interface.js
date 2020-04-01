import _extends from 'babel-runtime/helpers/extends';
import * as moment from 'moment';
// import { TimePickerProps } from '../time-picker'
import PropTypes from '../_util/vue-types';

export var MomentType = {
  type: Object,
  validator: function validator(value) {
    return value === undefined || moment.isMoment(value);
  }
};

export var PickerProps = function PickerProps() {
  return {
    name: PropTypes.string,
    transitionName: PropTypes.string,
    prefixCls: PropTypes.string,
    inputPrefixCls: PropTypes.string,
    format: PropTypes.oneOfType([PropTypes.string, PropTypes.array]),
    disabled: PropTypes.bool,
    allowClear: PropTypes.bool,
    suffixIcon: PropTypes.any,
    popupStyle: PropTypes.object,
    dropdownClassName: PropTypes.string,
    locale: PropTypes.any,
    localeCode: PropTypes.string,
    size: PropTypes.oneOf(['large', 'small', 'default']),
    getCalendarContainer: PropTypes.func,
    open: PropTypes.bool,
    // onOpenChange: PropTypes.(status: bool) => void,
    disabledDate: PropTypes.func,
    showToday: PropTypes.bool,
    dateRender: PropTypes.any, // (current: moment.Moment, today: moment.Moment) => React.ReactNode,
    pickerClass: PropTypes.string,
    pickerInputClass: PropTypes.string,
    timePicker: PropTypes.any,
    autoFocus: PropTypes.bool,
    tagPrefixCls: PropTypes.string,
    tabIndex: PropTypes.oneOfType([PropTypes.string, PropTypes.number])
  };
};

export var SinglePickerProps = function SinglePickerProps() {
  return {
    value: MomentType,
    defaultValue: MomentType,
    defaultPickerValue: MomentType,
    renderExtraFooter: PropTypes.any,
    placeholder: PropTypes.string
    // onChange?: (date: moment.Moment, dateString: string) => void;
  };
};

export var DatePickerProps = function DatePickerProps() {
  return _extends({}, PickerProps(), SinglePickerProps(), {
    showTime: PropTypes.oneOfType([PropTypes.object, PropTypes.bool]),
    open: PropTypes.bool,
    disabledTime: PropTypes.func,
    // onOpenChange?: (status: bool) => void;
    // onOk?: (selectedTime: moment.Moment) => void;
    mode: PropTypes.oneOf(['time', 'date', 'month', 'year'])
  });
};

export var MonthPickerProps = function MonthPickerProps() {
  return _extends({}, PickerProps(), SinglePickerProps(), {
    placeholder: PropTypes.string,
    monthCellContentRender: PropTypes.func
  });
};
function isMomentArray(value) {
  if (Array.isArray(value)) {
    return value.length === 0 || value.findIndex(function (val) {
      return val === undefined || moment.isMoment(val);
    }) !== -1;
  }
  return false;
}

export var RangePickerValue = PropTypes.custom(isMomentArray);
// export const RangePickerPresetRange = PropTypes.oneOfType([RangePickerValue, PropTypes.func])

export var RangePickerProps = function RangePickerProps() {
  return _extends({}, PickerProps(), {
    tagPrefixCls: PropTypes.string,
    value: RangePickerValue,
    defaultValue: RangePickerValue,
    defaultPickerValue: RangePickerValue,
    timePicker: PropTypes.any,
    // onChange?: (dates: RangePickerValue, dateStrings: [string, string]) => void;
    // onCalendarChange?: (dates: RangePickerValue, dateStrings: [string, string]) => void;
    // onOk?: (selectedTime: moment.Moment) => void;
    showTime: PropTypes.oneOfType([PropTypes.object, PropTypes.bool]),
    ranges: PropTypes.object,
    placeholder: PropTypes.arrayOf(String),
    mode: PropTypes.oneOfType([PropTypes.string, PropTypes.arrayOf(String)]),
    separator: PropTypes.any,
    disabledTime: PropTypes.func,
    showToday: PropTypes.bool,
    renderExtraFooter: PropTypes.any
    // onPanelChange?: (value?: RangePickerValue, mode?: string | string[]) => void;
  });
};

export var WeekPickerProps = function WeekPickerProps() {
  return _extends({}, PickerProps(), SinglePickerProps(), {
    placeholder: PropTypes.string
  });
};

// export interface DatePickerDecorator extends React.ClassicComponentClass<DatePickerProps> {
//   RangePicker: React.ClassicComponentClass<RangePickerProps>;
//   MonthPicker: React.ClassicComponentClass<MonthPickerProps>;
//   WeekPicker: React.ClassicComponentClass<WeexPickerProps>;
// }