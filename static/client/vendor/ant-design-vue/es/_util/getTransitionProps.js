import animate from './css-animation';
var noop = function noop() {};
var getTransitionProps = function getTransitionProps(transitionName) {
  var opt = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : {};
  var beforeEnter = opt.beforeEnter,
      enter = opt.enter,
      afterEnter = opt.afterEnter,
      leave = opt.leave,
      afterLeave = opt.afterLeave,
      _opt$appear = opt.appear,
      appear = _opt$appear === undefined ? true : _opt$appear,
      tag = opt.tag,
      nativeOn = opt.nativeOn;

  var transitionProps = {
    props: {
      appear: appear,
      css: false
    },
    on: {
      beforeEnter: beforeEnter || noop,
      enter: enter || function (el, done) {
        animate(el, transitionName + '-enter', done);
      },
      afterEnter: afterEnter || noop,
      leave: leave || function (el, done) {
        animate(el, transitionName + '-leave', done);
      },
      afterLeave: afterLeave || noop
    },
    nativeOn: nativeOn
  };
  // transition-group
  if (tag) {
    transitionProps.tag = tag;
  }
  return transitionProps;
};

export default getTransitionProps;