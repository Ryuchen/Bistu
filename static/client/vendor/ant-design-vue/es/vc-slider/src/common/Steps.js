import _defineProperty from 'babel-runtime/helpers/defineProperty';
import _extends from 'babel-runtime/helpers/extends';
import classNames from 'classnames';
import warning from '../../../_util/warning';

var calcPoints = function calcPoints(vertical, marks, dots, step, min, max) {
  warning(dots ? step > 0 : true, 'Slider', '`Slider[step]` should be a positive number in order to make Slider[dots] work.');
  var points = Object.keys(marks).map(parseFloat).sort(function (a, b) {
    return a - b;
  });
  if (dots && step) {
    for (var i = min; i <= max; i += step) {
      if (points.indexOf(i) === -1) {
        points.push(i);
      }
    }
  }
  return points;
};

var Steps = {
  functional: true,
  render: function render(h, context) {
    var _context$props = context.props,
        prefixCls = _context$props.prefixCls,
        vertical = _context$props.vertical,
        reverse = _context$props.reverse,
        marks = _context$props.marks,
        dots = _context$props.dots,
        step = _context$props.step,
        included = _context$props.included,
        lowerBound = _context$props.lowerBound,
        upperBound = _context$props.upperBound,
        max = _context$props.max,
        min = _context$props.min,
        dotStyle = _context$props.dotStyle,
        activeDotStyle = _context$props.activeDotStyle;

    var range = max - min;
    var elements = calcPoints(vertical, marks, dots, step, min, max).map(function (point) {
      var _classNames;

      var offset = Math.abs(point - min) / range * 100 + '%';

      var isActived = !included && point === upperBound || included && point <= upperBound && point >= lowerBound;
      var style = vertical ? _extends({}, dotStyle, _defineProperty({}, reverse ? 'top' : 'bottom', offset)) : _extends({}, dotStyle, _defineProperty({}, reverse ? 'right' : 'left', offset));
      if (isActived) {
        style = _extends({}, style, activeDotStyle);
      }

      var pointClassName = classNames((_classNames = {}, _defineProperty(_classNames, prefixCls + '-dot', true), _defineProperty(_classNames, prefixCls + '-dot-active', isActived), _defineProperty(_classNames, prefixCls + '-dot-reverse', reverse), _classNames));

      return h('span', { 'class': pointClassName, style: style, key: point });
    });

    return h(
      'div',
      { 'class': prefixCls + '-step' },
      [elements]
    );
  }
};

export default Steps;