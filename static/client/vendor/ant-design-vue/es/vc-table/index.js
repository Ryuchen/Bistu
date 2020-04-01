import _extends from 'babel-runtime/helpers/extends';
// base rc-table 6.10.9
import T from './src/Table';
import Column from './src/Column';
import ColumnGroup from './src/ColumnGroup';
import { getOptionProps, getKey, getClass, getStyle, getEvents, getSlotOptions, camelize, getSlots, getListeners } from '../_util/props-util';
import { INTERNAL_COL_DEFINE } from './src/utils';
var Table = {
  name: 'Table',
  Column: Column,
  ColumnGroup: ColumnGroup,
  props: T.props,
  methods: {
    getTableNode: function getTableNode() {
      return this.$refs.table.tableNode;
    },
    getBodyTable: function getBodyTable() {
      return this.$refs.table.ref_bodyTable;
    },
    normalize: function normalize() {
      var _this = this;

      var elements = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : [];

      var columns = [];
      elements.forEach(function (element) {
        if (!element.tag) {
          return;
        }
        var key = getKey(element);
        var style = getStyle(element);
        var cls = getClass(element);
        var props = getOptionProps(element);
        var events = getEvents(element);
        var listeners = {};
        Object.keys(events).forEach(function (e) {
          var k = 'on-' + e;
          listeners[camelize(k)] = events[e];
        });

        var _getSlots = getSlots(element),
            children = _getSlots['default'],
            title = _getSlots.title;

        var column = _extends({ title: title }, props, { style: style, 'class': cls }, listeners);
        if (key) {
          column.key = key;
        }
        if (getSlotOptions(element).isTableColumnGroup) {
          column.children = _this.normalize(typeof children === 'function' ? children() : children);
        } else {
          var customRender = element.data && element.data.scopedSlots && element.data.scopedSlots['default'];
          column.customRender = column.customRender || customRender;
        }
        columns.push(column);
      });
      return columns;
    }
  },
  render: function render() {
    var h = arguments[0];
    var $slots = this.$slots,
        normalize = this.normalize;

    var props = getOptionProps(this);
    var columns = props.columns || normalize($slots['default']);
    var tProps = {
      props: _extends({}, props, {
        columns: columns
      }),
      on: getListeners(this),
      ref: 'table'
    };
    return h(T, tProps);
  }
};

export default Table;
export { Column, ColumnGroup, INTERNAL_COL_DEFINE };