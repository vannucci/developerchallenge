import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import axios from 'axios'

import Vuetify, {
  VApp,
  VNavigationDrawer,
  VFooter,
  VToolbar,
  VFadeTransition
} from 'vuetify/lib'
import { Ripple } from 'vuetify/lib/directives'

Vue.config.productionTip = false
Vue.prototype.$http = axios

export const serverBus = new Vue()

new Vue({
  render: h => h(App),
}).$mount('#app')

Vue.use(Vuetify, {
  components: {
    VApp,
    VNavigationDrawer,
    VFooter,
    VToolbar,
    VFadeTransition
  },
  directives :{
    Ripple
  }
})