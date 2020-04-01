import _objectWithoutProperties from 'babel-runtime/helpers/objectWithoutProperties';
import _defineProperty from 'babel-runtime/helpers/defineProperty';
import Vue from 'vue';
import PropTypes from '../_util/vue-types';
import { getStyle, getComponentFromProp } from '../_util/props-util';
import BaseMixin from '../_util/BaseMixin';
import createChainedFunction from '../_util/createChainedFunction';
import getTransitionProps from '../_util/getTransitionProps';
import Notice from './Notice';
import Base from '../base';

function noop() {}

var seed = 0;
var now = Date.now();

function getUuid() {
  return 'rcNotification_' + now + '_' + seed++;
}

var Notification = {
  mixins: [BaseMixin],
  props: {
    prefixCls: PropTypes.string.def('rc-notification'),
    transitionName: PropTypes.string,
    animation: PropTypes.oneOfType([PropTypes.string, PropTypes.object]).def('fade'),
    maxCount: PropTypes.number,
    closeIcon: PropTypes.any
  },
  data: function data() {
    return {
      notices: []
    };
  },

  methods: {
    getTransitionName: function getTransitionName() {
      var props = this.$props;
      var transitionName = props.transitionName;
      if (!transitionName && props.animation) {
        transitionName = props.prefixCls + '-' + props.animation;
      }
      return transitionName;
    },
    add: function add(notice) {
      var key = notice.key = notice.key || getUuid();
      var maxCount = this.$props.maxCount;

      this.setState(function (previousState) {
        var notices = previousState.notices;
        var noticeIndex = notices.map(function (v) {
          return v.key;
        }).indexOf(key);
        var updatedNotices = notices.concat();
        if (noticeIndex !== -1) {
          updatedNotices.splice(noticeIndex, 1, notice);
        } else {
          if (maxCount && notices.length >= maxCount) {
            // XXX, use key of first item to update new added (let React to move exsiting
            // instead of remove and mount). Same key was used before for both a) external
            // manual control and b) internal react 'key' prop , which is not that good.
            notice.updateKey = updatedNotices[0].updateKey || updatedNotices[0].key;
            updatedNotices.shift();
          }
          updatedNotices.push(notice);
        }
        return {
          notices: updatedNotices
        };
      });
    },
    remove: function remove(key) {
      this.setState(function (previousState) {
        return {
          notices: previousState.notices.filter(function (notice) {
            return notice.key !== key;
          })
        };
      });
    }
  },

  render: function render(h) {
    var _this = this;

    var prefixCls = this.prefixCls,
        notices = this.notices,
        remove = this.remove,
        getTransitionName = this.getTransitionName;

    var transitionProps = getTransitionProps(getTransitionName());
    var noticeNodes = notices.map(function (notice, index) {
      var update = Boolean(index === notices.length - 1 && notice.updateKey);
      var key = notice.updateKey ? notice.updateKey : notice.key;

      var content = notice.content,
          duration = notice.duration,
          closable = notice.closable,
          onClose = notice.onClose,
          style = notice.style,
          className = notice['class'];

      var close = createChainedFunction(remove.bind(_this, notice.key), onClose);
      var noticeProps = {
        props: {
          prefixCls: prefixCls,
          duration: duration,
          closable: closable,
          update: update,
          closeIcon: getComponentFromProp(_this, 'closeIcon')
        },
        on: {
          close: close,
          click: notice.onClick || noop
        },
        style: style,
        'class': className,
        key: key
      };
      return h(
        Notice,
        noticeProps,
        [typeof content === 'function' ? content(h) : content]
      );
    });
    var className = _defineProperty({}, prefixCls, 1);
    var style = getStyle(this);
    return h(
      'div',
      {
        'class': className,
        style: style || {
          top: '65px',
          left: '50%'
        }
      },
      [h(
        'transition-group',
        transitionProps,
        [noticeNodes]
      )]
    );
  }
};

Notification.newInstance = function newNotificationInstance(properties, callback) {
  var _ref = properties || {},
      getContainer = _ref.getContainer,
      style = _ref.style,
      className = _ref['class'],
      props = _objectWithoutProperties(_ref, ['getContainer', 'style', 'class']);

  var div = document.createElement('div');
  if (getContainer) {
    var root = getContainer();
    root.appendChild(div);
  } else {
    document.body.appendChild(div);
  }
  var V = Base.Vue || Vue;
  new V({
    el: div,
    mounted: function mounted() {
      var self = this;
      this.$nextTick(function () {
        callback({
          notice: function notice(noticeProps) {
            self.$refs.notification.add(noticeProps);
          },
          removeNotice: function removeNotice(key) {
            self.$refs.notification.remove(key);
          },

          component: self,
          destroy: function destroy() {
            self.$destroy();
            self.$el.parentNode.removeChild(self.$el);
          }
        });
      });
    },
    render: function render() {
      var h = arguments[0];

      var p = {
        props: props,
        ref: 'notification',
        style: style,
        'class': className
      };
      return h(Notification, p);
    }
  });
};

export default Notification;