'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _extends2 = require('babel-runtime/helpers/extends');

var _extends3 = _interopRequireDefault(_extends2);

var _vueTypes = require('../../../_util/vue-types');

var _vueTypes2 = _interopRequireDefault(_vueTypes);

var _BasePopup = require('../Base/BasePopup');

var _BasePopup2 = _interopRequireDefault(_BasePopup);

var _SearchInput = require('../SearchInput');

var _SearchInput2 = _interopRequireDefault(_SearchInput);

var _util = require('../util');

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

var SinglePopup = {
  name: 'SinglePopup',
  props: (0, _extends3['default'])({}, _BasePopup2['default'].props, _SearchInput2['default'].props, {
    searchValue: _vueTypes2['default'].string,
    showSearch: _vueTypes2['default'].bool,
    dropdownPrefixCls: _vueTypes2['default'].string,
    disabled: _vueTypes2['default'].bool,
    searchPlaceholder: _vueTypes2['default'].string
  }),
  created: function created() {
    this.inputRef = (0, _util.createRef)();
  },

  methods: {
    onPlaceholderClick: function onPlaceholderClick() {
      this.inputRef.current.focus();
    },
    _renderPlaceholder: function _renderPlaceholder() {
      var h = this.$createElement;
      var _$props = this.$props,
          searchPlaceholder = _$props.searchPlaceholder,
          searchValue = _$props.searchValue,
          prefixCls = _$props.prefixCls;


      if (!searchPlaceholder) {
        return null;
      }

      return h(
        'span',
        {
          style: {
            display: searchValue ? 'none' : 'block'
          },
          on: {
            'click': this.onPlaceholderClick
          },

          'class': prefixCls + '-search__field__placeholder'
        },
        [searchPlaceholder]
      );
    },
    _renderSearch: function _renderSearch() {
      var h = this.$createElement;
      var _$props2 = this.$props,
          showSearch = _$props2.showSearch,
          dropdownPrefixCls = _$props2.dropdownPrefixCls;


      if (!showSearch) {
        return null;
      }

      return h(
        'span',
        { 'class': dropdownPrefixCls + '-search' },
        [h(_SearchInput2['default'], {
          props: (0, _extends3['default'])({}, this.$props, { renderPlaceholder: this._renderPlaceholder }),
          on: this.$listeners,
          directives: [{
            name: 'ant-ref',
            value: this.inputRef
          }]
        })]
      );
    }
  },
  render: function render() {
    var h = arguments[0];

    return h(_BasePopup2['default'], {
      props: (0, _extends3['default'])({}, this.$props, { renderSearch: this._renderSearch, __propsSymbol__: Symbol() }),
      on: this.$listeners
    });
  }
};

exports['default'] = SinglePopup;