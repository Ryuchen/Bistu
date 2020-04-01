'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.ListProps = exports.ListSize = exports.ListGridType = exports.ColumnType = exports.ColumnCount = exports.ListItemMetaProps = exports.ListItemProps = undefined;

var _babelHelperVueJsxMergeProps = require('babel-helper-vue-jsx-merge-props');

var _babelHelperVueJsxMergeProps2 = _interopRequireDefault(_babelHelperVueJsxMergeProps);

var _toConsumableArray2 = require('babel-runtime/helpers/toConsumableArray');

var _toConsumableArray3 = _interopRequireDefault(_toConsumableArray2);

var _objectWithoutProperties2 = require('babel-runtime/helpers/objectWithoutProperties');

var _objectWithoutProperties3 = _interopRequireDefault(_objectWithoutProperties2);

var _extends2 = require('babel-runtime/helpers/extends');

var _extends3 = _interopRequireDefault(_extends2);

var _defineProperty2 = require('babel-runtime/helpers/defineProperty');

var _defineProperty3 = _interopRequireDefault(_defineProperty2);

var _typeof2 = require('babel-runtime/helpers/typeof');

var _typeof3 = _interopRequireDefault(_typeof2);

var _Item = require('./Item');

Object.defineProperty(exports, 'ListItemProps', {
  enumerable: true,
  get: function get() {
    return _Item.ListItemProps;
  }
});
Object.defineProperty(exports, 'ListItemMetaProps', {
  enumerable: true,
  get: function get() {
    return _Item.ListItemMetaProps;
  }
});

var _vueTypes = require('../_util/vue-types');

var _vueTypes2 = _interopRequireDefault(_vueTypes);

var _classnames = require('classnames');

var _classnames2 = _interopRequireDefault(_classnames);

var _omit = require('omit.js');

var _omit2 = _interopRequireDefault(_omit);

var _configProvider = require('../config-provider');

var _spin = require('../spin');

var _spin2 = _interopRequireDefault(_spin);

var _pagination = require('../pagination');

var _pagination2 = _interopRequireDefault(_pagination);

var _grid = require('../grid');

var _Item2 = _interopRequireDefault(_Item);

var _propsUtil = require('../_util/props-util');

var _vnode = require('../_util/vnode');

var _base = require('../base');

var _base2 = _interopRequireDefault(_base);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

var ColumnCount = exports.ColumnCount = ['', 1, 2, 3, 4, 6, 8, 12, 24];

var ColumnType = exports.ColumnType = ['gutter', 'column', 'xs', 'sm', 'md', 'lg', 'xl', 'xxl'];

var ListGridType = exports.ListGridType = {
  gutter: _vueTypes2['default'].number,
  column: _vueTypes2['default'].oneOf(ColumnCount),
  xs: _vueTypes2['default'].oneOf(ColumnCount),
  sm: _vueTypes2['default'].oneOf(ColumnCount),
  md: _vueTypes2['default'].oneOf(ColumnCount),
  lg: _vueTypes2['default'].oneOf(ColumnCount),
  xl: _vueTypes2['default'].oneOf(ColumnCount),
  xxl: _vueTypes2['default'].oneOf(ColumnCount)
};

var ListSize = exports.ListSize = ['small', 'default', 'large'];

var ListProps = exports.ListProps = function ListProps() {
  return {
    bordered: _vueTypes2['default'].bool,
    dataSource: _vueTypes2['default'].array,
    extra: _vueTypes2['default'].any,
    grid: _vueTypes2['default'].shape(ListGridType).loose,
    itemLayout: _vueTypes2['default'].string,
    loading: _vueTypes2['default'].oneOfType([_vueTypes2['default'].bool, _vueTypes2['default'].object]),
    loadMore: _vueTypes2['default'].any,
    pagination: _vueTypes2['default'].oneOfType([_vueTypes2['default'].shape((0, _pagination.PaginationConfig)()).loose, _vueTypes2['default'].bool]),
    prefixCls: _vueTypes2['default'].string,
    rowKey: _vueTypes2['default'].any,
    renderItem: _vueTypes2['default'].any,
    size: _vueTypes2['default'].oneOf(ListSize),
    split: _vueTypes2['default'].bool,
    header: _vueTypes2['default'].any,
    footer: _vueTypes2['default'].any,
    locale: _vueTypes2['default'].object
  };
};

var List = {
  Item: _Item2['default'],
  name: 'AList',
  props: (0, _propsUtil.initDefaultProps)(ListProps(), {
    dataSource: [],
    bordered: false,
    split: true,
    loading: false,
    pagination: false
  }),
  provide: function provide() {
    return {
      listContext: this
    };
  },

  inject: {
    configProvider: { 'default': function _default() {
        return _configProvider.ConfigConsumerProps;
      } }
  },
  data: function data() {
    var _this = this;

    this.keys = [];
    this.defaultPaginationProps = {
      current: 1,
      pageSize: 10,
      onChange: function onChange(page, pageSize) {
        var pagination = _this.pagination;

        _this.paginationCurrent = page;
        if (pagination && pagination.onChange) {
          pagination.onChange(page, pageSize);
        }
      },
      total: 0
    };
    this.onPaginationChange = this.triggerPaginationEvent('onChange');
    this.onPaginationShowSizeChange = this.triggerPaginationEvent('onShowSizeChange');
    var pagination = this.$props.pagination;

    var paginationObj = pagination && (typeof pagination === 'undefined' ? 'undefined' : (0, _typeof3['default'])(pagination)) === 'object' ? pagination : {};
    return {
      paginationCurrent: paginationObj.defaultCurrent || 1,
      paginationSize: paginationObj.defaultPageSize || 10
    };
  },

  methods: {
    triggerPaginationEvent: function triggerPaginationEvent(eventName) {
      var _this2 = this;

      return function (page, pageSize) {
        var pagination = _this2.$props.pagination;

        _this2.paginationCurrent = page;
        _this2.paginationSize = pageSize;
        if (pagination && pagination[eventName]) {
          pagination[eventName](page, pageSize);
        }
      };
    },
    renderItem2: function renderItem2(item, index) {
      var $scopedSlots = this.$scopedSlots,
          rowKey = this.rowKey;

      var renderItem = this.renderItem || $scopedSlots.renderItem;
      if (!renderItem) return null;
      var key = void 0;
      if (typeof rowKey === 'function') {
        key = rowKey(item);
      } else if (typeof rowKey === 'string') {
        key = item[rowKey];
      } else {
        key = item.key;
      }

      if (!key) {
        key = 'list-item-' + index;
      }

      this.keys[index] = key;

      return renderItem(item, index);
    },
    isSomethingAfterLastItem: function isSomethingAfterLastItem() {
      var pagination = this.pagination;

      var loadMore = (0, _propsUtil.getComponentFromProp)(this, 'loadMore');
      var footer = (0, _propsUtil.getComponentFromProp)(this, 'footer');
      return !!(loadMore || pagination || footer);
    },
    renderEmpty: function renderEmpty(prefixCls, _renderEmpty) {
      var h = this.$createElement;
      var locale = this.locale;

      return h(
        'div',
        { 'class': prefixCls + '-empty-text' },
        [locale && locale.emptyText || _renderEmpty(h, 'List')]
      );
    }
  },

  render: function render() {
    var _classNames,
        _this3 = this;

    var h = arguments[0];
    var customizePrefixCls = this.prefixCls,
        bordered = this.bordered,
        split = this.split,
        itemLayout = this.itemLayout,
        pagination = this.pagination,
        grid = this.grid,
        _dataSource = this.dataSource,
        dataSource = _dataSource === undefined ? [] : _dataSource,
        size = this.size,
        loading = this.loading,
        $slots = this.$slots,
        paginationCurrent = this.paginationCurrent,
        paginationSize = this.paginationSize;

    var getPrefixCls = this.configProvider.getPrefixCls;
    var prefixCls = getPrefixCls('list', customizePrefixCls);

    var loadMore = (0, _propsUtil.getComponentFromProp)(this, 'loadMore');
    var footer = (0, _propsUtil.getComponentFromProp)(this, 'footer');
    var header = (0, _propsUtil.getComponentFromProp)(this, 'header');
    var children = (0, _propsUtil.filterEmpty)($slots['default'] || []);
    var loadingProp = loading;
    if (typeof loadingProp === 'boolean') {
      loadingProp = {
        spinning: loadingProp
      };
    }
    var isLoading = loadingProp && loadingProp.spinning;

    // large => lg
    // small => sm
    var sizeCls = '';
    switch (size) {
      case 'large':
        sizeCls = 'lg';
        break;
      case 'small':
        sizeCls = 'sm';
        break;
      default:
        break;
    }
    var classString = (0, _classnames2['default'])(prefixCls, (_classNames = {}, (0, _defineProperty3['default'])(_classNames, prefixCls + '-vertical', itemLayout === 'vertical'), (0, _defineProperty3['default'])(_classNames, prefixCls + '-' + sizeCls, sizeCls), (0, _defineProperty3['default'])(_classNames, prefixCls + '-split', split), (0, _defineProperty3['default'])(_classNames, prefixCls + '-bordered', bordered), (0, _defineProperty3['default'])(_classNames, prefixCls + '-loading', isLoading), (0, _defineProperty3['default'])(_classNames, prefixCls + '-grid', grid), (0, _defineProperty3['default'])(_classNames, prefixCls + '-something-after-last-item', this.isSomethingAfterLastItem()), _classNames));
    var paginationProps = (0, _extends3['default'])({}, this.defaultPaginationProps, {
      total: dataSource.length,
      current: paginationCurrent,
      pageSize: paginationSize
    }, pagination || {});
    var largestPage = Math.ceil(paginationProps.total / paginationProps.pageSize);
    if (paginationProps.current > largestPage) {
      paginationProps.current = largestPage;
    }
    var cls = paginationProps['class'],
        style = paginationProps.style,
        restProps = (0, _objectWithoutProperties3['default'])(paginationProps, ['class', 'style']);

    var paginationContent = pagination ? h(
      'div',
      { 'class': prefixCls + '-pagination' },
      [h(_pagination2['default'], {
        props: (0, _omit2['default'])(restProps, ['onChange']),
        'class': cls,
        style: style,
        on: {
          change: this.onPaginationChange,
          showSizeChange: this.onPaginationShowSizeChange
        }
      })]
    ) : null;

    var splitDataSource = [].concat((0, _toConsumableArray3['default'])(dataSource));
    if (pagination) {
      if (dataSource.length > (paginationProps.current - 1) * paginationProps.pageSize) {
        splitDataSource = [].concat((0, _toConsumableArray3['default'])(dataSource)).splice((paginationProps.current - 1) * paginationProps.pageSize, paginationProps.pageSize);
      }
    }

    var childrenContent = void 0;
    childrenContent = isLoading && h('div', { style: { minHeight: 53 } });
    if (splitDataSource.length > 0) {
      var items = splitDataSource.map(function (item, index) {
        return _this3.renderItem2(item, index);
      });
      var childrenList = items.map(function (child, index) {
        return (0, _vnode.cloneElement)(child, {
          key: _this3.keys[index]
        });
      });

      childrenContent = grid ? h(
        _grid.Row,
        {
          attrs: { gutter: grid.gutter }
        },
        [childrenList]
      ) : h(
        'ul',
        { 'class': prefixCls + '-items' },
        [childrenList]
      );
    } else if (!children.length && !isLoading) {
      var renderEmpty = this.configProvider.renderEmpty;
      childrenContent = this.renderEmpty(prefixCls, renderEmpty);
    }
    var paginationPosition = paginationProps.position || 'bottom';

    return h(
      'div',
      (0, _babelHelperVueJsxMergeProps2['default'])([{ 'class': classString }, { on: (0, _propsUtil.getListeners)(this) }]),
      [(paginationPosition === 'top' || paginationPosition === 'both') && paginationContent, header && h(
        'div',
        { 'class': prefixCls + '-header' },
        [header]
      ), h(
        _spin2['default'],
        { props: loadingProp },
        [childrenContent, children]
      ), footer && h(
        'div',
        { 'class': prefixCls + '-footer' },
        [footer]
      ), loadMore || (paginationPosition === 'bottom' || paginationPosition === 'both') && paginationContent]
    );
  }
};

/* istanbul ignore next */
List.install = function (Vue) {
  Vue.use(_base2['default']);
  Vue.component(List.name, List);
  Vue.component(List.Item.name, List.Item);
  Vue.component(List.Item.Meta.name, List.Item.Meta);
};

exports['default'] = List;