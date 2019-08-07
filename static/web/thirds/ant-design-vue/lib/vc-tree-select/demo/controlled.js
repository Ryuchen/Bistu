'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _BaseMixin = require('../../_util/BaseMixin');

var _BaseMixin2 = _interopRequireDefault(_BaseMixin);

require('../assets/index.less');

require('../../vc-dialog/assets/index.less');

var _index = require('../src/index');

var _index2 = _interopRequireDefault(_index);

require('./demo.less');

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

exports['default'] = {
  mixins: [_BaseMixin2['default']],
  data: function data() {
    return {
      treeExpandedKeys: []
    };
  },
  methods: {
    onTreeExpand: function onTreeExpand(treeExpandedKeys) {
      this.setState({
        treeExpandedKeys: treeExpandedKeys
      });
    },
    setTreeExpandedKeys: function setTreeExpandedKeys() {
      this.setState({
        treeExpandedKeys: ['000', '0-1-0']
      });
    }
  },

  render: function render() {
    var h = arguments[0];
    var treeExpandedKeys = this.treeExpandedKeys;


    return h('div', [h('h2', ['Conrolled treeExpandedKeys']), h(
      _index2['default'],
      {
        style: { width: '200px' },
        attrs: { dropdownStyle: { maxHeight: '200px', overflow: 'auto' },
          treeExpandedKeys: treeExpandedKeys,

          __propsSymbol__: Symbol()
        },
        on: {
          'treeExpand': this.onTreeExpand
        }
      },
      [h(
        _index.TreeNode,
        {
          attrs: { value: '', title: 'parent 1' },
          key: '000' },
        [h(
          _index.TreeNode,
          {
            attrs: { value: 'parent 1-0', title: 'parent 1-0' },
            key: '0-1-0' },
          [h(_index.TreeNode, {
            attrs: { value: 'leaf1', title: 'my leaf' },
            key: 'random' }), h(_index.TreeNode, {
            attrs: { value: 'leaf2', title: 'your leaf', disabled: true },
            key: 'random1' })]
        ), h(
          _index.TreeNode,
          {
            attrs: { value: 'parent 1-1', title: 'parent 1-1' },
            key: '0-1-1' },
          [h(_index.TreeNode, {
            attrs: {
              value: 'sss',
              title: h(
                'span',
                { style: { color: 'red' } },
                ['sss']
              )
            },
            key: 'random3'
          }), h(
            _index.TreeNode,
            {
              attrs: { value: 'same value1', title: 'same txtle' },
              key: '0-1-1-1' },
            [h(_index.TreeNode, {
              attrs: {
                value: 'same value10',
                title: 'same titlexd'
              },
              key: '0-1-1-1-0',
              style: { color: 'red', background: 'green' }
            })]
          )]
        )]
      ), h(
        _index.TreeNode,
        {
          attrs: { value: 'same value2', title: 'same title' },
          key: '0-2' },
        [h(_index.TreeNode, {
          attrs: { value: '2same value', title: '2same title' },
          key: '0-2-0' })]
      ), h(_index.TreeNode, {
        attrs: { value: 'same value3', title: 'same title' },
        key: '0-3' })]
    ), h(
      'button',
      {
        on: {
          'click': this.setTreeExpandedKeys
        }
      },
      ['Set treeExpandedKeys']
    )]);
  }
}; /* eslint react/no-multi-comp:0, no-console:0, no-alert: 0 */