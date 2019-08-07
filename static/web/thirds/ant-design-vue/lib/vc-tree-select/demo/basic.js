'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _toConsumableArray2 = require('babel-runtime/helpers/toConsumableArray');

var _toConsumableArray3 = _interopRequireDefault(_toConsumableArray2);

var _BaseMixin = require('../../_util/BaseMixin');

var _BaseMixin2 = _interopRequireDefault(_BaseMixin);

require('../assets/index.less');

require('../../vc-dialog/assets/index.less');

var _vcDialog = require('../../vc-dialog');

var _vcDialog2 = _interopRequireDefault(_vcDialog);

var _index = require('../src/index');

var _index2 = _interopRequireDefault(_index);

var _util = require('./util');

require('./demo.less');

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

function isLeaf(value) {
  if (!value) {
    return false;
  }
  var queues = [].concat((0, _toConsumableArray3['default'])(_util.gData));
  while (queues.length) {
    // BFS
    var item = queues.shift();
    if (item.value === value) {
      if (!item.children) {
        return true;
      }
      return false;
    }
    if (item.children) {
      queues = queues.concat(item.children);
    }
  }
  return false;
} /* eslint react/no-multi-comp:0, no-console:0, no-alert: 0 */


function findPath(value, data) {
  var sel = [];
  function loop(selected, children) {
    for (var i = 0; i < children.length; i++) {
      var item = children[i];
      if (selected === item.value) {
        sel.push(item);
        return;
      }
      if (item.children) {
        loop(selected, item.children, item);
        if (sel.length) {
          sel.push(item);
          return;
        }
      }
    }
  }
  loop(value, data);
  return sel;
}

exports['default'] = {
  mixins: [_BaseMixin2['default']],
  data: function data() {
    return {
      tsOpen: false,
      visible: false,
      searchValue: '0-0-0-label',
      value: '0-0-0-value1',
      // value: ['0-0-0-0-value', '0-0-0-1-value', '0-0-0-2-value'],
      lv: { value: '0-0-0-value', label: 'spe label' },
      multipleValue: [],
      simpleSearchValue: 'test111',
      simpleTreeData: [{ key: 1, pId: 0, label: 'test1', value: 'test1' }, { key: 121, pId: 0, label: 'test2', value: 'test2' }, { key: 11, pId: 1, label: 'test11', value: 'test11' }, { key: 12, pId: 1, label: 'test12', value: 'test12' }, { key: 111, pId: 11, label: 'test111', value: 'test111' }],
      treeDataSimpleMode: {
        id: 'key',
        rootPId: 0
      }
    };
  },
  methods: {
    onClick: function onClick() {
      this.setState({
        visible: true
      });
    },
    onClose: function onClose() {
      this.setState({
        visible: false
      });
    },
    onSearch: function onSearch(value) {
      console.log('Do Search:', value, arguments);
      this.setState({ searchValue: value });
    },
    onChange: function onChange(value) {
      var _console;

      for (var _len = arguments.length, rest = Array(_len > 1 ? _len - 1 : 0), _key = 1; _key < _len; _key++) {
        rest[_key - 1] = arguments[_key];
      }

      (_console = console).log.apply(_console, ['onChange', value].concat((0, _toConsumableArray3['default'])(rest)));
      this.setState({ value: value });
    },
    onChangeChildren: function onChangeChildren() {
      var _console2;

      for (var _len2 = arguments.length, args = Array(_len2), _key2 = 0; _key2 < _len2; _key2++) {
        args[_key2] = arguments[_key2];
      }

      (_console2 = console).log.apply(_console2, ['onChangeChildren'].concat((0, _toConsumableArray3['default'])(args)));
      var value = args[0];
      var pre = value ? this.value : undefined;
      this.setState({ value: isLeaf(value) ? value : pre });
    },
    onChangeLV: function onChangeLV(value) {
      console.log('labelInValue', arguments);
      if (!value) {
        this.setState({ lv: undefined });
        return;
      }
      var path = findPath(value.value, _util.gData).map(function (i) {
        return i.label;
      }).reverse().join(' > ');
      this.setState({ lv: { value: value.value, label: path } });
    },
    onMultipleChange: function onMultipleChange(value) {
      console.log('onMultipleChange', arguments);
      this.setState({ multipleValue: value });
    },
    onSelect: function onSelect() {
      // use onChange instead
      console.log(arguments);
    },
    onDropdownVisibleChange: function onDropdownVisibleChange(visible, info) {
      console.log(visible, this.value, info);
      if (Array.isArray(this.value) && this.value.length > 1 && this.value.length < 3) {
        window.alert('please select more than two item or less than one item.');
        return false;
      }
      return true;
    },
    filterTreeNode: function filterTreeNode(input, child) {
      return String(child.data.props.title).indexOf(input) === 0;
    }
  },

  render: function render() {
    var _this = this;

    var h = arguments[0];

    return h(
      'div',
      { style: { margin: '20px' } },
      [h('h2', ['tree-select in dialog']), h(
        'button',
        { 'class': 'btn btn-primary', on: {
            'click': this.onClick
          }
        },
        ['show dialog']
      ), this.visible ? h(
        _vcDialog2['default'],
        {
          attrs: {
            visible: this.visible,
            animation: 'zoom',
            maskAnimation: 'fade',

            id: 'area'
          },
          on: {
            'close': this.onClose
          },

          style: { width: '600px', height: '400px', overflow: 'auto' } },
        [h(
          'div',
          { style: { height: '600px', paddingTop: '100px' } },
          [h(_index2['default'], {
            attrs: {
              getPopupContainer: function getPopupContainer(triggerNode) {
                return triggerNode.parentNode;
              },

              transitionName: 'rc-tree-select-dropdown-slide-up',
              choiceTransitionName: 'rc-tree-select-selection__choice-zoom',
              dropdownStyle: { maxHeight: '200px', overflow: 'auto', zIndex: 1500 },
              placeholder: h('i', ['\u8BF7\u4E0B\u62C9\u9009\u62E9']),
              searchPlaceholder: 'please search',
              showSearch: true,
              allowClear: true,
              treeLine: true,
              value: this.value,
              treeData: _util.gData,
              treeNodeFilterProp: 'label',
              filterTreeNode: false,

              __propsSymbol__: Symbol()
            },
            style: { width: '300px' }, on: {
              'search': this.onSearch,
              'change': this.onChange,
              'select': this.onSelect
            }
          })]
        )]
      ) : null, h('h2', ['single select']), h(_index2['default'], {
        style: { width: '300px' },
        attrs: { transitionName: 'rc-tree-select-dropdown-slide-up',
          choiceTransitionName: 'rc-tree-select-selection__choice-zoom',
          dropdownStyle: { maxHeight: '200px', overflow: 'auto' },
          placeholder: h('i', ['\u8BF7\u4E0B\u62C9\u9009\u62E9']),
          searchPlaceholder: 'please search',
          showSearch: true,
          allowClear: true,
          treeLine: true,
          searchValue: this.searchValue,
          value: this.value,
          treeData: _util.gData,
          treeNodeFilterProp: 'label',
          filterTreeNode: false,

          open: this.tsOpen,

          dropdownVisibleChange: function dropdownVisibleChange(v, info) {
            console.log('single onDropdownVisibleChange', v, info);
            // document clicked
            if (info.documentClickClose && _this.value === '0-0-0-0-value') {
              return false;
            }
            _this.setState({
              tsOpen: v
            });
            return true;
          },

          __propsSymbol__: Symbol()
        },
        on: {
          'search': this.onSearch,
          'change': function change(value) {
            var _console3;

            for (var _len3 = arguments.length, args = Array(_len3 > 1 ? _len3 - 1 : 0), _key3 = 1; _key3 < _len3; _key3++) {
              args[_key3 - 1] = arguments[_key3];
            }

            (_console3 = console).log.apply(_console3, ['onChange', value].concat(args));
            if (value === '0-0-0-0-value') {
              _this.setState({ tsOpen: true });
            } else {
              _this.setState({ tsOpen: false });
            }
            _this.setState({ value: value });
          },
          'select': this.onSelect
        }
      }), h('h2', ['single select (just select children)']), h(_index2['default'], {
        style: { width: '300px' },
        attrs: { transitionName: 'rc-tree-select-dropdown-slide-up',
          choiceTransitionName: 'rc-tree-select-selection__choice-zoom',
          dropdownStyle: { maxHeight: '200px', overflow: 'auto' },
          placeholder: h('i', ['\u8BF7\u4E0B\u62C9\u9009\u62E9']),
          searchPlaceholder: 'please search',
          showSearch: true,
          allowClear: true,
          treeLine: true,
          value: this.value,
          treeData: _util.gData,
          treeNodeFilterProp: 'label',
          filterTreeNode: false,

          __propsSymbol__: Symbol()
        },
        on: {
          'change': this.onChangeChildren
        }
      }), h('h2', ['multiple select']), h(_index2['default'], {
        style: { width: '300px' },
        attrs: { transitionName: 'rc-tree-select-dropdown-slide-up',
          choiceTransitionName: 'rc-tree-select-selection__choice-zoom',
          dropdownStyle: { maxHeight: '200px', overflow: 'auto' },
          placeholder: h('i', ['\u8BF7\u4E0B\u62C9\u9009\u62E9']),
          searchPlaceholder: 'please search',
          multiple: true,
          value: this.multipleValue,
          treeData: _util.gData,
          treeNodeFilterProp: 'title',

          allowClear: true,
          __propsSymbol__: Symbol()
        },
        on: {
          'change': this.onMultipleChange,
          'select': this.onSelect
        }
      }), h('h2', ['check select']), h(_index2['default'], {
        'class': 'check-select',
        attrs: { transitionName: 'rc-tree-select-dropdown-slide-up',
          choiceTransitionName: 'rc-tree-select-selection__choice-zoom',
          dropdownStyle: { height: '200px', overflow: 'auto' },
          dropdownPopupAlign: { overflow: { adjustY: 0, adjustX: 0 }, offset: [0, 2] },
          dropdownVisibleChange: this.onDropdownVisibleChange,
          placeholder: h('i', ['\u8BF7\u4E0B\u62C9\u9009\u62E9']),
          searchPlaceholder: 'please search',
          treeLine: true,
          maxTagTextLength: 10,
          value: this.value,
          autoClearSearchValue: true,
          treeData: _util.gData,
          treeNodeFilterProp: 'title',
          treeCheckable: true,
          showCheckedStrategy: _index.SHOW_PARENT,

          maxTagCount: 2,
          maxTagPlaceholder: function maxTagPlaceholder(valueList) {
            console.log('Max Tag Rest Value:', valueList);
            return valueList.length + ' rest...';
          },
          __propsSymbol__: Symbol()
        },
        on: {
          'change': this.onChange,
          'select': this.onSelect
        }
      }), h('h2', ['labelInValue & show path']), h(_index2['default'], {
        style: { width: '500px' },
        attrs: { transitionName: 'rc-tree-select-dropdown-slide-up',
          choiceTransitionName: 'rc-tree-select-selection__choice-zoom',
          dropdownStyle: { maxHeight: '200px', overflow: 'auto' },
          placeholder: h('i', ['\u8BF7\u4E0B\u62C9\u9009\u62E9']),
          searchPlaceholder: 'please search',
          showSearch: true,
          allowClear: true,
          treeLine: true,
          value: this.lv,
          labelInValue: true,
          treeData: _util.gData,
          treeNodeFilterProp: 'label',
          filterTreeNode: false,

          __propsSymbol__: Symbol()
        },
        on: {
          'change': this.onChangeLV
        }
      }), h('h2', ['use treeDataSimpleMode']), h(_index2['default'], {
        style: { width: '300px' },
        attrs: { dropdownStyle: { maxHeight: '200px', overflow: 'auto' },
          placeholder: h('i', ['\u8BF7\u4E0B\u62C9\u9009\u62E9']),
          searchPlaceholder: 'please search',
          treeLine: true,
          maxTagTextLength: 10,
          searchValue: this.simpleSearchValue,

          value: this.value,
          treeData: this.simpleTreeData,
          treeNodeFilterProp: 'title',
          treeDataSimpleMode: this.treeDataSimpleMode,
          treeCheckable: true,
          showCheckedStrategy: _index.SHOW_PARENT,

          __propsSymbol__: Symbol()
        },
        on: {
          'search': function search(simpleSearchValue) {
            _this.setState({ simpleSearchValue: simpleSearchValue });
          },
          'change': this.onChange,
          'select': this.onSelect
        }
      }), h('h2', ['Testing in extreme conditions (Boundary conditions test) ']), h(_index2['default'], {
        style: { width: '200px' },
        attrs: { dropdownStyle: { maxHeight: '200px', overflow: 'auto' },
          defaultValue: 'leaf1',
          multiple: true,
          treeCheckable: true,
          showCheckedStrategy: _index.SHOW_PARENT,
          treeDefaultExpandAll: true,
          treeData: [{ key: '', value: '', label: 'empty value', children: [] }, {
            key: '0',
            value: '0',
            label: '0 label',
            children: [{ key: '00', value: '00', label: '00 label', children: [] }, { key: '01', value: '01', label: '01 label', children: [] }]
          }],

          __propsSymbol__: Symbol()
        },
        on: {
          'change': function change(val) {
            var _console4;

            for (var _len4 = arguments.length, args = Array(_len4 > 1 ? _len4 - 1 : 0), _key4 = 1; _key4 < _len4; _key4++) {
              args[_key4 - 1] = arguments[_key4];
            }

            return (_console4 = console).log.apply(_console4, [val].concat(args));
          }
        }
      }), h('h2', ['use TreeNode Component (not recommend)']), h(
        _index2['default'],
        {
          style: { width: '200px' },
          attrs: { dropdownStyle: { maxHeight: '200px', overflow: 'auto' },
            defaultValue: 'leaf1',
            treeDefaultExpandAll: true,
            treeNodeFilterProp: 'title',
            filterTreeNode: this.filterTreeNode,

            __propsSymbol__: Symbol()
          },
          on: {
            'change': function change(val) {
              var _console5;

              for (var _len5 = arguments.length, args = Array(_len5 > 1 ? _len5 - 1 : 0), _key5 = 1; _key5 < _len5; _key5++) {
                args[_key5 - 1] = arguments[_key5];
              }

              return (_console5 = console).log.apply(_console5, [val].concat(args));
            }
          }
        },
        [h(
          _index.TreeNode,
          {
            attrs: { value: '', title: 'parent 1' },
            key: '' },
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
      )]
    );
  }
};