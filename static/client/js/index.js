(function () {
  moment.locale('zh-cn');
  window.Bus = new Vue();  // 将 vue 的事件总线注册到 window 上
  window.csrftoken = Cookies.get('csrftoken');  // 将django页面渲染的csrftoken值作为全局对象
  /*
   * 声明 vuex 的状态管理
   */
  const store = new Vuex.Store({
    modules: {
      site: {
        namespaced: true,
        state: {
          application: {  // Pre define default value
            'app': {
              "name": "Postgraduate Manager System",
              "description": "Using for College CMS"
            },
            'auth': {
              "name": "Ryuchen",
              "year": "2018",
              "href": "https://github.com/Ryuchen"
            },
            'toolbox': {
              "lock": {
                "enable": true,
                "verify": "email"
              },
              "github": {
                "enable": true,
                "link": "https://github.com/ryuchen"
              },
              "search": {
                "enable": true,
              },
              "notice": {
                "enable": true,
              },
              "utility": {
                "enable": true,
              }
            }
          },  // 应用产品的信息
          collapsed: false,  // 侧边栏是否收起
          openKeys: [],  // 当前展开的 SubMenu 菜单项 key 数组
          activeKey: '0',  // 当前激活的tab页面key
          activePanes: [],  // 总共打开的tab页面
        },
        getters: {
          application: function(state) {
            const value = JSON.parse(window.localStorage.getItem('application') || null);
            state.application = value ? value : {};
            return state.application;
          },
          collapsed: function (state) {
            const value = JSON.parse(window.localStorage.getItem('collapsed') || null);
            state.collapsed = value ? value : false;
            return state.collapsed;
          },
          openKeys: function (state) {
            const value = JSON.parse(window.localStorage.getItem('openKeys') || null);
            state.openKeys = value ? value : [];
            return state.openKeys;
          },
          activeKey: function (state) {
            const value = JSON.parse(window.localStorage.getItem('activeKey') || null);
            state.activeKey = value ? value : '0';
            return state.activeKey;
          },
          activePanes: function (state) {
            const value = JSON.parse(window.localStorage.getItem('activePanes') || null);
            state.activePanes = value ? value : [];
            return state.activePanes;
          }
        },
        mutations: {
          application: function (state, payload) {
            state.application = payload;
            window.localStorage.setItem('application', JSON.stringify(state.application));
          },
          collapsed: function (state){
            state.collapsed = !state.collapsed;
            window.localStorage.setItem('collapsed', JSON.stringify(state.collapsed));
          },
          openKeys: function (state, payload) {
            state.openKeys = payload;
            window.localStorage.setItem('openKeys', JSON.stringify(state.openKeys));
          },
          activeKey: function (state, payload) {
            state.activeKey = payload;
            window.localStorage.setItem('activeKey', JSON.stringify(state.activeKey));
          },
          // for tab panes open && close method
          addActivePanes: function (state, payload) {
            const value = JSON.parse(window.localStorage.getItem('activePanes') || null);
            state.activePanes = value ? value : [];
            if (state.activePanes.findIndex(obj => obj.key === payload.key) === -1) {
              state.activePanes.push(payload);
            }
            window.localStorage.setItem('activePanes', JSON.stringify(state.activePanes));
          },
          delActivePanes: function (state, payload) {
            state.activePanes = state.activePanes.filter(item => item.key !== payload);
            window.localStorage.setItem('activePanes', JSON.stringify(state.activePanes));
          }
        }
      },
      user: {
        namespaced: true,
        state: {
          profile: {},  // 用户的账户信息
          authority: {},  // 用户的组信息
          permissions: {}  // 用户的权限信息
        },
        getters: {
          profile: function (state) {
            const value = JSON.parse(window.localStorage.getItem('profile') || null);
            state.profile = value ? value : {};
          },
          authority: function (state) {
            const value = JSON.parse(window.localStorage.getItem('authority') || null);
            state.authority = value ? value : {};
          },
          hasPermission: (state) => (permission) => {
            return !(state.permissions.indexOf(permission));
          }
        },
        mutations: {
          profile: function (state, payload) {
            state.profile = payload;
            window.localStorage.setItem('profile', JSON.stringify(state.profile));
          },
          authority: function (state, payload) {
            state.authority = payload;
            window.localStorage.setItem('authority', JSON.stringify(state.authority));
          },
          permissions: function (state, permissions) {
            state.permissions = permissions;
            window.localStorage.setItem('permissions', JSON.stringify(state.permissions));
          }
        }
      },
      colleges: {
        namespaced: true,
        state: {
          academy: {}
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
      // 全局事件总线:=>进行错误信息提醒
      const _this = this;
      Bus.$on('notification', function(type, title, message){
        _this.$notification[type]({
          message: title,
          description:
            message,
        });
      });
      // 全局事件总线:=>进行标签页打开&&关闭
      Bus.$on('openPane', function(payload){
        _this.$store.commit('site/addActivePanes', payload);
        _this.$store.commit('site/activeKey', payload.key);
      });
      Bus.$on('closePane', function(payload){
        _this.$store.commit('site/delActivePanes', payload);
        if (_this.$store.state.site.activePanes.length > 0) {
          _this.$store.commit('site/activeKey', _this.$store.state.site.activePanes[_this.$store.state.site.activePanes.length - 1].key);
        } else {
          _this.$store.commit('site/activeKey', '0');
        }
      });
    },
    methods: {
      // 全局右键菜单功能
      refresh () {
        window.location.reload(true);
      },
      closeCurrent () {
        // TODO: 虽然关闭了标签页面，但是没有重载tab页
        Bus.$emit('closePane', this.$store.state.site.activeKey);
      },
      goBack () {
        history.go(-1);
      }
    }
  });
})();

