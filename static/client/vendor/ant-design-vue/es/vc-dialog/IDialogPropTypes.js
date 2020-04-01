import PropTypes from '../_util/vue-types';

function IDialogPropTypes() {
  return {
    keyboard: PropTypes.bool,
    mask: PropTypes.bool,
    afterClose: PropTypes.func,
    // onClose: PropTypes. (e: SyntheticEvent<HTMLDivElement>) =>any,
    closable: PropTypes.bool,
    maskClosable: PropTypes.bool,
    visible: PropTypes.bool,
    destroyOnClose: PropTypes.bool,
    mousePosition: PropTypes.shape({
      x: PropTypes.number,
      y: PropTypes.number
    }).loose,
    title: PropTypes.any,
    footer: PropTypes.any,
    transitionName: PropTypes.string,
    maskTransitionName: PropTypes.string,
    animation: PropTypes.any,
    maskAnimation: PropTypes.any,
    wrapStyle: PropTypes.object,
    bodyStyle: PropTypes.object,
    maskStyle: PropTypes.object,
    prefixCls: PropTypes.string,
    wrapClassName: PropTypes.string,
    width: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
    height: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
    zIndex: PropTypes.number,
    bodyProps: PropTypes.any,
    maskProps: PropTypes.any,
    wrapProps: PropTypes.any,
    getContainer: PropTypes.any,
    dialogStyle: PropTypes.object.def(function () {
      return {};
    }),
    dialogClass: PropTypes.object.def(function () {
      return {};
    }),
    closeIcon: PropTypes.any,
    forceRender: PropTypes.bool,
    getOpenCount: PropTypes.func,
    // https://github.com/ant-design/ant-design/issues/19771
    // https://github.com/react-component/dialog/issues/95
    focusTriggerAfterClose: PropTypes.bool
  };
}

export default IDialogPropTypes;