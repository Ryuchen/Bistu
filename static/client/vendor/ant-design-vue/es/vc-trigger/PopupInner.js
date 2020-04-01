import _mergeJSXProps from 'babel-helper-vue-jsx-merge-props';
import PropTypes from '../_util/vue-types';
import LazyRenderBox from './LazyRenderBox';
import { getListeners } from '../_util/props-util';

export default {
  props: {
    hiddenClassName: PropTypes.string.def(''),
    prefixCls: PropTypes.string,
    visible: PropTypes.bool
  },
  render: function render() {
    var h = arguments[0];
    var _$props = this.$props,
        prefixCls = _$props.prefixCls,
        visible = _$props.visible,
        hiddenClassName = _$props.hiddenClassName;

    var divProps = {
      on: getListeners(this)
    };

    return h(
      'div',
      _mergeJSXProps([divProps, { 'class': !visible ? hiddenClassName : '' }]),
      [h(
        LazyRenderBox,
        { 'class': prefixCls + '-content', attrs: { visible: visible }
        },
        [this.$slots['default']]
      )]
    );
  }
};