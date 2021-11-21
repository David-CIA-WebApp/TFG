import Vue from 'vue'
import App from './App.vue'
import VueRouter from "vue-router";
import Routes from "./routes";

process.env.VUE_APP_BACK_URL = "http://141.94.203.217:8001";

Vue.use(VueRouter);

const rutas = new VueRouter({
  mode: "history",
	routes: Routes,
  scrollBehavior() {
    return { x: 0, y: 0 };
  },
})

new Vue({
  el: '#app',
  render: h => h(App),
  router: rutas
})