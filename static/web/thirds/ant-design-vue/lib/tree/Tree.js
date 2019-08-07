'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.TreeProps = undefined;

var _extends2 = require('babel-runtime/helpers/extends');

var _extends3 = _interopRequireDefault(_extends2);

var _objectWithoutProperties2 = require('babel-runtime/helpers/objectWithoutProperties');

var _objectWithoutProperties3 = _interopRequireDefault(_objectWithoutProperties2);

var _warning = require('warning');

var _warning2 = _interopRequireDefault(_warning);

var _vcTree = require('../vc-tree');

var _openAnimation = require('../_util/openAnimation');

var _openAnimation2 = _interopRequireDefault(_openAnimation);

var _vueTypes = require('../_util/vue-types');

var _vueTypes2 = _interopRequireDefault(_vueTypes);

var _propsUtil = require('../_util/props-util');

var _icon = require('../icon');

var _icon2 = _interopRequireDefault(_icon);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

function TreeProps() {
  return {
    showLine: _vueTypes2['default'].bool,
    /** 是否支持多选 */
    multiple: _vueTypes2['default'].bool,
    /** 是否自动展开父节点 */
    autoExpandParent: _vueTypes2['default'].bool,
    /** checkable状态下节点选择完全受控（父子节点选中状态不再关联）*/
    checkStrictly: _vueTypes2['default'].bool,
    /** 是否支持选中 */
    checkable: _vueTypes2['default'].bool,
    /** 是否禁用树 */
    disabled: _vueTypes2['default'].bool,
    /** 默认展开所有树节点 */
    defaultExpandAll: _vueTypes2['default'].bool,
    /** 默认展开对应树节点 */
    defaultExpandParent: _vueTypes2['default'].bool,
    /** 默认展开指定的树节点 */
    defaultExpandedKeys: _vueTypes2['default'].array,
    /** （受控）展开指定的树节点 */
    expandedKeys: _vueTypes2['default'].array,
    /** （受控）选中复选框的树节点 */
    checkedKeys: _vueTypes2['default'].oneOfType([_vueTypes2['default'].array, _vueTypes2['default'].shape({
      checked: _vueTypes2['default'].array,
      halfChecked: _vueTypes2['default'].array
    }).loose]),
    /** 默认选中复选框的树节点 */
    defaultCheckedKeys: _vueTypes2['default'].array,
    /** （受控）设置选中的树节点 */
    selectedKeys: _vueTypes2['default'].array,
    /** 默认选中的树节点 */
    defaultSelectedKeys: _vueTypes2['default'].array,
    selectable: _vueTypes2['default'].bool,
    /** 展开/收起节点时触发 */
    // onExpand: (expandedKeys: string[], info: AntTreeNodeExpandedEvent) => void | PromiseLike<any>,
    /** 点击复选框触发 */
    // onCheck: (checkedKeys: string[] | { checked: string[]; halfChecked: string[] }, e: AntTreeNodeCheckedEvent) => void,
    /** 点击树节点触发 */
    // onSelect: (selectedKeys: string[], e: AntTreeNodeSelectedEvent) => void,
    /** 单击树节点触发 */
    // onClick: (e: React.MouseEvent<HTMLElement>, node: AntTreeNode) => void,
    /** 双击树节点触发 */
    // onDoubleClick: (e: React.MouseEvent<HTMLElement>, node: AntTreeNode) => void,
    /** filter some AntTreeNodes as you need. it should return true */
    filterAntTreeNode: _vueTypes2['default'].func,
    /** 异步加载数据 */
    loadData: _vueTypes2['default'].func,
    loadedKeys: _vueTypes2['default'].array,
    // onLoaded: (loadedKeys: string[], info: { event: 'load', node: AntTreeNode; }) => void,
    /** 响应右键点击 */
    // onRightClick: (options: AntTreeNodeMouseEvent) => void,
    /** 设置节点可拖拽（IE>8）*/
    draggable: _vueTypes2['default'].bool,
    // /** 开始拖拽时调用 */
    // onDragStart: (options: AntTreeNodeMouseEvent) => void,
    // /** dragenter 触发时调用 */
    // onDragEnter: (options: AntTreeNodeMouseEvent) => void,
    // /** dragover 触发时调用 */
    // onDragOver: (options: AntTreeNodeMouseEvent) => void,
    // /** dragleave 触发时调用 */
    // onDragLeave: (options: AntTreeNodeMouseEvent) => void,
    // /** drop 触发时调用 */
    // onDrop: (options: AntTreeNodeMouseEvent) => void,
    showIcon: _vueTypes2['default'].bool,
    icon: _vueTypes2['default'].func,
    prefixCls: _vueTypes2['default'].string,
    filterTreeNode: _vueTypes2['default'].func,
    openAnimation: _vueTypes2['default'].any,
    treeNodes: _vueTypes2['default'].array,
    treeData: _vueTypes2['default'].array
  };
}

exports.TreeProps = TreeProps;
exports['default'] = {
  name: 'ATree',
  model: {
    prop: 'checkedKeys',
    event: 'check'
  },
  props: (0, _propsUtil.initDefaultProps)(TreeProps(), {
    prefixCls: 'ant-tree',
    checkable: false,
    showIcon: false,
    openAnimation: {
      on: _openAnimation2['default'],
      props: { appear: null }
    }
  }),
  created: function created() {
    (0, _warning2['default'])(!('treeNodes' in (0, _propsUtil.getOptionProps)(this)), '`treeNodes` is deprecated. please use treeData instead.');
  },

  TreeNode: _vcTree.TreeNode,
  methods: {
    renderSwitcherIcon: function renderSwitcherIcon(_ref) {
      var isLeaf = _ref.isLeaf,
          expanded = _ref.expanded,
          loading = _ref.loading;
      var h = this.$createElement;
      var _$props = this.$props,
          prefixCls = _$props.prefixCls,
          showLine = _$props.showLine;

      if (loading) {
        return h(_icon2['default'], {
          attrs: { type: 'loading' },
          'class': prefixCls + '-switcher-loading-icon' });
      }
      if (showLine) {
        if (isLeaf) {
          return h(_icon2['default'], {
            attrs: { type: 'file' },
            'class': prefixCls + '-switcher-line-icon' });
        }
        return h(_icon2['default'], {
          attrs: {
            type: expanded ? 'minus-square' : 'plus-square',

            theme: 'outlined'
          },
          'class': prefixCls + '-switcher-line-icon' });
      } else {
        if (isLeaf) {
          return null;
        }
        return h(_icon2['default'], {
          attrs: { type: 'caret-down', theme: 'filled' },
          'class': prefixCls + '-switcher-icon' });
      }
    },
    updateTreeData: function updateTreeData(treeData) {
      var _this = this;

      var $slots = this.$slots,
          $scopedSlots = this.$scopedSlots;

      return treeData.map(function (item) {
        var children = item.children,
            _item$on = item.on,
            on = _item$on === undefined ? {} : _item$on,
            _item$slots = item.slots,
            slots = _item$slots === undefined ? {} : _item$slots,
            _item$scopedSlots = item.scopedSlots,
            scopedSlots = _item$scopedSlots === undefined ? {} : _item$scopedSlots,
            key = item.key,
            cls = item['class'],
            style = item.style,
            restProps = (0, _objectWithoutProperties3['default'])(item, ['children', 'on', 'slots', 'scopedSlots', 'key', 'class', 'style']);

        var treeNodeProps = (0, _extends3['default'])({}, restProps, {
          icon: $slots[slots.icon] || $scopedSlots[scopedSlots.icon] && $scopedSlots[scopedSlots.icon] || restProps.icon,
          title: $slots[slots.title] || $scopedSlots[scopedSlots.title] && $scopedSlots[scopedSlots.title](item) || restProps.title,
          dataRef: item,
          on: on,
          key: key,
          'class': cls,
          style: style
        });
        if (children) {
          return (0, _extends3['default'])({}, treeNodeProps, { children: _this.updateTreeData(children) });
        }
        return treeNodeProps;
      });
    }
  },
  render: function render() {
    var h = arguments[0];

    var props = (0, _propsUtil.getOptionProps)(this);
    var prefixCls = props.prefixCls,
        showIcon = props.showIcon,
        treeNodes = props.treeNodes;

    var checkable = props.checkable;
    var treeData = props.treeData || treeNodes;
    if (treeData) {
      treeData = this.updateTreeData(treeData);
    }
    var vcTreeProps = {
      props: (0, _extends3['default'])({}, props, {
        checkable: checkable ? h('span', { 'class': prefixCls + '-checkbox-inner' }) : checkable,
        children: (0, _propsUtil.filterEmpty)(this.$slots['default'] || []),
        __propsSymbol__: Symbol(),
        switcherIcon: this.renderSwitcherIcon
      }),
      on: this.$listeners,
      ref: 'tree',
      'class': !showIcon && prefixCls + '-icon-hide'
    };
    if (treeData) {
      vcTreeProps.props.treeData = treeData;
    }
    return h(_vcTree.Tree, vcTreeProps);
  }
};