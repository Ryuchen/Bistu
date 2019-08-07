'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _defineProperty2 = require('babel-runtime/helpers/defineProperty');

var _defineProperty3 = _interopRequireDefault(_defineProperty2);

var _extends2 = require('babel-runtime/helpers/extends');

var _extends3 = _interopRequireDefault(_extends2);

var _vcMenu = require('../vc-menu');

var _vcMenu2 = _interopRequireDefault(_vcMenu);

var _domClosest = require('dom-closest');

var _domClosest2 = _interopRequireDefault(_domClosest);

var _classnames = require('classnames');

var _classnames2 = _interopRequireDefault(_classnames);

var _shallowequal = require('shallowequal');

var _shallowequal2 = _interopRequireDefault(_shallowequal);

var _dropdown = require('../dropdown');

var _dropdown2 = _interopRequireDefault(_dropdown);

var _icon = require('../icon');

var _icon2 = _interopRequireDefault(_icon);

var _checkbox = require('../checkbox');

var _checkbox2 = _interopRequireDefault(_checkbox);

var _radio = require('../radio');

var _radio2 = _interopRequireDefault(_radio);

var _FilterDropdownMenuWrapper = require('./FilterDropdownMenuWrapper');

var _FilterDropdownMenuWrapper2 = _interopRequireDefault(_FilterDropdownMenuWrapper);

var _interface = require('./interface');

var _propsUtil = require('../_util/props-util');

var _vnode = require('../_util/vnode');

var _BaseMixin = require('../_util/BaseMixin');

var _BaseMixin2 = _interopRequireDefault(_BaseMixin);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

function stopPropagation(e) {
  e.stopPropagation();
}

exports['default'] = {
  name: 'FilterMenu',
  mixins: [_BaseMixin2['default']],
  props: (0, _propsUtil.initDefaultProps)(_interface.FilterMenuProps, {
    handleFilter: function handleFilter() {},

    column: {}
  }),

  data: function data() {
    var visible = 'filterDropdownVisible' in this.column ? this.column.filterDropdownVisible : false;
    this.preProps = (0, _extends3['default'])({}, (0, _propsUtil.getOptionProps)(this));
    return {
      sSelectedKeys: this.selectedKeys,
      sKeyPathOfSelectedItem: {}, // 记录所有有选中子菜单的祖先菜单
      sVisible: visible
    };
  },

  watch: {
    _propsSymbol: function _propsSymbol() {
      var nextProps = (0, _propsUtil.getOptionProps)(this);
      var column = nextProps.column;

      this.setNeverShown(column);
      var newState = {};

      /**
       * if the state is visible the component should ignore updates on selectedKeys prop to avoid
       * that the user selection is lost
       * this happens frequently when a table is connected on some sort of realtime data
       * Fixes https://github.com/ant-design/ant-design/issues/10289 and
       * https://github.com/ant-design/ant-design/issues/10209
       */
      if ('selectedKeys' in nextProps && !(0, _shallowequal2['default'])(this.preProps.selectedKeys, nextProps.selectedKeys)) {
        newState.sSelectedKeys = nextProps.selectedKeys;
      }
      if ('filterDropdownVisible' in column) {
        newState.sVisible = column.filterDropdownVisible;
      }
      if (Object.keys(newState).length > 0) {
        this.setState(newState);
      }
      this.preProps = (0, _extends3['default'])({}, nextProps);
    }
  },

  mounted: function mounted() {
    var _this = this;

    var column = this.column;

    this.$nextTick(function () {
      _this.setNeverShown(column);
    });
  },

  methods: {
    getDropdownVisible: function getDropdownVisible() {
      return this.neverShown ? false : this.sVisible;
    },
    setNeverShown: function setNeverShown(column) {
      var rootNode = this.$el;
      var filterBelongToScrollBody = !!(0, _domClosest2['default'])(rootNode, '.ant-table-scroll');
      if (filterBelongToScrollBody) {
        // When fixed column have filters, there will be two dropdown menus
        // Filter dropdown menu inside scroll body should never be shown
        // To fix https://github.com/ant-design/ant-design/issues/5010 and
        // https://github.com/ant-design/ant-design/issues/7909
        this.neverShown = !!column.fixed;
      }
    },
    setSelectedKeys: function setSelectedKeys(_ref) {
      var selectedKeys = _ref.selectedKeys;

      this.setState({ sSelectedKeys: selectedKeys });
    },
    setVisible: function setVisible(visible) {
      var column = this.column;

      if (!('filterDropdownVisible' in column)) {
        this.setState({ sVisible: visible });
      }
      if (column.onFilterDropdownVisibleChange) {
        column.onFilterDropdownVisibleChange(visible);
      }
    },
    handleClearFilters: function handleClearFilters() {
      this.setState({
        sSelectedKeys: []
      }, this.handleConfirm);
    },
    handleConfirm: function handleConfirm() {
      var _this2 = this;

      this.setVisible(false);
      this.confirmFilter2();
      // Call `setSelectedKeys` & `confirm` in the same time will make filter data not up to date
      // https://github.com/ant-design/ant-design/issues/12284
      this.$forceUpdate();
      this.$nextTick(function () {
        _this2.confirmFilter;
      });
    },
    onVisibleChange: function onVisibleChange(visible) {
      this.setVisible(visible);
      if (!visible) {
        this.confirmFilter2();
      }
    },
    confirmFilter2: function confirmFilter2() {
      if (!(0, _shallowequal2['default'])(this.sSelectedKeys, this.selectedKeys)) {
        this.confirmFilter(this.column, this.sSelectedKeys);
      }
    },
    renderMenuItem: function renderMenuItem(item) {
      var h = this.$createElement;
      var column = this.column;
      var selectedKeys = this.$data.sSelectedKeys;

      var multiple = 'filterMultiple' in column ? column.filterMultiple : true;
      var input = multiple ? h(_checkbox2['default'], {
        attrs: { checked: selectedKeys && selectedKeys.indexOf(item.value.toString()) >= 0 }
      }) : h(_radio2['default'], {
        attrs: { checked: selectedKeys && selectedKeys.indexOf(item.value.toString()) >= 0 }
      });

      return h(
        _vcMenu.Item,
        { key: item.value },
        [input, h('span', [item.text])]
      );
    },
    hasSubMenu: function hasSubMenu() {
      var _column$filters = this.column.filters,
          filters = _column$filters === undefined ? [] : _column$filters;

      return filters.some(function (item) {
        return !!(item.children && item.children.length > 0);
      });
    },
    renderMenus: function renderMenus(items) {
      var _this3 = this;

      var h = this.$createElement;

      return items.map(function (item) {
        if (item.children && item.children.length > 0) {
          var sKeyPathOfSelectedItem = _this3.sKeyPathOfSelectedItem;

          var containSelected = Object.keys(sKeyPathOfSelectedItem).some(function (key) {
            return sKeyPathOfSelectedItem[key].indexOf(item.value) >= 0;
          });
          var subMenuCls = containSelected ? _this3.dropdownPrefixCls + '-submenu-contain-selected' : '';
          return h(
            _vcMenu.SubMenu,
            {
              attrs: { title: item.text },
              'class': subMenuCls, key: item.value.toString() },
            [_this3.renderMenus(item.children)]
          );
        }
        return _this3.renderMenuItem(item);
      });
    },
    handleMenuItemClick: function handleMenuItemClick(info) {
      var selectedKeys = this.$data.sSelectedKeys;

      if (!info.keyPath || info.keyPath.length <= 1) {
        return;
      }
      var keyPathOfSelectedItem = this.sKeyPathOfSelectedItem;
      if (selectedKeys && selectedKeys.indexOf(info.key) >= 0) {
        // deselect SubMenu child
        delete keyPathOfSelectedItem[info.key];
      } else {
        // select SubMenu child
        keyPathOfSelectedItem[info.key] = info.keyPath;
      }
      this.setState({ keyPathOfSelectedItem: keyPathOfSelectedItem });
    },
    renderFilterIcon: function renderFilterIcon() {
      var _classNames;

      var h = this.$createElement;
      var column = this.column,
          locale = this.locale,
          prefixCls = this.prefixCls,
          selectedKeys = this.selectedKeys;

      var filtered = selectedKeys && selectedKeys.length > 0;
      var filterIcon = column.filterIcon;
      if (typeof filterIcon === 'function') {
        filterIcon = filterIcon(filtered, column);
      }
      var dropdownIconClass = (0, _classnames2['default'])((_classNames = {}, (0, _defineProperty3['default'])(_classNames, prefixCls + '-selected', filtered), (0, _defineProperty3['default'])(_classNames, prefixCls + '-open', this.getDropdownVisible()), _classNames));

      return filterIcon ? (0, _vnode.cloneElement)(filterIcon, {
        attrs: {
          title: locale.filterTitle
        },
        on: {
          click: stopPropagation
        },
        'class': (0, _classnames2['default'])(prefixCls + '-icon', dropdownIconClass)
      }) : h(_icon2['default'], {
        attrs: {
          title: locale.filterTitle,
          type: 'filter',
          theme: 'filled'
        },
        'class': dropdownIconClass,
        on: {
          'click': stopPropagation
        }
      });
    }
  },

  render: function render() {
    var _this4 = this;

    var h = arguments[0];
    var column = this.column,
        locale = this.locale,
        prefixCls = this.prefixCls,
        dropdownPrefixCls = this.dropdownPrefixCls,
        getPopupContainer = this.getPopupContainer;
    // default multiple selection in filter dropdown

    var multiple = 'filterMultiple' in column ? column.filterMultiple : true;
    var dropdownMenuClass = (0, _classnames2['default'])((0, _defineProperty3['default'])({}, dropdownPrefixCls + '-menu-without-submenu', !this.hasSubMenu()));
    var filterDropdown = column.filterDropdown;

    if (filterDropdown instanceof Function) {
      filterDropdown = filterDropdown({
        prefixCls: dropdownPrefixCls + '-custom',
        setSelectedKeys: function setSelectedKeys(selectedKeys) {
          return _this4.setSelectedKeys({ selectedKeys: selectedKeys });
        },
        selectedKeys: this.sSelectedKeys,
        confirm: this.handleConfirm,
        clearFilters: this.handleClearFilters,
        filters: column.filters,
        getPopupContainer: function getPopupContainer(triggerNode) {
          return triggerNode.parentNode;
        },
        column: column
      });
    }

    var menus = filterDropdown ? h(_FilterDropdownMenuWrapper2['default'], [filterDropdown]) : h(
      _FilterDropdownMenuWrapper2['default'],
      { 'class': prefixCls + '-dropdown' },
      [h(
        _vcMenu2['default'],
        {
          attrs: {
            multiple: multiple,

            prefixCls: dropdownPrefixCls + '-menu',

            selectedKeys: this.sSelectedKeys,
            getPopupContainer: function getPopupContainer(triggerNode) {
              return triggerNode.parentNode;
            }
          },
          on: {
            'click': this.handleMenuItemClick,
            'select': this.setSelectedKeys,
            'deselect': this.setSelectedKeys
          },
          'class': dropdownMenuClass
        },
        [this.renderMenus(column.filters)]
      ), h(
        'div',
        { 'class': prefixCls + '-dropdown-btns' },
        [h(
          'a',
          { 'class': prefixCls + '-dropdown-link confirm', on: {
              'click': this.handleConfirm
            }
          },
          [locale.filterConfirm]
        ), h(
          'a',
          { 'class': prefixCls + '-dropdown-link clear', on: {
              'click': this.handleClearFilters
            }
          },
          [locale.filterReset]
        )]
      )]
    );

    return h(
      _dropdown2['default'],
      {
        attrs: {
          trigger: ['click'],
          placement: 'bottomRight',
          visible: this.getDropdownVisible(),

          getPopupContainer: getPopupContainer,
          forceRender: true
        },
        on: {
          'visibleChange': this.onVisibleChange
        }
      },
      [h(
        'template',
        { slot: 'overlay' },
        [menus]
      ), this.renderFilterIcon()]
    );
  }
};