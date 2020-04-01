import PropTypes from '../../_util/vue-types';

var collapseProps = function collapseProps() {
  return {
    prefixCls: PropTypes.string,
    activeKey: PropTypes.oneOfType([PropTypes.string, PropTypes.number, PropTypes.arrayOf(PropTypes.oneOfType([PropTypes.string, PropTypes.number]))]),
    defaultActiveKey: PropTypes.oneOfType([PropTypes.string, PropTypes.number, PropTypes.arrayOf(PropTypes.oneOfType([PropTypes.string, PropTypes.number]))]),
    accordion: PropTypes.bool,
    destroyInactivePanel: PropTypes.bool,
    bordered: PropTypes.bool,
    expandIcon: PropTypes.func,
    openAnimation: PropTypes.object,
    expandIconPosition: PropTypes.oneOf(['left', 'right'])
  };
};

var panelProps = function panelProps() {
  return {
    openAnimation: PropTypes.object,
    prefixCls: PropTypes.string,
    header: PropTypes.oneOfType([PropTypes.string, PropTypes.number, PropTypes.node]),
    headerClass: PropTypes.string,
    showArrow: PropTypes.bool,
    isActive: PropTypes.bool,
    destroyInactivePanel: PropTypes.bool,
    disabled: PropTypes.bool,
    accordion: PropTypes.bool,
    forceRender: PropTypes.bool,
    expandIcon: PropTypes.func,
    extra: PropTypes.any,
    panelKey: PropTypes.any
  };
};

export { collapseProps, panelProps };