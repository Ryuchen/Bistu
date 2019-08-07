'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _index = require('../src/index');

var _index2 = _interopRequireDefault(_index);

var _index3 = require('../../button/index');

var _index4 = _interopRequireDefault(_index3);

require('../assets/index.less');

require('../../menu/style/index');

require('../../icon/style/index');

require('../../button/style/index');

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

exports['default'] = {
  data: function data() {
    return {
      open: false,
      openChild: false,
      openChildren: false
    };
  },

  methods: {
    onClick: function onClick() {
      this.open = !this.open;
    },
    onChildClick: function onChildClick() {
      this.openChild = !this.openChild;
    },
    onChildrenClick: function onChildrenClick() {
      this.openChildren = !this.openChildren;
    },
    getLevelMove: function getLevelMove(e) {
      var target = e.target;
      if (target.className.indexOf('drawer1') >= 0) {
        return [200, 100];
      }
      return 100;
    }
  },
  render: function render() {
    var h = arguments[0];

    return h('div', [h(
      'div',
      {
        style: {
          width: '100%',
          height: 667,
          background: '#fff000',
          color: '#fff',
          textAlign: 'center',
          lineHeight: '667px'
        }
      },
      [h(
        _index4['default'],
        {
          on: {
            'click': this.onClick
          }
        },
        ['\u6253\u5F00\u62BD\u5C49']
      )]
    ), h(
      _index2['default'],
      {
        attrs: {
          width: '20vw',
          handler: false,
          open: this.open,

          placement: 'right'
        },
        on: {
          'maskClick': this.onClick
        },

        'class': 'drawer1' },
      [h('div', [h(
        _index4['default'],
        {
          on: {
            'click': this.onChildClick
          }
        },
        ['\u6253\u5F00\u5B50\u7EA7']
      ), h(
        _index2['default'],
        {
          attrs: {
            handler: false,
            open: this.openChild,

            level: '.drawer1',
            placement: 'right',
            levelMove: 100
          },
          on: {
            'maskClick': this.onChildClick
          },

          'class': 'drawer2' },
        [h(
          'div',
          { style: { width: 200 } },
          ['\u4E8C\u7EA7\u62BD\u5C49', h(
            _index4['default'],
            {
              on: {
                'click': this.onChildrenClick
              }
            },
            ['\u6253\u5F00\u5B50\u7EA7']
          ), h(
            _index2['default'],
            {
              attrs: {
                handler: false,
                open: this.openChildren,

                level: ['.drawer1', '.drawer2'],
                placement: 'right',
                levelMove: this.getLevelMove
              },
              on: {
                'maskClick': this.onChildrenClick
              }
            },
            [h(
              'div',
              { style: { width: 200 } },
              ['\u4E09\u7EA7\u62BD\u5C49']
            )]
          )]
        )]
      )])]
    )]);
  }
};