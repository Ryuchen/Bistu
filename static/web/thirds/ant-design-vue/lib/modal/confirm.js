'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _extends2 = require('babel-runtime/helpers/extends');

var _extends3 = _interopRequireDefault(_extends2);

exports['default'] = confirm;

var _vue = require('vue');

var _vue2 = _interopRequireDefault(_vue);

var _ConfirmDialog = require('./ConfirmDialog');

var _ConfirmDialog2 = _interopRequireDefault(_ConfirmDialog);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

function confirm(config) {
  var div = document.createElement('div');
  var el = document.createElement('div');
  div.appendChild(el);
  document.body.appendChild(div);
  var currentConfig = (0, _extends3['default'])({}, config, { close: close, visible: true });

  var confirmDialogInstance = null;
  var confirmDialogProps = { props: {} };
  function close() {
    destroy.apply(undefined, arguments);
  }
  function update(newConfig) {
    currentConfig = (0, _extends3['default'])({}, currentConfig, newConfig);
    confirmDialogProps.props = currentConfig;
  }
  function destroy() {
    if (confirmDialogInstance && div.parentNode) {
      confirmDialogInstance.$destroy();
      confirmDialogInstance = null;
      div.parentNode.removeChild(div);
    }

    for (var _len = arguments.length, args = Array(_len), _key = 0; _key < _len; _key++) {
      args[_key] = arguments[_key];
    }

    var triggerCancel = args.some(function (param) {
      return param && param.triggerCancel;
    });
    if (config.onCancel && triggerCancel) {
      config.onCancel.apply(config, args);
    }
  }

  function render(props) {
    confirmDialogProps.props = props;
    return new _vue2['default']({
      el: el,
      data: function data() {
        return { confirmDialogProps: confirmDialogProps };
      },
      render: function render() {
        var h = arguments[0];

        // 先解构，避免报错，原因不详
        var cdProps = (0, _extends3['default'])({}, this.confirmDialogProps);
        return h(_ConfirmDialog2['default'], cdProps);
      }
    });
  }

  confirmDialogInstance = render(currentConfig);

  return {
    destroy: close,
    update: update
  };
}