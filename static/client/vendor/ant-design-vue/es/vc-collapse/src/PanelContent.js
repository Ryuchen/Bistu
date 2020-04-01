import _defineProperty from 'babel-runtime/helpers/defineProperty';
import PropTypes from '../../_util/vue-types';

export default {
  name: 'PanelContent',
  props: {
    prefixCls: PropTypes.string,
    isActive: PropTypes.bool,
    destroyInactivePanel: PropTypes.bool,
    forceRender: PropTypes.bool,
    role: PropTypes.any
  },
  data: function data() {
    return {
      _isActive: undefined
    };
  },
  render: function render() {
    var _contentCls;

    var h = arguments[0];

    this._isActive = this.forceRender || this._isActive || this.isActive;
    if (!this._isActive) {
      return null;
    }
    var _$props = this.$props,
        prefixCls = _$props.prefixCls,
        isActive = _$props.isActive,
        destroyInactivePanel = _$props.destroyInactivePanel,
        forceRender = _$props.forceRender,
        role = _$props.role;
    var $slots = this.$slots;

    var contentCls = (_contentCls = {}, _defineProperty(_contentCls, prefixCls + '-content', true), _defineProperty(_contentCls, prefixCls + '-content-active', isActive), _contentCls);
    var child = !forceRender && !isActive && destroyInactivePanel ? null : h(
      'div',
      { 'class': prefixCls + '-content-box' },
      [$slots['default']]
    );
    return h(
      'div',
      { 'class': contentCls, attrs: { role: role }
      },
      [child]
    );
  }
};