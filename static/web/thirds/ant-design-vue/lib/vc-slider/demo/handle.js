'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _objectWithoutProperties2 = require('babel-runtime/helpers/objectWithoutProperties');

var _objectWithoutProperties3 = _interopRequireDefault(_objectWithoutProperties2);

var _extends2 = require('babel-runtime/helpers/extends');

var _extends3 = _interopRequireDefault(_extends2);

var _index = require('../index');

var _index2 = _interopRequireDefault(_index);

var _vcTooltip = require('../../vc-tooltip');

var _vcTooltip2 = _interopRequireDefault(_vcTooltip);

require('../assets/index.less');

require('../../vc-tooltip/assets/bootstrap.less');

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

var Handle = _index2['default'].Handle;
var createSliderWithTooltip = _index2['default'].createSliderWithTooltip;

var Range = createSliderWithTooltip(_index2['default'].Range);

exports['default'] = {
  data: function data() {
    return {
      visibles: []
    };
  },

  methods: {
    handleTooltipVisibleChange: function handleTooltipVisibleChange(index, visible) {
      this.visibles[index] = visible;
      this.visibles = (0, _extends3['default'])({}, this.visibles);
    }
  },
  render: function render() {
    var h = arguments[0];

    var handle = function handle(props) {
      var value = props.value,
          dragging = props.dragging,
          index = props.index,
          ref = props.ref,
          style = props.style,
          restProps = (0, _objectWithoutProperties3['default'])(props, ['value', 'dragging', 'index', 'ref', 'style']);

      var handleProps = {
        props: (0, _extends3['default'])({}, restProps, {
          value: value
        }),
        key: index,
        style: style,
        ref: ref
      };
      return h(
        _vcTooltip2['default'],
        {
          attrs: {
            prefixCls: 'rc-slider-tooltip',
            overlay: value,
            visible: dragging,
            placement: 'top'
          },
          key: index
        },
        [h(Handle, handleProps)]
      );
    };

    // const handleRange = (h, { value, ref, dragging, index, disabled, style, ...restProps }) => {
    //   const tipFormatter = value => `${value}%`
    //   const tipProps = {}

    //   const {
    //     prefixCls = 'rc-slider-tooltip',
    //     overlay = tipFormatter(value),
    //     placement = 'top',
    //     visible = visible || false,
    //     ...restTooltipProps } = tipProps

    //   let handleStyleWithIndex
    //   if (Array.isArray(style)) {
    //     handleStyleWithIndex = style[index] || style[0]
    //   } else {
    //     handleStyleWithIndex = style
    //   }

    //   const tooltipProps = {
    //     props: {
    //       prefixCls,
    //       overlay,
    //       placement,
    //       visible: (!disabled && (this.visibles[index] || dragging)) || visible,
    //       ...restTooltipProps,
    //     },
    //     key: index,
    //   }
    //   const handleProps = {
    //     props: {
    //       value,
    //       ...restProps,
    //     },
    //     on: {
    //       mouseenter: () => this.handleTooltipVisibleChange(index, true),
    //       mouseleave: () => this.handleTooltipVisibleChange(index, false),
    //     },
    //     style: {
    //       ...handleStyleWithIndex,
    //     },
    //     ref,
    //   }

    //   return (
    //     <Tooltip
    //       {...tooltipProps}
    //     >

    //       <Handle
    //         {...handleProps}
    //       />
    //     </Tooltip>
    //   )
    // }
    var wrapperStyle = 'width: 400px; margin: 50px';

    return h('div', [h(
      'div',
      { style: wrapperStyle },
      [h('p', ['Slider with custom handle']), h(_index2['default'], {
        attrs: { min: 0, max: 20, defaultValue: 3, handle: handle }
      })]
    ), h(
      'div',
      { style: wrapperStyle },
      [h('p', ['Range with custom handle']), h(Range, {
        attrs: { min: 0, max: 20, defaultValue: [3, 10], tipFormatter: function tipFormatter(value) {
            return value + '%';
          } }
      })]
    )]);
  }
};