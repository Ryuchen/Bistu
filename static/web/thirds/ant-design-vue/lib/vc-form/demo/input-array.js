'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _index = require('../index');

var _styles = require('./styles');

/* eslint no-console:0 */

var uuid = 0;

var Form = {
  props: {
    form: Object
  },
  methods: {
    remove: function remove(k) {
      var form = this.form;
      // can use data-binding to get

      var keys = form.getFieldValue('keys');
      keys = keys.filter(function (key) {
        return key !== k;
      });
      // can use data-binding to set
      form.setFieldsValue({
        keys: keys
      });
    },
    add: function add() {
      uuid++;
      var form = this.form;
      // can use data-binding to get

      var keys = form.getFieldValue('keys');
      keys = keys.concat(uuid);
      // can use data-binding to set
      // important! notify form to detect changes
      form.setFieldsValue({
        keys: keys
      });
    },
    submit: function submit(e) {
      e.preventDefault();
      console.log(this.form.getFieldsValue());
    }
  },

  render: function render() {
    var _this = this;

    var h = arguments[0];
    var _form = this.form,
        getFieldProps = _form.getFieldProps,
        getFieldValue = _form.getFieldValue;

    getFieldProps('keys', {
      initialValue: []
    });
    var inputs = getFieldValue('keys').map(function (k) {
      return h(
        'div',
        { key: k, style: _styles.regionStyle },
        [h('input', getFieldProps('name' + k)), h(
          'a',
          {
            on: {
              'click': _this.remove.bind(_this, k)
            }
          },
          ['delete']
        )]
      );
    });
    return h('div', [inputs, h(
      'div',
      { style: _styles.regionStyle },
      [h(
        'button',
        {
          on: {
            'click': this.submit
          }
        },
        ['submit']
      ), h(
        'button',
        {
          on: {
            'click': this.add
          }
        },
        ['add']
      )]
    )]);
  }
};

exports['default'] = (0, _index.createForm)()(Form);