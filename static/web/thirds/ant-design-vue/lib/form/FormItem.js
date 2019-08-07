'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.FormItemProps = undefined;

var _typeof2 = require('babel-runtime/helpers/typeof');

var _typeof3 = _interopRequireDefault(_typeof2);

var _defineProperty2 = require('babel-runtime/helpers/defineProperty');

var _defineProperty3 = _interopRequireDefault(_defineProperty2);

var _objectWithoutProperties2 = require('babel-runtime/helpers/objectWithoutProperties');

var _objectWithoutProperties3 = _interopRequireDefault(_objectWithoutProperties2);

var _babelHelperVueJsxMergeProps = require('babel-helper-vue-jsx-merge-props');

var _babelHelperVueJsxMergeProps2 = _interopRequireDefault(_babelHelperVueJsxMergeProps);

var _toConsumableArray2 = require('babel-runtime/helpers/toConsumableArray');

var _toConsumableArray3 = _interopRequireDefault(_toConsumableArray2);

var _intersperse = require('intersperse');

var _intersperse2 = _interopRequireDefault(_intersperse);

var _vueTypes = require('../_util/vue-types');

var _vueTypes2 = _interopRequireDefault(_vueTypes);

var _classnames = require('classnames');

var _classnames2 = _interopRequireDefault(_classnames);

var _find = require('lodash/find');

var _find2 = _interopRequireDefault(_find);

var _Row = require('../grid/Row');

var _Row2 = _interopRequireDefault(_Row);

var _Col = require('../grid/Col');

var _Col2 = _interopRequireDefault(_Col);

var _warning = require('../_util/warning');

var _warning2 = _interopRequireDefault(_warning);

var _constants = require('./constants');

var _propsUtil = require('../_util/props-util');

var _getTransitionProps = require('../_util/getTransitionProps');

var _getTransitionProps2 = _interopRequireDefault(_getTransitionProps);

var _BaseMixin = require('../_util/BaseMixin');

var _BaseMixin2 = _interopRequireDefault(_BaseMixin);

var _vnode = require('../_util/vnode');

var _icon = require('../icon');

var _icon2 = _interopRequireDefault(_icon);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

function noop() {}
var FormItemProps = exports.FormItemProps = {
  id: _vueTypes2['default'].string,
  prefixCls: _vueTypes2['default'].string,
  label: _vueTypes2['default'].any,
  labelCol: _vueTypes2['default'].shape(_Col.ColProps).loose,
  wrapperCol: _vueTypes2['default'].shape(_Col.ColProps).loose,
  help: _vueTypes2['default'].any,
  extra: _vueTypes2['default'].any,
  validateStatus: _vueTypes2['default'].oneOf(['', 'success', 'warning', 'error', 'validating']),
  hasFeedback: _vueTypes2['default'].bool,
  required: _vueTypes2['default'].bool,
  colon: _vueTypes2['default'].bool,
  fieldDecoratorId: _vueTypes2['default'].string,
  fieldDecoratorOptions: _vueTypes2['default'].object
};
function comeFromSlot() {
  var vnodes = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : [];
  var itemVnode = arguments[1];

  var isSlot = false;
  for (var i = 0, len = vnodes.length; i < len; i++) {
    var vnode = vnodes[i];
    if (vnode && (vnode === itemVnode || vnode.$vnode === itemVnode)) {
      isSlot = true;
    } else {
      var children = vnode.componentOptions ? vnode.componentOptions.children : vnode.children;
      isSlot = comeFromSlot(children, itemVnode);
    }
    if (isSlot) {
      break;
    }
  }
  return isSlot;
}

exports['default'] = {
  name: 'AFormItem',
  __ANT_FORM_ITEM: true,
  mixins: [_BaseMixin2['default']],
  props: (0, _propsUtil.initDefaultProps)(FormItemProps, {
    hasFeedback: false,
    prefixCls: 'ant-form',
    colon: true
  }),
  inject: {
    FormProps: { 'default': function _default() {
        return {};
      } },
    decoratorFormProps: { 'default': function _default() {
        return {};
      } },
    collectFormItemContext: { 'default': function _default() {
        return noop;
      } }
  },
  data: function data() {
    return { helpShow: false };
  },
  created: function created() {
    this.collectContext();
  },
  beforeUpdate: function beforeUpdate() {
    if (process.env.NODE_ENV !== 'production') {
      this.collectContext();
    }
  },
  beforeDestroy: function beforeDestroy() {
    this.collectFormItemContext(this.$vnode.context, 'delete');
  },
  mounted: function mounted() {
    (0, _warning2['default'])(this.getControls(this.slotDefault, true).length <= 1, '`Form.Item` cannot generate `validateStatus` and `help` automatically, ' + 'while there are more than one `getFieldDecorator` in it.');
    (0, _warning2['default'])(!this.fieldDecoratorId, '`fieldDecoratorId` is deprecated. please use `v-decorator={id, options}` instead.');
  },

  methods: {
    collectContext: function collectContext() {
      if (this.FormProps.form && this.FormProps.form.templateContext) {
        var templateContext = this.FormProps.form.templateContext;

        var vnodes = Object.values(templateContext.$slots || {}).reduce(function (a, b) {
          return [].concat((0, _toConsumableArray3['default'])(a), (0, _toConsumableArray3['default'])(b));
        }, []);
        var isSlot = comeFromSlot(vnodes, this.$vnode);
        (0, _warning2['default'])(!isSlot, 'You can not set FormItem from slot, please use slot-scope instead slot');
        var isSlotScope = false;
        // 进一步判断是否是通过slot-scope传递
        if (!isSlot && this.$vnode.context !== templateContext) {
          isSlotScope = comeFromSlot(this.$vnode.context.$children, templateContext.$vnode);
        }
        if (!isSlotScope && !isSlot) {
          this.collectFormItemContext(this.$vnode.context);
        }
      }
    },
    getHelpMessage: function getHelpMessage() {
      var help = (0, _propsUtil.getComponentFromProp)(this, 'help');
      var onlyControl = this.getOnlyControl();
      if (help === undefined && onlyControl) {
        var errors = this.getField().errors;
        if (errors) {
          return (0, _intersperse2['default'])(errors.map(function (e, index) {
            return (0, _propsUtil.isValidElement)(e.message) ? (0, _vnode.cloneElement)(e.message, { key: index }) : e.message;
          }), ' ');
        } else {
          return '';
        }
      }

      return help;
    },
    getControls: function getControls() {
      var childrenArray = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : [];
      var recursively = arguments[1];

      var controls = [];
      for (var i = 0; i < childrenArray.length; i++) {
        if (!recursively && controls.length > 0) {
          break;
        }

        var child = childrenArray[i];
        if (!child.tag && child.text.trim() === '') {
          continue;
        }

        if ((0, _propsUtil.getSlotOptions)(child).__ANT_FORM_ITEM) {
          continue;
        }
        var children = (0, _propsUtil.getAllChildren)(child);
        var attrs = child.data && child.data.attrs || {};
        if (_constants.FIELD_META_PROP in attrs) {
          // And means FIELD_DATA_PROP in child.props, too.
          controls.push(child);
        } else if (children) {
          controls = controls.concat(this.getControls(children, recursively));
        }
      }
      return controls;
    },
    getOnlyControl: function getOnlyControl() {
      var child = this.getControls(this.slotDefault, false)[0];
      return child !== undefined ? child : null;
    },
    getChildAttr: function getChildAttr(prop) {
      var child = this.getOnlyControl();
      var data = {};
      if (!child) {
        return undefined;
      }
      if (child.data) {
        data = child.data;
      } else if (child.$vnode && child.$vnode.data) {
        data = child.$vnode.data;
      }
      return data[prop] || data.attrs[prop];
    },
    getId: function getId() {
      return this.getChildAttr('id');
    },
    getMeta: function getMeta() {
      return this.getChildAttr(_constants.FIELD_META_PROP);
    },
    getField: function getField() {
      return this.getChildAttr(_constants.FIELD_DATA_PROP);
    },
    onHelpAnimEnd: function onHelpAnimEnd(_key, helpShow) {
      this.helpShow = helpShow;
      if (!helpShow) {
        this.$forceUpdate();
      }
    },
    renderHelp: function renderHelp() {
      var _this = this;

      var h = this.$createElement;

      var prefixCls = this.prefixCls;
      var help = this.getHelpMessage();
      var children = help ? h(
        'div',
        { 'class': prefixCls + '-explain', key: 'help' },
        [help]
      ) : null;
      if (children) {
        this.helpShow = !!children;
      }
      var transitionProps = (0, _getTransitionProps2['default'])('show-help', {
        afterEnter: function afterEnter() {
          return _this.onHelpAnimEnd('help', true);
        },
        afterLeave: function afterLeave() {
          return _this.onHelpAnimEnd('help', false);
        }
      });
      return h(
        'transition',
        (0, _babelHelperVueJsxMergeProps2['default'])([transitionProps, { key: 'help' }]),
        [children]
      );
    },
    renderExtra: function renderExtra() {
      var h = this.$createElement;
      var prefixCls = this.prefixCls;

      var extra = (0, _propsUtil.getComponentFromProp)(this, 'extra');
      return extra ? h(
        'div',
        { 'class': prefixCls + '-extra' },
        [extra]
      ) : null;
    },
    getValidateStatus: function getValidateStatus() {
      var onlyControl = this.getOnlyControl();
      if (!onlyControl) {
        return '';
      }
      var field = this.getField();
      if (field.validating) {
        return 'validating';
      }
      if (field.errors) {
        return 'error';
      }
      var fieldValue = 'value' in field ? field.value : this.getMeta().initialValue;
      if (fieldValue !== undefined && fieldValue !== null && fieldValue !== '') {
        return 'success';
      }
      return '';
    },
    renderValidateWrapper: function renderValidateWrapper(c1, c2, c3) {
      var h = this.$createElement;

      var props = this.$props;
      var onlyControl = this.getOnlyControl;
      var validateStatus = props.validateStatus === undefined && onlyControl ? this.getValidateStatus() : props.validateStatus;

      var classes = props.prefixCls + '-item-control';
      if (validateStatus) {
        classes = (0, _classnames2['default'])(props.prefixCls + '-item-control', {
          'has-feedback': props.hasFeedback || validateStatus === 'validating',
          'has-success': validateStatus === 'success',
          'has-warning': validateStatus === 'warning',
          'has-error': validateStatus === 'error',
          'is-validating': validateStatus === 'validating'
        });
      }
      var iconType = '';
      switch (validateStatus) {
        case 'success':
          iconType = 'check-circle';
          break;
        case 'warning':
          iconType = 'exclamation-circle';
          break;
        case 'error':
          iconType = 'close-circle';
          break;
        case 'validating':
          iconType = 'loading';
          break;
        default:
          iconType = '';
          break;
      }
      var icon = props.hasFeedback && iconType ? h(
        'span',
        { 'class': props.prefixCls + '-item-children-icon' },
        [h(_icon2['default'], {
          attrs: { type: iconType, theme: iconType === 'loading' ? 'outlined' : 'filled' }
        })]
      ) : null;
      return h(
        'div',
        { 'class': classes },
        [h(
          'span',
          { 'class': props.prefixCls + '-item-children' },
          [c1, icon]
        ), c2, c3]
      );
    },
    renderWrapper: function renderWrapper(children) {
      var h = this.$createElement;
      var prefixCls = this.prefixCls,
          _wrapperCol = this.wrapperCol,
          wrapperCol = _wrapperCol === undefined ? {} : _wrapperCol;
      var cls = wrapperCol['class'],
          style = wrapperCol.style,
          id = wrapperCol.id,
          on = wrapperCol.on,
          restProps = (0, _objectWithoutProperties3['default'])(wrapperCol, ['class', 'style', 'id', 'on']);

      var className = (0, _classnames2['default'])(prefixCls + '-item-control-wrapper', cls);
      var colProps = {
        props: restProps,
        'class': className,
        key: 'wrapper',
        style: style,
        id: id,
        on: on
      };
      return h(
        _Col2['default'],
        colProps,
        [children]
      );
    },
    isRequired: function isRequired() {
      var required = this.required;

      if (required !== undefined) {
        return required;
      }
      if (this.getOnlyControl()) {
        var meta = this.getMeta() || {};
        var validate = meta.validate || [];

        return validate.filter(function (item) {
          return !!item.rules;
        }).some(function (item) {
          return item.rules.some(function (rule) {
            return rule.required;
          });
        });
      }
      return false;
    },


    // Resolve duplicated ids bug between different forms
    // https://github.com/ant-design/ant-design/issues/7351
    onLabelClick: function onLabelClick(e) {
      var label = (0, _propsUtil.getComponentFromProp)(this, 'label');
      var id = this.id || this.getId();
      if (!id) {
        return;
      }
      var controls = document.querySelectorAll('[id="' + id + '"]');
      if (controls.length !== 1) {
        // Only prevent in default situation
        // Avoid preventing event in `label={<a href="xx">link</a>}``
        if (typeof label === 'string') {
          e.preventDefault();
        }
        var control = this.$el.querySelector('[id="' + id + '"]');
        if (control && control.focus) {
          control.focus();
        }
      }
    },
    renderLabel: function renderLabel() {
      var h = this.$createElement;
      var prefixCls = this.prefixCls,
          _labelCol = this.labelCol,
          labelCol = _labelCol === undefined ? {} : _labelCol,
          colon = this.colon,
          id = this.id;

      var label = (0, _propsUtil.getComponentFromProp)(this, 'label');
      var required = this.isRequired();
      var labelColClass = labelCol['class'],
          labelColStyle = labelCol.style,
          labelColId = labelCol.id,
          on = labelCol.on,
          restProps = (0, _objectWithoutProperties3['default'])(labelCol, ['class', 'style', 'id', 'on']);

      var labelColClassName = (0, _classnames2['default'])(prefixCls + '-item-label', labelColClass);
      var labelClassName = (0, _classnames2['default'])((0, _defineProperty3['default'])({}, prefixCls + '-item-required', required));

      var labelChildren = label;
      // Keep label is original where there should have no colon
      var haveColon = colon && this.FormProps.layout !== 'vertical';
      // Remove duplicated user input colon
      if (haveColon && typeof label === 'string' && label.trim() !== '') {
        labelChildren = label.replace(/[：|:]\s*$/, '');
      }
      var colProps = {
        props: restProps,
        'class': labelColClassName,
        key: 'label',
        style: labelColStyle,
        id: labelColId,
        on: on
      };

      return label ? h(
        _Col2['default'],
        colProps,
        [h(
          'label',
          {
            attrs: {
              'for': id || this.getId(),

              title: typeof label === 'string' ? label : ''
            },
            'class': labelClassName, on: {
              'click': this.onLabelClick
            }
          },
          [labelChildren]
        )]
      ) : null;
    },
    renderChildren: function renderChildren() {
      return [this.renderLabel(), this.renderWrapper(this.renderValidateWrapper(this.slotDefault, this.renderHelp(), this.renderExtra()))];
    },
    renderFormItem: function renderFormItem(children) {
      var _itemClassName;

      var h = this.$createElement;

      var props = this.$props;
      var prefixCls = props.prefixCls;
      var itemClassName = (_itemClassName = {}, (0, _defineProperty3['default'])(_itemClassName, prefixCls + '-item', true), (0, _defineProperty3['default'])(_itemClassName, prefixCls + '-item-with-help', this.helpShow), (0, _defineProperty3['default'])(_itemClassName, prefixCls + '-item-no-colon', !props.colon), _itemClassName);

      return h(
        _Row2['default'],
        { 'class': (0, _classnames2['default'])(itemClassName) },
        [children]
      );
    },
    decoratorOption: function decoratorOption(vnode) {
      if (vnode.data && vnode.data.directives) {
        var directive = (0, _find2['default'])(vnode.data.directives, ['name', 'decorator']);
        (0, _warning2['default'])(!directive || directive && Array.isArray(directive.value), 'Invalid directive: type check failed for directive "decorator". Expected Array, got ' + (0, _typeof3['default'])(directive ? directive.value : directive) + '. At ' + vnode.tag + '.');
        return directive ? directive.value : null;
      } else {
        return null;
      }
    },
    decoratorChildren: function decoratorChildren(vnodes) {
      var FormProps = this.FormProps;

      var getFieldDecorator = FormProps.form.getFieldDecorator;
      for (var i = 0, len = vnodes.length; i < len; i++) {
        var vnode = vnodes[i];
        if ((0, _propsUtil.getSlotOptions)(vnode).__ANT_FORM_ITEM) {
          break;
        }
        if (vnode.children) {
          vnode.children = this.decoratorChildren((0, _vnode.cloneVNodes)(vnode.children));
        } else if (vnode.componentOptions && vnode.componentOptions.children) {
          vnode.componentOptions.children = this.decoratorChildren((0, _vnode.cloneVNodes)(vnode.componentOptions.children));
        }
        var option = this.decoratorOption(vnode);
        if (option && option[0]) {
          vnodes[i] = getFieldDecorator(option[0], option[1])(vnode);
        }
      }
      return vnodes;
    }
  },

  render: function render() {
    var $slots = this.$slots,
        decoratorFormProps = this.decoratorFormProps,
        fieldDecoratorId = this.fieldDecoratorId,
        _fieldDecoratorOption = this.fieldDecoratorOptions,
        fieldDecoratorOptions = _fieldDecoratorOption === undefined ? {} : _fieldDecoratorOption,
        FormProps = this.FormProps;

    var child = (0, _propsUtil.filterEmpty)($slots['default'] || []);
    if (decoratorFormProps.form && fieldDecoratorId && child.length) {
      var getFieldDecorator = decoratorFormProps.form.getFieldDecorator;
      child[0] = getFieldDecorator(fieldDecoratorId, fieldDecoratorOptions)(child[0]);
      (0, _warning2['default'])(!(child.length > 1), '`autoFormCreate` just `decorator` then first children. but you can use JSX to support multiple children');
      this.slotDefault = child;
    } else if (FormProps.form) {
      child = (0, _vnode.cloneVNodes)(child);
      this.slotDefault = this.decoratorChildren(child);
    } else {
      this.slotDefault = child;
    }

    var children = this.renderChildren();
    return this.renderFormItem(children);
  }
};