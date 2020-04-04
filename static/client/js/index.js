(function () {
  window.Bus = new Vue(); // 将 vue 的事件总线注册到 window 上

  /*
   * 声明 vuex 的状态管理
   */
  const store = new Vuex.Store({
    modules: {
      app: {
        namespaced: true,
        state: {
          application: {},
          collapsed: false,
          activeKey: '0',
          activePanes: [],
          permissions: [],
        },
        getters: {
          collapsed: function (state) {
            const value = JSON.parse(window.localStorage.getItem('collapsed') || null);
            if (value) state.collapsed = value;
            return state.collapsed;
          },
          activeKey: function (state) {
            const value = JSON.parse(window.localStorage.getItem('activeKey') || null);
            if (value) state.activeKey = value;
            return state.activeKey;
          },
          activeKeys: function (state) {
            const value = JSON.parse(window.localStorage.getItem('activeKey') || null);
            if (value) state.activeKey = value;
            return [state.activeKey];
          },
          activePanes: function (state) {
            const value = JSON.parse(window.localStorage.getItem('activePanes') || null);
            if (value) state.activePanes = value;
            return state.activePanes;
          },
          hasPermission: (state) => (permission) => {
            return !(state.permissions.indexOf(permission));
          }
        },
        mutations: {
          changeCollapsed: function (state){
            state.collapsed = !state.collapsed;
            window.localStorage.setItem('collapsed', JSON.stringify(state.collapsed));
          },
          changeActiveKey: function (state, payload) {
            state.activeKey = payload;
            window.localStorage.setItem('activeKey', JSON.stringify(state.activeKey));
          },
          addActivePanes: function (state, payload) {
            if (state.activePanes.findIndex(obj => obj.key === payload.key) === -1) {
              state.activePanes.push(payload);
            }
            window.localStorage.setItem('activePanes', JSON.stringify(state.activePanes));
          },
          setPermissions: function (state, permissions) {
            state.permissions = permissions;
          }
        }
      }
    }
  });

  /*
   * 全局 vue 实例
   */
  new Vue({
    delimiters: ['<%', '%>'],
    el: '#app',
    store,
    mixins: window.mixins.mixins,
    created: function () {
      const _this = this;
      if (window.innerWidth <= 992) {
        this.$store.commit('app/changeCollapsed');
      }
      Bus.$on('notification', function(type, title, message){
        _this.$notification[type]({
          message: title,
          description:
            message,
        });
      });
    }
  });
})();

