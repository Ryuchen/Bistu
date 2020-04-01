import PropTypes from '../_util/vue-types';
var triggerType = PropTypes.oneOf(['hover', 'focus', 'click', 'contextmenu']);
export default (function () {
  return {
    trigger: PropTypes.oneOfType([triggerType, PropTypes.arrayOf(triggerType)]).def('hover'),
    visible: PropTypes.bool,
    defaultVisible: PropTypes.bool,
    placement: PropTypes.oneOf(['top', 'left', 'right', 'bottom', 'topLeft', 'topRight', 'bottomLeft', 'bottomRight', 'leftTop', 'leftBottom', 'rightTop', 'rightBottom']).def('top'),
    transitionName: PropTypes.string.def('zoom-big-fast'),
    // onVisibleChange: PropTypes.func,
    overlayStyle: PropTypes.object.def(function () {
      return {};
    }),
    overlayClassName: PropTypes.string,
    prefixCls: PropTypes.string,
    mouseEnterDelay: PropTypes.number.def(0.1),
    mouseLeaveDelay: PropTypes.number.def(0.1),
    getPopupContainer: PropTypes.func,
    arrowPointAtCenter: PropTypes.bool.def(false),
    autoAdjustOverflow: PropTypes.oneOfType([PropTypes.bool, PropTypes.object]).def(true),
    destroyTooltipOnHide: PropTypes.bool.def(false),
    align: PropTypes.object.def(function () {
      return {};
    }),
    builtinPlacements: PropTypes.object
  };
});