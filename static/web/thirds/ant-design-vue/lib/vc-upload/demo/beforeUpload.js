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
        action: 'https://www.mocky.io/v2/5cc8019d300000980a055e76',
        multiple: true,
        beforeUpload: function beforeUpload(file, fileList) {
          console.log(file, fileList);
          return new Promise(function (resolve) {
            console.log('start check');
            setTimeout(function () {
              console.log('check finshed');
              resolve(file);
            }, 3000);
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
      }
    };
    return h(
      'div',
      {
        style: {
          margin: '100px'
        }
      },
      [h('div', [h(
        _index2['default'],
        uploaderProps,
        [h('a', ['\u5F00\u59CB\u4E0A\u4F20'])]
      )])]
    );
  }
};