'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _toConsumableArray2 = require('babel-runtime/helpers/toConsumableArray');

var _toConsumableArray3 = _interopRequireDefault(_toConsumableArray2);

var _BaseMixin = require('../../_util/BaseMixin');

var _BaseMixin2 = _interopRequireDefault(_BaseMixin);

require('../assets/index.less');

var _index = require('../src/index');

var _index2 = _interopRequireDefault(_index);

var _util = require('./util');

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

/* eslint react/no-multi-comp:0, no-console:0 */

exports['default'] = {
  mixins: [_BaseMixin2['default']],
  data: function data() {
    return {
      treeData: [{ label: 'pNode 01', value: '0-0', key: '0-0' }, { label: 'pNode 02', value: '0-1', key: '0-1' }, { label: 'pNode 03', value: '0-2', key: '0-2', isLeaf: true }],
      // value: '0-0',
      value: { value: '0-0-0-value', label: '0-0-0-label' }
    };
  },
  methods: {
    onChange: function onChange(value) {
      console.log(value);
      this.setState({
        value: value
      });
    },
    onLoadData: function onLoadData(treeNode) {
      var _this = this;

      console.log(treeNode);
      return new Promise(function (resolve) {
        setTimeout(function () {
          var treeData = [].concat((0, _toConsumableArray3['default'])(_this.treeData));
          (0, _util.getNewTreeData)(treeData, treeNode.eventKey, (0, _util.generateTreeNodes)(treeNode), 2);
          _this.setState({ treeData: treeData });
          resolve();
        }, 500);
      });
    }
  },

  render: function render() {
    var h = arguments[0];

    return h(
      'div',
      { style: { padding: '10px 30px' } },
      [h('h2', ['dynamic render']), h(_index2['default'], {
        style: { width: '300px' },
        attrs: { treeData: this.treeData,
          labelInValue: true,
          value: this.value,

          loadData: this.onLoadData,
          __propsSymbol__: Symbol()
        },
        on: {
          'change': this.onChange
        }
      })]
    );
  }
};