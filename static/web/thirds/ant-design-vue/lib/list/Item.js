'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.Meta = exports.ListItemMetaProps = exports.ListItemProps = undefined;

var _defineProperty2 = require('babel-runtime/helpers/defineProperty');

var _defineProperty3 = _interopRequireDefault(_defineProperty2);

var _babelHelperVueJsxMergeProps = require('babel-helper-vue-jsx-merge-props');

var _babelHelperVueJsxMergeProps2 = _interopRequireDefault(_babelHelperVueJsxMergeProps);

var _vueTypes = require('../_util/vue-types');

var _vueTypes2 = _interopRequireDefault(_vueTypes);

var _classnames = require('classnames');

var _classnames2 = _interopRequireDefault(_classnames);

var _propsUtil = require('../_util/props-util');

var _grid = require('../grid');

var _index = require('./index');

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

var ListItemProps = exports.ListItemProps = {
  prefixCls: _vueTypes2['default'].string,
  extra: _vueTypes2['default'].any,
  actions: _vueTypes2['default'].arrayOf(_vueTypes2['default'].any),
  grid: _index.ListGridType
};

var ListItemMetaProps = exports.ListItemMetaProps = {
  avatar: _vueTypes2['default'].any,
  description: _vueTypes2['default'].any,
  prefixCls: _vueTypes2['default'].string,
  title: _vueTypes2['default'].any
};

var Meta = exports.Meta = {
  functional: true,
  name: 'AListItemMeta',
  __ANT_LIST_ITEM_META: true,
  render: function render(h, context) {
    var props = context.props,
        slots = context.slots,
        listeners = context.listeners;

    var slotsMap = slots();
    var _props$prefixCls = props.prefixCls,
        prefixCls = _props$prefixCls === undefined ? 'ant-list' : _props$prefixCls;

    var avatar = props.avatar || slotsMap.avatar;
    var title = props.title || slotsMap.title;
    var description = props.description || slotsMap.description;
    var content = h(
      'div',
      { 'class': prefixCls + '-item-meta-content' },
      [title && h(
        'h4',
        { 'class': prefixCls + '-item-meta-title' },
        [title]
      ), description && h(
        'div',
        { 'class': prefixCls + '-item-meta-description' },
        [description]
      )]
    );
    return h(
      'div',
      (0, _babelHelperVueJsxMergeProps2['default'])([{ on: listeners }, { 'class': prefixCls + '-item-meta' }]),
      [avatar && h(
        'div',
        { 'class': prefixCls + '-item-meta-avatar' },
        [avatar]
      ), (title || description) && content]
    );
  }
};

function getGrid(grid, t) {
  return grid[t] && Math.floor(24 / grid[t]);
}

exports['default'] = {
  name: 'AListItem',
  Meta: Meta,
  props: ListItemProps,
  inject: {
    listContext: { 'default': function _default() {
        return {};
      } }
  },

  render: function render() {
    var h = arguments[0];
    var grid = this.listContext.grid;
    var _prefixCls = this.prefixCls,
        prefixCls = _prefixCls === undefined ? 'ant-list' : _prefixCls,
        $slots = this.$slots,
        $listeners = this.$listeners;

    var classString = prefixCls + '-item';
    var extra = (0, _propsUtil.getComponentFromProp)(this, 'extra');
    var actions = (0, _propsUtil.getComponentFromProp)(this, 'actions');
    var metaContent = [];
    var otherContent = [];

    ($slots['default'] || []).forEach(function (element) {
      if (!(0, _propsUtil.isEmptyElement)(element)) {
        if ((0, _propsUtil.getSlotOptions)(element).__ANT_LIST_ITEM_META) {
          metaContent.push(element);
        } else {
          otherContent.push(element);
        }
      }
    });

    var contentClassString = (0, _classnames2['default'])(prefixCls + '-item-content', (0, _defineProperty3['default'])({}, prefixCls + '-item-content-single', metaContent.length < 1));
    var content = otherContent.length > 0 ? h(
      'div',
      { 'class': contentClassString },
      [otherContent]
    ) : null;

    var actionsContent = void 0;
    if (actions && actions.length > 0) {
      var actionsContentItem = function actionsContentItem(action, i) {
        return h(
          'li',
          { key: prefixCls + '-item-action-' + i },
          [action, i !== actions.length - 1 && h('em', { 'class': prefixCls + '-item-action-split' })]
        );
      };
      actionsContent = h(
        'ul',
        { 'class': prefixCls + '-item-action' },
        [actions.map(function (action, i) {
          return actionsContentItem(action, i);
        })]
      );
    }

    var extraContent = h(
      'div',
      { 'class': prefixCls + '-item-extra-wrap' },
      [h(
        'div',
        { 'class': prefixCls + '-item-main' },
        [metaContent, content, actionsContent]
      ), h(
        'div',
        { 'class': prefixCls + '-item-extra' },
        [extra]
      )]
    );

    var mainContent = grid ? h(
      _grid.Col,
      {
        attrs: {
          span: getGrid(grid, 'column'),
          xs: getGrid(grid, 'xs'),
          sm: getGrid(grid, 'sm'),
          md: getGrid(grid, 'md'),
          lg: getGrid(grid, 'lg'),
          xl: getGrid(grid, 'xl'),
          xxl: getGrid(grid, 'xxl')
        }
      },
      [h(
        'div',
        (0, _babelHelperVueJsxMergeProps2['default'])([{ on: $listeners }, { 'class': classString }]),
        [extra && extraContent, !extra && metaContent, !extra && content, !extra && actionsContent]
      )]
    ) : h(
      'div',
      (0, _babelHelperVueJsxMergeProps2['default'])([{ on: $listeners }, { 'class': classString }]),
      [extra && extraContent, !extra && metaContent, !extra && content, !extra && actionsContent]
    );

    return mainContent;
  }
};