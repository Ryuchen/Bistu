'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _slicedToArray2 = require('babel-runtime/helpers/slicedToArray');

var _slicedToArray3 = _interopRequireDefault(_slicedToArray2);

var _extends2 = require('babel-runtime/helpers/extends');

var _extends3 = _interopRequireDefault(_extends2);

var _vueTypes = require('../_util/vue-types');

var _vueTypes2 = _interopRequireDefault(_vueTypes);

var _vnode = require('../_util/vnode');

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

function chaining() {
  for (var _len = arguments.length, fns = Array(_len), _key = 0; _key < _len; _key++) {
    fns[_key] = arguments[_key];
  }

  return function () {
    for (var _len2 = arguments.length, args = Array(_len2), _key2 = 0; _key2 < _len2; _key2++) {
      args[_key2] = arguments[_key2];
    }

    // eslint-disable-line
    // eslint-disable-line
    for (var i = 0; i < fns.length; i++) {
      if (fns[i] && typeof fns[i] === 'function') {
        fns[i].apply(this, args);
      }
    }
  };
}
exports['default'] = {
  props: {
    value: _vueTypes2['default'].any,
    disabled: _vueTypes2['default'].bool
  },
  methods: {
    focus: function focus() {
      var ele = this.$refs.ele;
      ele.focus ? ele.focus() : this.$el.focus();
    },
    blur: function blur() {
      var ele = this.$refs.ele;
      ele.blur ? ele.blur() : this.$el.blur();
    }
  },

  render: function render() {
    var _$slots = this.$slots,
        $slots = _$slots === undefined ? {} : _$slots,
        _$listeners = this.$listeners,
        $listeners = _$listeners === undefined ? {} : _$listeners,
        _$props = this.$props,
        $props = _$props === undefined ? {} : _$props,
        _$attrs = this.$attrs,
        $attrs = _$attrs === undefined ? {} : _$attrs;

    var value = $props.value === undefined ? '' : $props.value;
    var children = $slots['default'][0];
    var _$slots$default$0$com = $slots['default'][0].componentOptions,
        componentOptions = _$slots$default$0$com === undefined ? {} : _$slots$default$0$com;
    var _componentOptions$lis = componentOptions.listeners,
        listeners = _componentOptions$lis === undefined ? {} : _componentOptions$lis;

    var newEvent = (0, _extends3['default'])({}, listeners);

    var _iteratorNormalCompletion = true;
    var _didIteratorError = false;
    var _iteratorError = undefined;

    try {
      for (var _iterator = Object.entries($listeners)[Symbol.iterator](), _step; !(_iteratorNormalCompletion = (_step = _iterator.next()).done); _iteratorNormalCompletion = true) {
        var _ref = _step.value;

        var _ref2 = (0, _slicedToArray3['default'])(_ref, 2);

        var eventName = _ref2[0];
        var event = _ref2[1];

        newEvent[eventName] = chaining(event, listeners[eventName]);
      }
    } catch (err) {
      _didIteratorError = true;
      _iteratorError = err;
    } finally {
      try {
        if (!_iteratorNormalCompletion && _iterator['return']) {
          _iterator['return']();
        }
      } finally {
        if (_didIteratorError) {
          throw _iteratorError;
        }
      }
    }

    return (0, _vnode.cloneElement)(children, {
      domProps: {
        value: value
      },
      props: $props,
      on: newEvent,
      attrs: (0, _extends3['default'])({}, $attrs, { value: value }),
      ref: 'ele'
    });
  }
};