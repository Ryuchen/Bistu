import _mergeJSXProps from 'babel-helper-vue-jsx-merge-props';
import _defineProperty from 'babel-runtime/helpers/defineProperty';
import _extends from 'babel-runtime/helpers/extends';
import ResizeObserver from '../vc-resize-observer';
import omit from 'omit.js';
import classNames from 'classnames';
import calculateNodeHeight from './calculateNodeHeight';
import raf from '../_util/raf';
import warning from '../_util/warning';
import BaseMixin from '../_util/BaseMixin';
import inputProps from './inputProps';
import PropTypes from '../_util/vue-types';
import { getOptionProps, getListeners } from '../_util/props-util';

var TextAreaProps = _extends({}, inputProps, {
  autosize: PropTypes.oneOfType([Object, Boolean]),
  autoSize: PropTypes.oneOfType([Object, Boolean])
});
var ResizableTextArea = {
  name: 'ResizableTextArea',
  props: TextAreaProps,
  data: function data() {
    return {
      textareaStyles: {},
      resizing: false
    };
  },

  mixins: [BaseMixin],
  mounted: function mounted() {
    this.resizeTextarea();
  },
  beforeDestroy: function beforeDestroy() {
    raf.cancel(this.nextFrameActionId);
    raf.cancel(this.resizeFrameId);
  },

  watch: {
    value: function value() {
      var _this = this;

      this.$nextTick(function () {
        _this.resizeTextarea();
      });
    }
  },
  methods: {
    resizeOnNextFrame: function resizeOnNextFrame() {
      raf.cancel(this.nextFrameActionId);
      this.nextFrameActionId = raf(this.resizeTextarea);
    },
    resizeTextarea: function resizeTextarea() {
      var _this2 = this;

      var autoSize = this.$props.autoSize || this.$props.autosize;
      if (!autoSize || !this.$refs.textArea) {
        return;
      }
      var minRows = autoSize.minRows,
          maxRows = autoSize.maxRows;

      var textareaStyles = calculateNodeHeight(this.$refs.textArea, false, minRows, maxRows);
      this.setState({ textareaStyles: textareaStyles, resizing: true }, function () {
        raf.cancel(_this2.resizeFrameId);
        _this2.resizeFrameId = raf(function () {
          _this2.setState({ resizing: false });
          _this2.fixFirefoxAutoScroll();
        });
      });
    },

    // https://github.com/ant-design/ant-design/issues/21870
    fixFirefoxAutoScroll: function fixFirefoxAutoScroll() {
      try {
        if (document.activeElement === this.$refs.textArea) {
          var currentStart = this.$refs.textArea.selectionStart;
          var currentEnd = this.$refs.textArea.selectionEnd;
          this.$refs.textArea.setSelectionRange(currentStart, currentEnd);
        }
      } catch (e) {
        // Fix error in Chrome:
        // Failed to read the 'selectionStart' property from 'HTMLInputElement'
        // http://stackoverflow.com/q/21177489/3040605
      }
    },
    renderTextArea: function renderTextArea() {
      var h = this.$createElement;

      var props = getOptionProps(this);
      var prefixCls = props.prefixCls,
          autoSize = props.autoSize,
          autosize = props.autosize,
          disabled = props.disabled;
      var _$data = this.$data,
          textareaStyles = _$data.textareaStyles,
          resizing = _$data.resizing;

      warning(autosize === undefined, 'Input.TextArea', 'autosize is deprecated, please use autoSize instead.');
      var otherProps = omit(props, ['prefixCls', 'autoSize', 'autosize', 'defaultValue', 'allowClear', 'type', 'lazy', 'value']);
      var cls = classNames(prefixCls, _defineProperty({}, prefixCls + '-disabled', disabled));
      var domProps = {};
      // Fix https://github.com/ant-design/ant-design/issues/6776
      // Make sure it could be reset when using form.getFieldDecorator
      if ('value' in props) {
        domProps.value = props.value || '';
      }
      var style = _extends({}, textareaStyles, resizing ? { overflowX: 'hidden', overflowY: 'hidden' } : null);
      var textareaProps = {
        attrs: otherProps,
        domProps: domProps,
        style: style,
        'class': cls,
        on: omit(getListeners(this), 'pressEnter'),
        directives: [{
          name: 'ant-input'
        }]
      };
      return h(
        ResizeObserver,
        {
          on: {
            'resize': this.resizeOnNextFrame
          },
          attrs: { disabled: !(autoSize || autosize) }
        },
        [h('textarea', _mergeJSXProps([textareaProps, { ref: 'textArea' }]))]
      );
    }
  },

  render: function render() {
    return this.renderTextArea();
  }
};

export default ResizableTextArea;