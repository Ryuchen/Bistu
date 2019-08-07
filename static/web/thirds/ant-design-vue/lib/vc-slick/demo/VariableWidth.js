'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

require('../assets/index.less');

var _slider = require('../src/slider');

var _slider2 = _interopRequireDefault(_slider);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

exports['default'] = {
  render: function render() {
    var h = arguments[0];

    var settings = {
      'class': 'slider variable-width',
      props: {
        dots: true,
        infinite: true,
        centerMode: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        variableWidth: true
      }
    };
    return h('div', [h('h2', ['Variable width']), h(
      _slider2['default'],
      settings,
      [h(
        'div',
        { style: { width: '100px' } },
        [h('p', ['100'])]
      ), h(
        'div',
        { style: { width: '200px' } },
        [h('p', ['200'])]
      ), h(
        'div',
        { style: { width: '75px' } },
        [h('p', ['75'])]
      ), h(
        'div',
        { style: { width: '300px' } },
        [h('p', ['300'])]
      ), h(
        'div',
        { style: { width: '225px' } },
        [h('p', ['225'])]
      ), h(
        'div',
        { style: { width: '175px' } },
        [h('p', ['175'])]
      )]
    )]);
  }
};