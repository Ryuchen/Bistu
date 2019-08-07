'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _index = require('../index');

var Form = {
  methods: {
    handleSubmit: function handleSubmit(e) {
      e.preventDefault();
      var validateFields = this.form.validateFields;

      validateFields().then(console.log)['catch'](console.error);
    }
  },

  render: function render() {
    var h = arguments[0];
    var getFieldDecorator = this.form.getFieldDecorator;

    return h(
      'form',
      {
        on: {
          'submit': this.handleSubmit
        }
      },
      [getFieldDecorator('name', {
        rules: [{
          required: true
        }]
      })(h('input')), h(
        'button',
        {
          attrs: { type: 'submit' }
        },
        ['submit']
      )]
    );
  }
};

exports['default'] = (0, _index.createForm)()(Form);