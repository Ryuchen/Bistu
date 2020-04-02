(function () {
  window.mixins = {
    // Vue instances mixins list
    _mixins: [],

    // add new mixins object item
    set mixins (object) {
      this._mixins.push(object)
    },

    // get whole mixins object items
    get mixins () {
      return this._mixins;
    }
  }
})();
