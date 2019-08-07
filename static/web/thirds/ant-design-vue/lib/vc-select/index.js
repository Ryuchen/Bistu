'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.SelectPropTypes = exports.OptGroup = exports.Option = exports.Select = undefined;

var _Select = require('./Select');

var _Select2 = _interopRequireDefault(_Select);

var _Option = require('./Option');

var _Option2 = _interopRequireDefault(_Option);

var _PropTypes = require('./PropTypes');

var _OptGroup = require('./OptGroup');

var _OptGroup2 = _interopRequireDefault(_OptGroup);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

// based on vc-select 8.7.0
_Select.Select.Option = _Option2['default'];
_Select.Select.OptGroup = _OptGroup2['default'];
_Select2['default'].Option = _Option2['default'];
_Select2['default'].OptGroup = _OptGroup2['default'];
exports.Select = _Select.Select;
exports.Option = _Option2['default'];
exports.OptGroup = _OptGroup2['default'];
exports.SelectPropTypes = _PropTypes.SelectPropTypes;
exports['default'] = _Select2['default'];