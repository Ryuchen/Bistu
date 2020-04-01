import PropTypes from '../_util/vue-types';
export default {
  prefixCls: PropTypes.string.def('rc-menu'),
  focusable: PropTypes.bool.def(true),
  multiple: PropTypes.bool,
  defaultActiveFirst: PropTypes.bool,
  visible: PropTypes.bool.def(true),
  activeKey: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
  selectedKeys: PropTypes.arrayOf(PropTypes.oneOfType([PropTypes.string, PropTypes.number])),
  defaultSelectedKeys: PropTypes.arrayOf(PropTypes.oneOfType([PropTypes.string, PropTypes.number])).def([]),
  defaultOpenKeys: PropTypes.arrayOf(PropTypes.oneOfType([PropTypes.string, PropTypes.number])).def([]),
  openKeys: PropTypes.arrayOf(PropTypes.oneOfType([PropTypes.string, PropTypes.number])),
  openAnimation: PropTypes.oneOfType([PropTypes.string, PropTypes.object]),
  mode: PropTypes.oneOf(['horizontal', 'vertical', 'vertical-left', 'vertical-right', 'inline']).def('vertical'),
  triggerSubMenuAction: PropTypes.string.def('hover'),
  subMenuOpenDelay: PropTypes.number.def(0.1),
  subMenuCloseDelay: PropTypes.number.def(0.1),
  level: PropTypes.number.def(1),
  inlineIndent: PropTypes.number.def(24),
  theme: PropTypes.oneOf(['light', 'dark']).def('light'),
  getPopupContainer: PropTypes.func,
  openTransitionName: PropTypes.string,
  forceSubMenuRender: PropTypes.bool,
  selectable: PropTypes.bool,
  isRootMenu: PropTypes.bool.def(true),
  builtinPlacements: PropTypes.object.def(function () {
    return {};
  }),
  itemIcon: PropTypes.any,
  expandIcon: PropTypes.any,
  overflowedIndicator: PropTypes.any
};