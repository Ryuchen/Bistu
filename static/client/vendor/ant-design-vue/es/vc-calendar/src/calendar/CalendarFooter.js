import _defineProperty from 'babel-runtime/helpers/defineProperty';
import _mergeJSXProps from 'babel-helper-vue-jsx-merge-props';
import _extends from 'babel-runtime/helpers/extends';
import PropTypes from '../../../_util/vue-types';
import BaseMixin from '../../../_util/BaseMixin';
import { getOptionProps, getListeners } from '../../../_util/props-util';
import TodayButton from './TodayButton';
import OkButton from './OkButton';
import TimePickerButton from './TimePickerButton';

var CalendarFooter = {
  mixins: [BaseMixin],
  props: {
    prefixCls: PropTypes.string,
    showDateInput: PropTypes.bool,
    disabledTime: PropTypes.any,
    timePicker: PropTypes.any,
    selectedValue: PropTypes.any,
    showOk: PropTypes.bool,
    // onSelect: PropTypes.func,
    value: PropTypes.object,
    renderFooter: PropTypes.func,
    defaultValue: PropTypes.object,
    locale: PropTypes.object,
    showToday: PropTypes.bool,
    disabledDate: PropTypes.func,
    showTimePicker: PropTypes.bool,
    okDisabled: PropTypes.bool,
    mode: PropTypes.string
  },
  methods: {
    onSelect: function onSelect(value) {
      this.__emit('select', value);
    },
    getRootDOMNode: function getRootDOMNode() {
      return this.$el;
    }
  },

  render: function render() {
    var h = arguments[0];

    var props = getOptionProps(this);
    var value = props.value,
        prefixCls = props.prefixCls,
        showOk = props.showOk,
        timePicker = props.timePicker,
        renderFooter = props.renderFooter,
        showToday = props.showToday,
        mode = props.mode;

    var footerEl = null;
    var extraFooter = renderFooter && renderFooter(mode);
    if (showToday || timePicker || extraFooter) {
      var _cls;

      var btnProps = {
        props: _extends({}, props, {
          value: value
        }),
        on: getListeners(this)
      };
      var nowEl = null;
      if (showToday) {
        nowEl = h(TodayButton, _mergeJSXProps([{ key: 'todayButton' }, btnProps]));
      }
      delete btnProps.props.value;
      var okBtn = null;
      if (showOk === true || showOk !== false && !!timePicker) {
        okBtn = h(OkButton, _mergeJSXProps([{ key: 'okButton' }, btnProps]));
      }
      var timePickerBtn = null;
      if (timePicker) {
        timePickerBtn = h(TimePickerButton, _mergeJSXProps([{ key: 'timePickerButton' }, btnProps]));
      }

      var footerBtn = void 0;
      if (nowEl || timePickerBtn || okBtn || extraFooter) {
        footerBtn = h(
          'span',
          { 'class': prefixCls + '-footer-btn' },
          [extraFooter, nowEl, timePickerBtn, okBtn]
        );
      }
      var cls = (_cls = {}, _defineProperty(_cls, prefixCls + '-footer', true), _defineProperty(_cls, prefixCls + '-footer-show-ok', !!okBtn), _cls);
      footerEl = h(
        'div',
        { 'class': cls },
        [footerBtn]
      );
    }
    return footerEl;
  }
};

export default CalendarFooter;