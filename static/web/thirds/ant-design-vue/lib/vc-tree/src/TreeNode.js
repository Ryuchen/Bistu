'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _defineProperty2 = require('babel-runtime/helpers/defineProperty');

var _defineProperty3 = _interopRequireDefault(_defineProperty2);

var _typeof2 = require('babel-runtime/helpers/typeof');

var _typeof3 = _interopRequireDefault(_typeof2);

var _extends2 = require('babel-runtime/helpers/extends');

var _extends3 = _interopRequireDefault(_extends2);

var _vueTypes = require('../../_util/vue-types');

var _vueTypes2 = _interopRequireDefault(_vueTypes);

var _classnames = require('classnames');

var _classnames2 = _interopRequireDefault(_classnames);

var _util = require('./util');

var _propsUtil = require('../../_util/props-util');

var _BaseMixin = require('../../_util/BaseMixin');

var _BaseMixin2 = _interopRequireDefault(_BaseMixin);

var _getTransitionProps = require('../../_util/getTransitionProps');

var _getTransitionProps2 = _interopRequireDefault(_getTransitionProps);

var _vnode = require('../../_util/vnode');

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

function noop() {}
var ICON_OPEN = 'open';
var ICON_CLOSE = 'close';

var defaultTitle = '---';

var TreeNode = {
  name: 'TreeNode',
  mixins: [_BaseMixin2['default']],
  __ANT_TREE_NODE: true,
  props: (0, _propsUtil.initDefaultProps)({
    eventKey: _vueTypes2['default'].oneOfType([_vueTypes2['default'].string, _vueTypes2['default'].number]), // Pass by parent `cloneElement`
    prefixCls: _vueTypes2['default'].string,
    // className: PropTypes.string,
    root: _vueTypes2['default'].object,
    // onSelect: PropTypes.func,

    // By parent
    expanded: _vueTypes2['default'].bool,
    selected: _vueTypes2['default'].bool,
    checked: _vueTypes2['default'].bool,
    loaded: _vueTypes2['default'].bool,
    loading: _vueTypes2['default'].bool,
    halfChecked: _vueTypes2['default'].bool,
    title: _vueTypes2['default'].any,
    pos: _vueTypes2['default'].string,
    dragOver: _vueTypes2['default'].bool,
    dragOverGapTop: _vueTypes2['default'].bool,
    dragOverGapBottom: _vueTypes2['default'].bool,

    // By user
    isLeaf: _vueTypes2['default'].bool,
    selectable: _vueTypes2['default'].bool,
    disabled: _vueTypes2['default'].bool,
    disableCheckbox: _vueTypes2['default'].bool,
    icon: _vueTypes2['default'].any,
    dataRef: _vueTypes2['default'].object,
    switcherIcon: _vueTypes2['default'].any,

    label: _vueTypes2['default'].any,
    value: _vueTypes2['default'].any
  }, {}),

  data: function data() {
    return {
      dragNodeHighlight: false
    };
  },

  inject: {
    vcTree: { 'default': function _default() {
        return {};
      } },
    vcTreeNode: { 'default': function _default() {
        return {};
      } }
  },
  provide: function provide() {
    return {
      vcTreeNode: this
    };
  },


  // Isomorphic needn't load data in server side
  mounted: function mounted() {
    this.syncLoadData(this.$props);
  },
  updated: function updated() {
    this.syncLoadData(this.$props);
  },


  methods: {
    onSelectorClick: function onSelectorClick(e) {
      // Click trigger before select/check operation
      var onNodeClick = this.vcTree.onNodeClick;

      onNodeClick(e, this);
      if (this.isSelectable()) {
        this.onSelect(e);
      } else {
        this.onCheck(e);
      }
    },
    onSelectorDoubleClick: function onSelectorDoubleClick(e) {
      var onNodeDoubleClick = this.vcTree.onNodeDoubleClick;

      onNodeDoubleClick(e, this);
    },
    onSelect: function onSelect(e) {
      if (this.isDisabled()) return;

      var onNodeSelect = this.vcTree.onNodeSelect;

      e.preventDefault();
      onNodeSelect(e, this);
    },
    onCheck: function onCheck(e) {
      if (this.isDisabled()) return;

      var disableCheckbox = this.disableCheckbox,
          checked = this.checked;
      var _vcTree = this.vcTree,
          checkable = _vcTree.checkable,
          onNodeCheck = _vcTree.onNodeCheck;


      if (!checkable || disableCheckbox) return;

      e.preventDefault();
      var targetChecked = !checked;
      onNodeCheck(e, this, targetChecked);
    },
    onMouseEnter: function onMouseEnter(e) {
      var onNodeMouseEnter = this.vcTree.onNodeMouseEnter;

      onNodeMouseEnter(e, this);
    },
    onMouseLeave: function onMouseLeave(e) {
      var onNodeMouseLeave = this.vcTree.onNodeMouseLeave;

      onNodeMouseLeave(e, this);
    },
    onContextMenu: function onContextMenu(e) {
      var onNodeContextMenu = this.vcTree.onNodeContextMenu;

      onNodeContextMenu(e, this);
    },
    onDragStart: function onDragStart(e) {
      var onNodeDragStart = this.vcTree.onNodeDragStart;


      e.stopPropagation();
      this.setState({
        dragNodeHighlight: true
      });
      onNodeDragStart(e, this);

      try {
        // ie throw error
        // firefox-need-it
        e.dataTransfer.setData('text/plain', '');
      } catch (error) {
        // empty
      }
    },
    onDragEnter: function onDragEnter(e) {
      var onNodeDragEnter = this.vcTree.onNodeDragEnter;


      e.preventDefault();
      e.stopPropagation();
      onNodeDragEnter(e, this);
    },
    onDragOver: function onDragOver(e) {
      var onNodeDragOver = this.vcTree.onNodeDragOver;


      e.preventDefault();
      e.stopPropagation();
      onNodeDragOver(e, this);
    },
    onDragLeave: function onDragLeave(e) {
      var onNodeDragLeave = this.vcTree.onNodeDragLeave;


      e.stopPropagation();
      onNodeDragLeave(e, this);
    },
    onDragEnd: function onDragEnd(e) {
      var onNodeDragEnd = this.vcTree.onNodeDragEnd;


      e.stopPropagation();
      this.setState({
        dragNodeHighlight: false
      });
      onNodeDragEnd(e, this);
    },
    onDrop: function onDrop(e) {
      var onNodeDrop = this.vcTree.onNodeDrop;


      e.preventDefault();
      e.stopPropagation();
      this.setState({
        dragNodeHighlight: false
      });
      onNodeDrop(e, this);
    },


    // Disabled item still can be switch
    onExpand: function onExpand(e) {
      var onNodeExpand = this.vcTree.onNodeExpand;

      onNodeExpand(e, this);
    },
    getNodeChildren: function getNodeChildren() {
      var children = this.$slots['default'];

      var originList = (0, _propsUtil.filterEmpty)(children);
      var targetList = (0, _util.getNodeChildren)(originList);

      if (originList.length !== targetList.length) {
        (0, _util.warnOnlyTreeNode)();
      }

      return targetList;
    },
    getNodeState: function getNodeState() {
      var expanded = this.expanded;


      if (this.isLeaf2()) {
        return null;
      }

      return expanded ? ICON_OPEN : ICON_CLOSE;
    },
    isLeaf2: function isLeaf2() {
      var isLeaf = this.isLeaf,
          loaded = this.loaded;
      var loadData = this.vcTree.loadData;


      var hasChildren = this.getNodeChildren().length !== 0;
      if (isLeaf === false) {
        return false;
      }
      return isLeaf || !loadData && !hasChildren || loadData && loaded && !hasChildren;
    },
    isDisabled: function isDisabled() {
      var disabled = this.disabled;
      var treeDisabled = this.vcTree.disabled;

      // Follow the logic of Selectable

      if (disabled === false) {
        return false;
      }

      return !!(treeDisabled || disabled);
    },
    isSelectable: function isSelectable() {
      var selectable = this.selectable;
      var treeSelectable = this.vcTree.selectable;

      // Ignore when selectable is undefined or null

      if (typeof selectable === 'boolean') {
        return selectable;
      }

      return treeSelectable;
    },


    // Load data to avoid default expanded tree without data
    syncLoadData: function syncLoadData(props) {
      var expanded = props.expanded,
          loading = props.loading,
          loaded = props.loaded;
      var _vcTree2 = this.vcTree,
          loadData = _vcTree2.loadData,
          onNodeLoad = _vcTree2.onNodeLoad;

      if (loading) return;
      // read from state to avoid loadData at same time
      if (loadData && expanded && !this.isLeaf2()) {
        // We needn't reload data when has children in sync logic
        // It's only needed in node expanded
        var hasChildren = this.getNodeChildren().length !== 0;
        if (!hasChildren && !loaded) {
          onNodeLoad(this);
        }
      }
    },


    // Switcher
    renderSwitcher: function renderSwitcher() {
      var h = this.$createElement;
      var expanded = this.expanded;
      var prefixCls = this.vcTree.prefixCls;

      var switcherIcon = (0, _propsUtil.getComponentFromProp)(this, 'switcherIcon', {}, false) || (0, _propsUtil.getComponentFromProp)(this.vcTree, 'switcherIcon', {}, false);
      if (this.isLeaf2()) {
        return h(
          'span',
          {
            key: 'switcher',
            'class': (0, _classnames2['default'])(prefixCls + '-switcher', prefixCls + '-switcher-noop')
          },
          [typeof switcherIcon === 'function' ? (0, _vnode.cloneElement)(switcherIcon((0, _extends3['default'])({}, this.$props, { isLeaf: true }))) : switcherIcon]
        );
      }

      var switcherCls = (0, _classnames2['default'])(prefixCls + '-switcher', prefixCls + '-switcher_' + (expanded ? ICON_OPEN : ICON_CLOSE));
      return h(
        'span',
        { key: 'switcher', on: {
            'click': this.onExpand
          },
          'class': switcherCls },
        [typeof switcherIcon === 'function' ? (0, _vnode.cloneElement)(switcherIcon((0, _extends3['default'])({}, this.$props, { isLeaf: false }))) : switcherIcon]
      );
    },


    // Checkbox
    renderCheckbox: function renderCheckbox() {
      var h = this.$createElement;
      var checked = this.checked,
          halfChecked = this.halfChecked,
          disableCheckbox = this.disableCheckbox;
      var _vcTree3 = this.vcTree,
          prefixCls = _vcTree3.prefixCls,
          checkable = _vcTree3.checkable;

      var disabled = this.isDisabled();

      if (!checkable) return null;

      // [Legacy] Custom element should be separate with `checkable` in future
      var $custom = typeof checkable !== 'boolean' ? checkable : null;

      return h(
        'span',
        {
          key: 'checkbox',
          'class': (0, _classnames2['default'])(prefixCls + '-checkbox', checked && prefixCls + '-checkbox-checked', !checked && halfChecked && prefixCls + '-checkbox-indeterminate', (disabled || disableCheckbox) && prefixCls + '-checkbox-disabled'),
          on: {
            'click': this.onCheck
          }
        },
        [$custom]
      );
    },
    renderIcon: function renderIcon() {
      var h = this.$createElement;
      var loading = this.loading;
      var prefixCls = this.vcTree.prefixCls;


      return h('span', {
        key: 'icon',
        'class': (0, _classnames2['default'])(prefixCls + '-iconEle', prefixCls + '-icon__' + (this.getNodeState() || 'docu'), loading && prefixCls + '-icon_loading')
      });
    },


    // Icon + Title
    renderSelector: function renderSelector(h) {
      var selected = this.selected,
          icon = this.icon,
          loading = this.loading,
          dragNodeHighlight = this.dragNodeHighlight;
      var _vcTree4 = this.vcTree,
          prefixCls = _vcTree4.prefixCls,
          showIcon = _vcTree4.showIcon,
          treeIcon = _vcTree4.icon,
          draggable = _vcTree4.draggable,
          loadData = _vcTree4.loadData;

      var disabled = this.isDisabled();
      var title = (0, _propsUtil.getComponentFromProp)(this, 'title') || defaultTitle;
      var wrapClass = prefixCls + '-node-content-wrapper';

      // Icon - Still show loading icon when loading without showIcon
      var $icon = void 0;

      if (showIcon) {
        var currentIcon = icon || treeIcon;
        $icon = currentIcon ? h(
          'span',
          { 'class': (0, _classnames2['default'])(prefixCls + '-iconEle', prefixCls + '-icon__customize') },
          [typeof currentIcon === 'function' ? currentIcon((0, _extends3['default'])({}, this.$props), h) : currentIcon]
        ) : this.renderIcon();
      } else if (loadData && loading) {
        $icon = this.renderIcon();
      }

      // Title
      var $title = h(
        'span',
        { 'class': prefixCls + '-title' },
        [title]
      );

      return h(
        'span',
        {
          key: 'selector',
          ref: 'selectHandle',
          attrs: { title: typeof title === 'string' ? title : '',

            draggable: !disabled && draggable || undefined,
            'aria-grabbed': !disabled && draggable || undefined
          },
          'class': (0, _classnames2['default'])('' + wrapClass, wrapClass + '-' + (this.getNodeState() || 'normal'), !disabled && (selected || dragNodeHighlight) && prefixCls + '-node-selected', !disabled && draggable && 'draggable'), on: {
            'mouseenter': this.onMouseEnter,
            'mouseleave': this.onMouseLeave,
            'contextmenu': this.onContextMenu,
            'click': this.onSelectorClick,
            'dblclick': this.onSelectorDoubleClick,
            'dragstart': draggable ? this.onDragStart : noop
          }
        },
        [$icon, $title]
      );
    },


    // Children list wrapped with `Animation`
    renderChildren: function renderChildren() {
      var h = this.$createElement;
      var expanded = this.expanded,
          pos = this.pos;
      var _vcTree5 = this.vcTree,
          prefixCls = _vcTree5.prefixCls,
          openTransitionName = _vcTree5.openTransitionName,
          openAnimation = _vcTree5.openAnimation,
          renderTreeNode = _vcTree5.renderTreeNode;


      var animProps = {};
      if (openTransitionName) {
        animProps = (0, _getTransitionProps2['default'])(openTransitionName);
      } else if ((typeof openAnimation === 'undefined' ? 'undefined' : (0, _typeof3['default'])(openAnimation)) === 'object') {
        animProps = (0, _extends3['default'])({}, openAnimation);
        animProps.props = (0, _extends3['default'])({ css: false }, animProps.props);
      }

      // Children TreeNode
      var nodeList = this.getNodeChildren();

      if (nodeList.length === 0) {
        return null;
      }

      var $children = void 0;
      if (expanded) {
        $children = h(
          'ul',
          {
            'class': (0, _classnames2['default'])(prefixCls + '-child-tree', expanded && prefixCls + '-child-tree-open'),
            attrs: { 'data-expanded': expanded,
              role: 'group'
            }
          },
          [(0, _util.mapChildren)(nodeList, function (node, index) {
            return renderTreeNode(node, index, pos);
          })]
        );
      }

      return h(
        'transition',
        animProps,
        [$children]
      );
    }
  },

  render: function render(h) {
    var _ref;

    var _$props = this.$props,
        dragOver = _$props.dragOver,
        dragOverGapTop = _$props.dragOverGapTop,
        dragOverGapBottom = _$props.dragOverGapBottom,
        isLeaf = _$props.isLeaf,
        expanded = _$props.expanded,
        selected = _$props.selected,
        checked = _$props.checked,
        halfChecked = _$props.halfChecked,
        loading = _$props.loading;
    var _vcTree6 = this.vcTree,
        prefixCls = _vcTree6.prefixCls,
        filterTreeNode = _vcTree6.filterTreeNode,
        draggable = _vcTree6.draggable;

    var disabled = this.isDisabled();
    return h(
      'li',
      {
        'class': (_ref = {}, (0, _defineProperty3['default'])(_ref, prefixCls + '-treenode-disabled', disabled), (0, _defineProperty3['default'])(_ref, prefixCls + '-treenode-switcher-' + (expanded ? 'open' : 'close'), !isLeaf), (0, _defineProperty3['default'])(_ref, prefixCls + '-treenode-checkbox-checked', checked), (0, _defineProperty3['default'])(_ref, prefixCls + '-treenode-checkbox-indeterminate', halfChecked), (0, _defineProperty3['default'])(_ref, prefixCls + '-treenode-selected', selected), (0, _defineProperty3['default'])(_ref, prefixCls + '-treenode-loading', loading), (0, _defineProperty3['default'])(_ref, 'drag-over', !disabled && dragOver), (0, _defineProperty3['default'])(_ref, 'drag-over-gap-top', !disabled && dragOverGapTop), (0, _defineProperty3['default'])(_ref, 'drag-over-gap-bottom', !disabled && dragOverGapBottom), (0, _defineProperty3['default'])(_ref, 'filter-node', filterTreeNode && filterTreeNode(this)), _ref),
        attrs: { role: 'treeitem'
        },
        on: {
          'dragenter': draggable ? this.onDragEnter : noop,
          'dragover': draggable ? this.onDragOver : noop,
          'dragleave': draggable ? this.onDragLeave : noop,
          'drop': draggable ? this.onDrop : noop,
          'dragend': draggable ? this.onDragEnd : noop
        }
      },
      [this.renderSwitcher(), this.renderCheckbox(), this.renderSelector(h), this.renderChildren()]
    );
  }
};

TreeNode.isTreeNode = 1;

exports['default'] = TreeNode;