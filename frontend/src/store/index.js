import { createStore } from 'vuex'
import settings from './modules/settings'
import auth from './modules/auth'

export default createStore({
  modules: {
    settings,
    auth
  }
})
