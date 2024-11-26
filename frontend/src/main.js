import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

const app = createApp(App)

// 配置 axios
axios.defaults.baseURL = 'http://localhost:8000'
axios.defaults.withCredentials = true

app.config.globalProperties.$axios = axios

app.use(store)
   .use(router)
   .mount('#app')
