'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _index = require('../index');

var _index2 = _interopRequireDefault(_index);

require('../assets/index.less');

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

/* eslint-disable no-console,func-names,react/no-multi-comp */
var data = [{ key: 0, a: '123' }, { key: 1, a: 'cdd', b: 'edd' }, { key: 2, a: '1333', c: 'eee', d: 2 }];

var columns = [{ title: 'title 1', dataIndex: 'a', key: 'a', width: 100 }, { title: 'title 2', dataIndex: 'b', key: 'b', width: 100 }, { title: 'title 3', dataIndex: 'c', key: 'c', width: 200 }];
exports['default'] = {
  methods: {
    CustomExpandIcon: function CustomExpandIcon(props) {
      var h = this.$createElement;

      var text = void 0;
      if (props.expanded) {
        text = h('span', ['\u21E7 collapse']);
      } else {
        text = h('span', ['\u21E9 expand']);
      }
      return h(
        'a',
        {
          'class': 'expand-row-icon',
          on: {
            'click': function click(e) {
              return props.onExpand(props.record, e);
            }
          },

          style: { color: 'blue', cursor: 'pointer' }
        },
        [text]
      );
    },
    onExpand: function onExpand(expanded, record) {
      console.log('onExpand', expanded, record);
    }
  },
  render: function render() {
    var h = arguments[0];

    return h('div', [h('h2', ['expandIcon']), h('div', [h(_index2['default'], {
      attrs: {
        columns: columns,
        expandedRowRender: function expandedRowRender(record) {
          return h('p', ['extra: ', record.a]);
        },

        expandIcon: this.CustomExpandIcon,
        expandIconAsCell: true,
        data: data
      },
      on: {
        'expand': this.onExpand
      }
    })])]);
  }
};