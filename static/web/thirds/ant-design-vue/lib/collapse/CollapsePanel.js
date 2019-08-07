'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _defineProperty2 = require('babel-runtime/helpers/defineProperty');

var _defineProperty3 = _interopRequireDefault(_defineProperty2);

var _extends2 = require('babel-runtime/helpers/extends');

var _extends3 = _interopRequireDefault(_extends2);

var _propsUtil = require('../_util/props-util');

var _vcCollapse = require('../vc-collapse');

var _vcCollapse2 = _interopRequireDefault(_vcCollapse);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

exports['default'] = {
  name: 'ACollapsePanel',
  props: (0, _extends3['default'])({}, _vcCollapse.panelProps),
  render: function render() {
    var h = arguments[0];
    var prefixCls = this.prefixCls,
        _showArrow = this.showArrow,
        showArrow = _showArrow === undefined ? true : _showArrow,
        $listeners = this.$listeners;

    var collapsePanelClassName = (0, _defineProperty3['default'])({}, prefixCls + '-no-arrow', !showArrow);
    var rcCollapePanelProps = {
      props: (0, _extends3['default'])({}, (0, _propsUtil.getOptionProps)(this)),
      'class': collapsePanelClassName,
      on: $listeners
    };
    var header = (0, _propsUtil.getComponentFromProp)(this, 'header');
    return h(
      _vcCollapse2['default'].Panel,
      rcCollapePanelProps,
      [this.$slots['default'], header ? h(
        'template',
        { slot: 'header' },
        [header]
      ) : null]
    );
  }
};