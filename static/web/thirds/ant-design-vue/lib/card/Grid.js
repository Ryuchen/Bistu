'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _babelHelperVueJsxMergeProps = require('babel-helper-vue-jsx-merge-props');

var _babelHelperVueJsxMergeProps2 = _interopRequireDefault(_babelHelperVueJsxMergeProps);

var _defineProperty2 = require('babel-runtime/helpers/defineProperty');

var _defineProperty3 = _interopRequireDefault(_defineProperty2);

var _vueTypes = require('../_util/vue-types');

var _vueTypes2 = _interopRequireDefault(_vueTypes);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

exports['default'] = {
  name: 'ACardGrid',
  __ANT_CARD_GRID: true,
  props: {
    prefixCls: _vueTypes2['default'].string.def('ant-card')
  },
  render: function render() {
    var h = arguments[0];
    var _$props$prefixCls = this.$props.prefixCls,
        prefixCls = _$props$prefixCls === undefined ? 'ant-card' : _$props$prefixCls;

    var classString = (0, _defineProperty3['default'])({}, prefixCls + '-grid', true);
    return h(
      'div',
      (0, _babelHelperVueJsxMergeProps2['default'])([{ on: this.$listeners }, { 'class': classString }]),
      [this.$slots['default']]
    );
  }
};