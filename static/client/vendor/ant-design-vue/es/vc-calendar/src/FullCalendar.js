import _extends from 'babel-runtime/helpers/extends';
import moment from 'moment';
import PropTypes from '../../_util/vue-types';
import BaseMixin from '../../_util/BaseMixin';
import { getOptionProps, hasProp, getListeners } from '../../_util/props-util';
import DateTable from './date/DateTable';
import MonthTable from './month/MonthTable';
import CalendarMixin, { getNowByCurrentStateValue } from './mixin/CalendarMixin';
import CommonMixin from './mixin/CommonMixin';
import CalendarHeader from './full-calendar/CalendarHeader';
import enUs from './locale/en_US';
var FullCalendar = {
  props: {
    locale: PropTypes.object.def(enUs),
    format: PropTypes.oneOfType([PropTypes.string, PropTypes.array]),
    visible: PropTypes.bool.def(true),
    prefixCls: PropTypes.string.def('rc-calendar'),
    defaultType: PropTypes.string.def('date'),
    type: PropTypes.string,
    fullscreen: PropTypes.bool.def(false),
    monthCellRender: PropTypes.func,
    dateCellRender: PropTypes.func,
    showTypeSwitch: PropTypes.bool.def(true),
    Select: PropTypes.object.isRequired,
    headerComponents: PropTypes.array,
    headerComponent: PropTypes.object, // The whole header component
    headerRender: PropTypes.func,
    showHeader: PropTypes.bool.def(true),
    disabledDate: PropTypes.func,
    value: PropTypes.object,
    defaultValue: PropTypes.object,
    selectedValue: PropTypes.object,
    defaultSelectedValue: PropTypes.object,
    renderFooter: PropTypes.func.def(function () {
      return null;
    }),
    renderSidebar: PropTypes.func.def(function () {
      return null;
    })
  },
  mixins: [BaseMixin, CommonMixin, CalendarMixin],
  data: function data() {
    var type = void 0;
    if (hasProp(this, 'type')) {
      type = this.type;
    } else {
      type = this.defaultType;
    }
    var props = this.$props;
    return {
      sType: type,
      sValue: props.value || props.defaultValue || moment(),
      sSelectedValue: props.selectedValue || props.defaultSelectedValue
    };
  },

  watch: {
    type: function type(val) {
      this.setState({
        sType: val
      });
    },
    value: function value(val) {
      var sValue = val || this.defaultValue || getNowByCurrentStateValue(this.sValue);
      this.setState({
        sValue: sValue
      });
    },
    selectedValue: function selectedValue(val) {
      this.setState({
        sSelectedValue: val
      });
    }
  },
  methods: {
    onMonthSelect: function onMonthSelect(value) {
      this.onSelect(value, {
        target: 'month'
      });
    },
    setType: function setType(type) {
      if (!hasProp(this, 'type')) {
        this.setState({
          sType: type
        });
      }
      this.__emit('typeChange', type);
    }
  },

  render: function render() {
    var h = arguments[0];

    var props = getOptionProps(this);
    var locale = props.locale,
        prefixCls = props.prefixCls,
        fullscreen = props.fullscreen,
        showHeader = props.showHeader,
        headerComponent = props.headerComponent,
        headerRender = props.headerRender,
        disabledDate = props.disabledDate;
    var value = this.sValue,
        type = this.sType;


    var header = null;
    if (showHeader) {
      if (headerRender) {
        header = headerRender(value, type, locale);
      } else {
        var TheHeader = headerComponent || CalendarHeader;
        var headerProps = {
          props: _extends({}, props, {
            prefixCls: prefixCls + '-full',
            type: type,
            value: value
          }),
          on: _extends({}, getListeners(this), {
            typeChange: this.setType,
            valueChange: this.setValue
          }),
          key: 'calendar-header'
        };
        header = h(TheHeader, headerProps);
      }
    }

    var table = type === 'date' ? h(DateTable, {
      attrs: {
        dateRender: props.dateCellRender,
        contentRender: props.dateCellContentRender,
        locale: locale,
        prefixCls: prefixCls,

        value: value,
        disabledDate: disabledDate
      },
      on: {
        'select': this.onSelect
      }
    }) : h(MonthTable, {
      attrs: {
        cellRender: props.monthCellRender,
        contentRender: props.monthCellContentRender,
        locale: locale,

        prefixCls: prefixCls + '-month-panel',
        value: value,
        disabledDate: disabledDate
      },
      on: {
        'select': this.onMonthSelect
      }
    });

    var children = [header, h(
      'div',
      { key: 'calendar-body', 'class': prefixCls + '-calendar-body' },
      [table]
    )];

    var className = [prefixCls + '-full'];

    if (fullscreen) {
      className.push(prefixCls + '-fullscreen');
    }

    return this.renderRoot({
      children: children,
      'class': className.join(' ')
    });
  }
};

export default FullCalendar;