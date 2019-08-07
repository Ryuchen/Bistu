'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _extends2 = require('babel-runtime/helpers/extends');

var _extends3 = _interopRequireDefault(_extends2);

var _vueTypes = require('../../_util/vue-types');

var _vueTypes2 = _interopRequireDefault(_vueTypes);

var _get = require('lodash/get');

var _get2 = _interopRequireDefault(_get);

var _propsUtil = require('../../_util/props-util');

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

function isInvalidRenderCellText(text) {
  return text && !(0, _propsUtil.isValidElement)(text) && Object.prototype.toString.call(text) === '[object Object]';
}

exports['default'] = {
  name: 'TableCell',
  props: {
    record: _vueTypes2['default'].object,
    prefixCls: _vueTypes2['default'].string,
    index: _vueTypes2['default'].number,
    indent: _vueTypes2['default'].number,
    indentSize: _vueTypes2['default'].number,
    column: _vueTypes2['default'].object,
    expandIcon: _vueTypes2['default'].any,
    component: _vueTypes2['default'].any
  },
  methods: {
    handleClick: function handleClick(e) {
      var record = this.record,
          onCellClick = this.column.onCellClick;

      if (onCellClick) {
        onCellClick(record, e);
      }
    }
  },

  render: function render() {
    var h = arguments[0];
    var record = this.record,
        indentSize = this.indentSize,
        prefixCls = this.prefixCls,
        indent = this.indent,
        index = this.index,
        expandIcon = this.expandIcon,
        column = this.column,
        BodyCell = this.component;
    var dataIndex = column.dataIndex,
        customRender = column.customRender,
        _column$className = column.className,
        className = _column$className === undefined ? '' : _column$className;

    var cls = className || column['class'];
    // We should return undefined if no dataIndex is specified, but in order to
    // be compatible with object-path's behavior, we return the record object instead.
    var text = void 0;
    if (typeof dataIndex === 'number') {
      text = (0, _get2['default'])(record, dataIndex);
    } else if (!dataIndex || dataIndex.length === 0) {
      text = record;
    } else {
      text = (0, _get2['default'])(record, dataIndex);
    }
    var tdProps = {
      props: {},
      attrs: {},
      'class': cls,
      on: {
        click: this.handleClick
      }
    };
    var colSpan = void 0;
    var rowSpan = void 0;

    if (customRender) {
      text = customRender(text, record, index);
      if (isInvalidRenderCellText(text)) {
        tdProps.attrs = text.attrs || {};
        tdProps.props = text.props || {};
        colSpan = tdProps.attrs.colSpan;
        rowSpan = tdProps.attrs.rowSpan;
        text = text.children;
      }
    }

    if (column.customCell) {
      tdProps = (0, _propsUtil.mergeProps)(tdProps, column.customCell(record, index));
    }

    // Fix https://github.com/ant-design/ant-design/issues/1202
    if (isInvalidRenderCellText(text)) {
      text = null;
    }

    var indentText = expandIcon ? h('span', {
      style: { paddingLeft: indentSize * indent + 'px' },
      'class': prefixCls + '-indent indent-level-' + indent
    }) : null;

    if (rowSpan === 0 || colSpan === 0) {
      return null;
    }
    if (column.align) {
      tdProps.style = (0, _extends3['default'])({}, tdProps.style, { textAlign: column.align });
    }

    return h(
      BodyCell,
      tdProps,
      [indentText, expandIcon, text]
    );
  }
};