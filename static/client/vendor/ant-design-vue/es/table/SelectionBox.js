import _extends from 'babel-runtime/helpers/extends';
import _objectWithoutProperties from 'babel-runtime/helpers/objectWithoutProperties';
import Checkbox from '../checkbox';
import Radio from '../radio';
import { SelectionBoxProps } from './interface';
import BaseMixin from '../_util/BaseMixin';
import { getOptionProps, getListeners } from '../_util/props-util';

export default {
  name: 'SelectionBox',
  mixins: [BaseMixin],
  props: SelectionBoxProps,
  data: function data() {
    return {
      checked: this.getCheckState(this.$props)
    };
  },
  mounted: function mounted() {
    this.subscribe();
  },
  beforeDestroy: function beforeDestroy() {
    if (this.unsubscribe) {
      this.unsubscribe();
    }
  },

  methods: {
    getCheckState: function getCheckState(props) {
      var store = props.store,
          defaultSelection = props.defaultSelection,
          rowIndex = props.rowIndex;

      var checked = false;
      if (store.getState().selectionDirty) {
        checked = store.getState().selectedRowKeys.indexOf(rowIndex) >= 0;
      } else {
        checked = store.getState().selectedRowKeys.indexOf(rowIndex) >= 0 || defaultSelection.indexOf(rowIndex) >= 0;
      }
      return checked;
    },
    subscribe: function subscribe() {
      var _this = this;

      var store = this.store;

      this.unsubscribe = store.subscribe(function () {
        var checked = _this.getCheckState(_this.$props);
        _this.setState({ checked: checked });
      });
    }
  },

  render: function render() {
    var h = arguments[0];

    var _getOptionProps = getOptionProps(this),
        type = _getOptionProps.type,
        rowIndex = _getOptionProps.rowIndex,
        rest = _objectWithoutProperties(_getOptionProps, ['type', 'rowIndex']);

    var checked = this.checked;

    var checkboxProps = {
      props: _extends({
        checked: checked
      }, rest),
      on: getListeners(this)
    };
    if (type === 'radio') {
      checkboxProps.props.value = rowIndex;
      return h(Radio, checkboxProps);
    }
    return h(Checkbox, checkboxProps);
  }
};