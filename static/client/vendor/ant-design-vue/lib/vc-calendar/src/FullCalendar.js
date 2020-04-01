'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _extends2 = require('babel-runtime/helpers/extends');

var _extends3 = _interopRequireDefault(_extends2);

var _moment = require('moment');

var _moment2 = _interopRequireDefault(_moment);

var _vueTypes = require('../../_util/vue-types');

var _vueTypes2 = _interopRequireDefault(_vueTypes);

var _BaseMixin = require('../../_util/BaseMixin');

var _BaseMixin2 = _interopRequireDefault(_BaseMixin);

var _propsUtil = require('../../_util/props-util');

var _DateTable = require('./date/DateTable');

var _DateTable2 = _interopRequireDefault(_DateTable);

var _MonthTable = require('./month/MonthTable');

var _MonthTable2 = _interopRequireDefault(_MonthTable);

var _CalendarMixin = require('./mixin/CalendarMixin');

var _CalendarMixin2 = _interopRequireDefault(_CalendarMixin);

var _CommonMixin = require('./mixin/CommonMixin');

var _CommonMixin2 = _interopRequireDefault(_CommonMixin);

var _CalendarHeader = require('./full-calendar/CalendarHeader');

var _CalendarHeader2 = _interopRequireDefault(_CalendarHeader);

var _en_US = require('./locale/en_US');

var _en_US2 = _interopRequireDefault(_en_US);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

var FullCalendar = {
  props: {
    locale: _vueTypes2['default'].object.def(_en_US2['default']),
    format: _vueTypes2['default'].oneOfType([_vueTypes2['default'].string, _vueTypes2['default'].array]),
    visible: _vueTypes2['default'].bool.def(true),
    prefixCls: _vueTypes2['default'].string.def('rc-calendar'),
    defaultType: _vueTypes2['default'].string.def('date'),
    type: _vueTypes2['default'].string,
    fullscreen: _vueTypes2['default'].bool.def(false),
    monthCellRender: _vueTypes2['default'].func,
    dateCellRender: _vueTypes2['default'].func,
    showTypeSwitch: _vueTypes2['default'].bool.def(true),
    Select: _vueTypes2['default'].object.isRequired,
    headerComponents: _vueTypes2['default'].array,
    headerComponent: _vueTypes2['default'].object, // The whole header component
    headerRender: _vueTypes2['default'].func,
    showHeader: _vueTypes2['default'].bool.def(true),
    disabledDate: _vueTypes2['default'].func,
    value: _vueTypes2['default'].object,
    defaultValue: _vueTypes2['default'].object,
    selectedValue: _vueTypes2['default'].object,
    defaultSelectedValue: _vueTypes2['default'].object,
    renderFooter: _vueTypes2['default'].func.def(function () {
      return null;
    }),
    renderSidebar: _vueTypes2['default'].func.def(function () {
      return null;
    })
  },
  mixins: [_BaseMixin2['default'], _CommonMixin2['default'], _CalendarMixin2['default']],
  data: function data() {
    var type = void 0;
    if ((0, _propsUtil.hasProp)(this, 'type')) {
      type = this.type;
    } else {
      type = this.defaultType;
    }
    var props = this.$props;
    return {
      sType: type,
      sValue: props.value || props.defaultValue || (0, _moment2['default'])(),
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
      var sValue = val || this.defaultValue || (0, _CalendarMixin.getNowByCurrentStateValue)(this.sValue);
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
      if (!(0, _propsUtil.hasProp)(this, 'type')) {
        this.setState({
          sType: type
        });
      }
      this.__emit('typeChange', type);
    }
  },

  render: function render() {
    var h = arguments[0];

    var props = (0, _propsUtil.getOptionProps)(this);
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
        var TheHeader = headerComponent || _CalendarHeader2['default'];
        var headerProps = {
          props: (0, _extends3['default'])({}, props, {
            prefixCls: prefixCls + '-full',
            type: type,
            value: value
          }),
          on: (0, _extends3['default'])({}, (0, _propsUtil.getListeners)(this), {
            typeChange: this.setType,
            valueChange: this.setValue
          }),
          key: 'calendar-header'
        };
        header = h(TheHeader, headerProps);
      }
    }

    var table = type === 'date' ? h(_DateTable2['default'], {
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
    }) : h(_MonthTable2['default'], {
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

exports['default'] = FullCalendar;