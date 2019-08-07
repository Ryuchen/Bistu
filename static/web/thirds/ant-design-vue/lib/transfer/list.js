'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.TransferListProps = undefined;

var _babelHelperVueJsxMergeProps = require('babel-helper-vue-jsx-merge-props');

var _babelHelperVueJsxMergeProps2 = _interopRequireDefault(_babelHelperVueJsxMergeProps);

var _defineProperty2 = require('babel-runtime/helpers/defineProperty');

var _defineProperty3 = _interopRequireDefault(_defineProperty2);

var _extends2 = require('babel-runtime/helpers/extends');

var _extends3 = _interopRequireDefault(_extends2);

var _classnames = require('classnames');

var _classnames2 = _interopRequireDefault(_classnames);

var _vueTypes = require('../_util/vue-types');

var _vueTypes2 = _interopRequireDefault(_vueTypes);

var _propsUtil = require('../_util/props-util');

var _BaseMixin = require('../_util/BaseMixin');

var _BaseMixin2 = _interopRequireDefault(_BaseMixin);

var _getTransitionProps = require('../_util/getTransitionProps');

var _getTransitionProps2 = _interopRequireDefault(_getTransitionProps);

var _checkbox = require('../checkbox');

var _checkbox2 = _interopRequireDefault(_checkbox);

var _search = require('./search');

var _search2 = _interopRequireDefault(_search);

var _item = require('./item');

var _item2 = _interopRequireDefault(_item);

var _triggerEvent = require('../_util/triggerEvent');

var _triggerEvent2 = _interopRequireDefault(_triggerEvent);

var _addEventListener = require('../_util/Dom/addEventListener');

var _addEventListener2 = _interopRequireDefault(_addEventListener);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

function noop() {}

var TransferItem = {
  key: _vueTypes2['default'].string.isRequired,
  title: _vueTypes2['default'].string.isRequired,
  description: _vueTypes2['default'].string,
  disabled: _vueTypes2['default'].bool
};

function isRenderResultPlainObject(result) {
  return result && !(0, _propsUtil.isValidElement)(result) && Object.prototype.toString.call(result) === '[object Object]';
}

var TransferListProps = exports.TransferListProps = {
  prefixCls: _vueTypes2['default'].string,
  titleText: _vueTypes2['default'].string,
  dataSource: _vueTypes2['default'].arrayOf(_vueTypes2['default'].shape(TransferItem).loose),
  filter: _vueTypes2['default'].string,
  filterOption: _vueTypes2['default'].func,
  checkedKeys: _vueTypes2['default'].arrayOf(_vueTypes2['default'].string),
  handleFilter: _vueTypes2['default'].func,
  handleSelect: _vueTypes2['default'].func,
  handleSelectAll: _vueTypes2['default'].func,
  handleClear: _vueTypes2['default'].func,
  renderItem: _vueTypes2['default'].func,
  showSearch: _vueTypes2['default'].bool,
  searchPlaceholder: _vueTypes2['default'].string,
  notFoundContent: _vueTypes2['default'].any,
  itemUnit: _vueTypes2['default'].string,
  itemsUnit: _vueTypes2['default'].string,
  body: _vueTypes2['default'].any,
  footer: _vueTypes2['default'].any,
  lazy: _vueTypes2['default'].oneOfType([_vueTypes2['default'].bool, _vueTypes2['default'].object]),
  disabled: _vueTypes2['default'].bool
};

exports['default'] = {
  name: 'TransferList',
  mixins: [_BaseMixin2['default']],
  props: (0, _propsUtil.initDefaultProps)(TransferListProps, {
    dataSource: [],
    titleText: '',
    showSearch: false,
    renderItem: noop,
    lazy: {}
  }),
  data: function data() {
    this.timer = null;
    this.triggerScrollTimer = null;
    return {
      mounted: false
    };
  },
  mounted: function mounted() {
    var _this = this;

    this.timer = setTimeout(function () {
      _this.setState({
        mounted: true
      });
    }, 0);
    this.$nextTick(function () {
      if (_this.$refs.listContentWrapper) {
        var listContentWrapperDom = _this.$refs.listContentWrapper.$el;
        _this.scrollEvent = (0, _addEventListener2['default'])(listContentWrapperDom, 'scroll', _this.handleScroll);
      }
    });
  },
  beforeDestroy: function beforeDestroy() {
    clearTimeout(this.timer);
    clearTimeout(this.triggerScrollTimer);
    if (this.scrollEvent) {
      this.scrollEvent.remove();
    }
  },
  updated: function updated() {
    var _this2 = this;

    this.$nextTick(function () {
      if (_this2.scrollEvent) {
        _this2.scrollEvent.remove();
      }
      if (_this2.$refs.listContentWrapper) {
        var listContentWrapperDom = _this2.$refs.listContentWrapper.$el;
        _this2.scrollEvent = (0, _addEventListener2['default'])(listContentWrapperDom, 'scroll', _this2.handleScroll);
      }
    });
  },

  methods: {
    handleScroll: function handleScroll(e) {
      this.$emit('scroll', e);
    },
    getCheckStatus: function getCheckStatus(filteredDataSource) {
      var checkedKeys = this.$props.checkedKeys;

      if (checkedKeys.length === 0) {
        return 'none';
      } else if (filteredDataSource.every(function (item) {
        return checkedKeys.indexOf(item.key) >= 0;
      })) {
        return 'all';
      }
      return 'part';
    },
    _handleSelect: function _handleSelect(selectedItem) {
      var checkedKeys = this.$props.checkedKeys;

      var result = checkedKeys.some(function (key) {
        return key === selectedItem.key;
      });
      this.handleSelect(selectedItem, !result);
    },
    _handleFilter: function _handleFilter(e) {
      var _this3 = this;

      this.handleFilter(e);
      if (!e.target.value) {
        return;
      }
      // Manually trigger scroll event for lazy search bug
      // https://github.com/ant-design/ant-design/issues/5631
      this.triggerScrollTimer = setTimeout(function () {
        var transferNode = _this3.$el;
        var listNode = transferNode.querySelectorAll('.ant-transfer-list-content')[0];
        if (listNode) {
          (0, _triggerEvent2['default'])(listNode, 'scroll');
        }
      }, 0);
    },
    _handleClear: function _handleClear(e) {
      this.handleClear(e);
    },
    matchFilter: function matchFilter(text, item) {
      var _$props = this.$props,
          filter = _$props.filter,
          filterOption = _$props.filterOption;

      if (filterOption) {
        return filterOption(filter, item);
      }
      return text.indexOf(filter) >= 0;
    },
    renderItemHtml: function renderItemHtml(item) {
      var _$props$renderItem = this.$props.renderItem,
          renderItem = _$props$renderItem === undefined ? noop : _$props$renderItem;

      var renderResult = renderItem(item);
      var isRenderResultPlain = isRenderResultPlainObject(renderResult);
      return {
        renderedText: isRenderResultPlain ? renderResult.value : renderResult,
        renderedEl: isRenderResultPlain ? renderResult.label : renderResult
      };
    },
    filterNull: function filterNull(arr) {
      return arr.filter(function (item) {
        return item !== null;
      });
    }
  },

  render: function render() {
    var _this4 = this;

    var h = arguments[0];
    var _$props2 = this.$props,
        prefixCls = _$props2.prefixCls,
        dataSource = _$props2.dataSource,
        titleText = _$props2.titleText,
        checkedKeys = _$props2.checkedKeys,
        lazy = _$props2.lazy,
        disabled = _$props2.disabled,
        body = _$props2.body,
        footer = _$props2.footer,
        showSearch = _$props2.showSearch,
        filter = _$props2.filter,
        searchPlaceholder = _$props2.searchPlaceholder,
        notFoundContent = _$props2.notFoundContent,
        itemUnit = _$props2.itemUnit,
        itemsUnit = _$props2.itemsUnit;

    // Custom Layout

    var footerDom = footer && footer((0, _extends3['default'])({}, this.$props));
    var bodyDom = body && body((0, _extends3['default'])({}, this.$props));

    var listCls = (0, _classnames2['default'])(prefixCls, (0, _defineProperty3['default'])({}, prefixCls + '-with-footer', !!footerDom));

    var filteredDataSource = [];
    var totalDataSource = [];

    var showItems = dataSource.map(function (item) {
      var _renderItemHtml = _this4.renderItemHtml(item),
          renderedText = _renderItemHtml.renderedText,
          renderedEl = _renderItemHtml.renderedEl;

      if (filter && filter.trim() && !_this4.matchFilter(renderedText, item)) {
        return null;
      }

      // all show items
      totalDataSource.push(item);
      if (!item.disabled) {
        // response to checkAll items
        filteredDataSource.push(item);
      }

      var checked = checkedKeys.indexOf(item.key) >= 0;
      return h(_item2['default'], {
        attrs: {
          disabled: disabled,

          item: item,
          lazy: lazy,
          renderedText: renderedText,
          renderedEl: renderedEl,
          checked: checked,
          prefixCls: prefixCls
        },
        key: item.key, on: {
          'click': _this4._handleSelect
        }
      });
    });

    var unit = dataSource.length > 1 ? itemsUnit : itemUnit;

    var search = showSearch ? h(
      'div',
      { 'class': prefixCls + '-body-search-wrapper' },
      [h(_search2['default'], {
        attrs: {
          prefixCls: prefixCls + '-search',

          handleClear: this.handleClear,
          placeholder: searchPlaceholder,
          value: filter,
          disabled: disabled
        },
        on: {
          'change': this._handleFilter
        }
      })]
    ) : null;
    var transitionName = this.mounted ? prefixCls + '-content-item-highlight' : '';
    var transitionProps = (0, _getTransitionProps2['default'])(transitionName, {
      leave: noop
    });

    var searchNotFound = showItems.every(function (item) {
      return item === null;
    }) && h(
      'div',
      { 'class': prefixCls + '-body-not-found' },
      [notFoundContent]
    );
    var listBody = bodyDom || h(
      'div',
      {
        'class': (0, _classnames2['default'])(showSearch ? prefixCls + '-body ' + prefixCls + '-body-with-search' : prefixCls + '-body')
      },
      [search, h(
        'transition-group',
        (0, _babelHelperVueJsxMergeProps2['default'])([transitionProps, {
          attrs: {
            tag: 'ul'
          },
          'class': prefixCls + '-content',
          ref: 'listContentWrapper'
        }]),
        [showItems]
      ), searchNotFound]
    );

    var listFooter = footerDom ? h(
      'div',
      { 'class': prefixCls + '-footer' },
      [footerDom]
    ) : null;

    var checkStatus = this.getCheckStatus(filteredDataSource);
    var checkedAll = checkStatus === 'all';
    var checkAllCheckbox = h(_checkbox2['default'], {
      ref: 'checkbox',
      attrs: { disabled: disabled,
        checked: checkedAll,
        indeterminate: checkStatus === 'part'
      },
      on: {
        'change': function change() {
          _this4.handleSelectAll(filteredDataSource, checkedAll);
        }
      }
    });

    return h(
      'div',
      { 'class': listCls },
      [h(
        'div',
        { 'class': prefixCls + '-header' },
        [checkAllCheckbox, h(
          'span',
          { 'class': prefixCls + '-header-selected' },
          [h('span', [(checkedKeys.length > 0 ? checkedKeys.length + '/' : '') + totalDataSource.length, ' ', unit]), h(
            'span',
            { 'class': prefixCls + '-header-title' },
            [titleText]
          )]
        )]
      ), listBody, listFooter]
    );
  }
};