'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _index = require('../index');

var _index2 = _interopRequireDefault(_index);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

exports['default'] = {
  render: function render() {
    var h = arguments[0];

    var uploaderProps = {
      props: {
        action: function action() {
          return new Promise(function (resolve) {
            setTimeout(function () {
              resolve('https://www.mocky.io/v2/5cc8019d300000980a055e76');
            }, 2000);
          });
        }
      },
      on: {
        start: function start(file) {
          console.log('start', file, file.name);
        },
        success: function success(file) {
          console.log('success', file);
        },
        error: function error(err) {
          console.log('error', err);
        }
      },
      style: {
        margin: '100px'
      }
    };
    return h(
      _index2['default'],
      uploaderProps,
      [h('a', ['\u5F00\u59CB\u4E0A\u4F20'])]
    );
  }
};