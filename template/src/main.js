// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
// element-ui
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

// 跨域问题解决方案
import axios from 'axios'
axios.defaults.baseURL = 'http://127.0.0.1:5000'
Vue.prototype.$ajax = axios

Vue.config.productionTip = false

// element-ui
Vue.use(ElementUI)

// 绘图插件
import jsPlumb from 'jsplumb'
Vue.prototype.$jsPlumb = jsPlumb.jsPlumb

import SuperFlow from 'vue-super-flow'
import 'vue-super-flow/lib/index.css'

Vue.use(SuperFlow)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
