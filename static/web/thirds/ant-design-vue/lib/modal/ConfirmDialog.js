'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _defineProperty2 = require('babel-runtime/helpers/defineProperty');

var _defineProperty3 = _interopRequireDefault(_defineProperty2);

var _classnames = require('classnames');

var _classnames2 = _interopRequireDefault(_classnames);

var _icon = require('../icon');

var _icon2 = _interopRequireDefault(_icon);

var _Modal = require('./Modal');

var _Modal2 = _interopRequireDefault(_Modal);

var _ActionButton = require('./ActionButton');

var _ActionButton2 = _interopRequireDefault(_ActionButton);

var _locale = require('./locale');

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

exports['default'] = {
  functional: true,
  render: function render(h, context) {
    var props = context.props;
    var onCancel = props.onCancel,
        onOk = props.onOk,
        close = props.close,
        zIndex = props.zIndex,
        afterClose = props.afterClose,
        visible = props.visible,
        keyboard = props.keyboard,
        centered = props.centered,
        getContainer = props.getContainer,
        maskStyle = props.maskStyle,
        okButtonProps = props.okButtonProps,
        cancelButtonProps = props.cancelButtonProps,
        _props$closable = props.closable,
        closable = _props$closable === undefined ? false : _props$closable;

    var iconType = props.iconType || 'question-circle';
    var okType = props.okType || 'primary';
    var prefixCls = props.prefixCls || 'ant-modal';
    var contentPrefixCls = prefixCls + '-confirm';
    // 默认为 true，保持向下兼容
    var okCancel = 'okCancel' in props ? props.okCancel : true;
    var width = props.width || 416;
    var style = props.style || {};
    // 默认为 false，保持旧版默认行为
    var maskClosable = props.maskClosable === undefined ? false : props.maskClosable;
    var runtimeLocale = (0, _locale.getConfirmLocale)();
    var okText = props.okText || (okCancel ? runtimeLocale.okText : runtimeLocale.justOkText);
    var cancelText = props.cancelText || runtimeLocale.cancelText;
    var autoFocusButton = props.autoFocusButton === null ? false : props.autoFocusButton || 'ok';

    var classString = (0, _classnames2['default'])(contentPrefixCls, contentPrefixCls + '-' + props.type, prefixCls + '-' + props.type, props['class']);

    var cancelButton = okCancel && h(
      _ActionButton2['default'],
      {
        attrs: {
          actionFn: onCancel,
          closeModal: close,
          autoFocus: autoFocusButton === 'cancel',
          buttonProps: cancelButtonProps
        }
      },
      [cancelText]
    );

    return h(
      _Modal2['default'],
      {
        attrs: {
          prefixCls: prefixCls,

          wrapClassName: (0, _classnames2['default'])((0, _defineProperty3['default'])({}, contentPrefixCls + '-centered', !!centered)),

          visible: visible,
          closable: closable,
          title: '',
          transitionName: 'zoom',
          footer: '',
          maskTransitionName: 'fade',
          maskClosable: maskClosable,
          maskStyle: maskStyle,

          width: width,
          zIndex: zIndex,
          afterClose: afterClose,
          keyboard: keyboard,
          centered: centered,
          getContainer: getContainer
        },
        'class': classString, on: {
          'cancel': function cancel(e) {
            return close({ triggerCancel: true }, e);
          }
        },
        style: style },
      [h(
        'div',
        { 'class': contentPrefixCls + '-body-wrapper' },
        [h(
          'div',
          { 'class': contentPrefixCls + '-body' },
          [h(_icon2['default'], {
            attrs: { type: iconType }
          }), h(
            'span',
            { 'class': contentPrefixCls + '-title' },
            [props.title]
          ), h(
            'div',
            { 'class': contentPrefixCls + '-content' },
            [props.content]
          )]
        ), h(
          'div',
          { 'class': contentPrefixCls + '-btns' },
          [cancelButton, h(
            _ActionButton2['default'],
            {
              attrs: {
                type: okType,
                actionFn: onOk,
                closeModal: close,
                autoFocus: autoFocusButton === 'ok',
                buttonProps: okButtonProps
              }
            },
            [okText]
          )]
        )]
      )]
    );
  }
};