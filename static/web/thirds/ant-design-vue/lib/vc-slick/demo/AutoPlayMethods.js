'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

require('../assets/index.less');

var _slider = require('../src/slider');

var _slider2 = _interopRequireDefault(_slider);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

exports['default'] = {
  methods: {
    play: function play() {
      this.$refs.slider.slickPlay();
    },
    pause: function pause() {
      this.$refs.slider.slickPause();
    }
  },
  render: function render() {
    var h = arguments[0];

    var settings = {
      props: {
        dots: true,
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 2000
      },
      ref: 'slider'
    };
    return h('div', [h('h2', ['Auto Play & Pause with buttons']), h(
      _slider2['default'],
      settings,
      [h('div', [h('h3', ['1'])]), h('div', [h('h3', ['2'])]), h('div', [h('h3', ['3'])]), h('div', [h('h3', ['4'])]), h('div', [h('h3', ['5'])]), h('div', [h('h3', ['6'])])]
    ), h(
      'div',
      { style: { textAlign: 'center' } },
      [h(
        'button',
        { 'class': 'button', on: {
            'click': this.play
          }
        },
        ['Play']
      ), h(
        'button',
        { 'class': 'button', on: {
            'click': this.pause
          }
        },
        ['Pause']
      )]
    )]);
  }
};