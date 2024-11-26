export default {
  namespaced: true,
  state: {
    user: {
      isAuthenticated: false,
      username: '',
      token: localStorage.getItem('token') || ''
    }
  },
  
  mutations: {
    setUser(state, user) {
      state.user.isAuthenticated = true
      state.user.username = user.username
      state.user.token = user.token
      localStorage.setItem('token', user.token)
    },
    
    clearUser(state) {
      state.user.isAuthenticated = false
      state.user.username = ''
      state.user.token = ''
      localStorage.removeItem('token')
    }
  },
  
  actions: {
    async login({ commit }, credentials) {
      try {
        const response = await fetch('/api/login/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(credentials)
        })
        const data = await response.json()
        if (data.success) {
          commit('setUser', {
            username: credentials.username,
            token: data.token
          })
          return true
        }
        return false
      } catch (error) {
        console.error('登入失敗:', error)
        return false
      }
    },
    
    logout({ commit }) {
      commit('clearUser')
    }
  },
  
  getters: {
    isAuthenticated: state => state.user.isAuthenticated,
    username: state => state.user.username
  }
}
