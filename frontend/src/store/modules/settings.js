export default {
  namespaced: true,
  state: {
    language: localStorage.getItem('language') || 'zh',
    fontSize: localStorage.getItem('fontSize') || 'medium'
  },
  mutations: {
    SET_LANGUAGE(state, language) {
      state.language = language
      localStorage.setItem('language', language)
    },
    SET_FONT_SIZE(state, size) {
      state.fontSize = size
      localStorage.setItem('fontSize', size)
    }
  },
  actions: {
    changeLanguage({ commit }, language) {
      commit('SET_LANGUAGE', language)
    },
    changeFontSize({ commit }, size) {
      commit('SET_FONT_SIZE', size)
    }
  },
  getters: {
    currentLanguage: state => state.language,
    currentFontSize: state => state.fontSize
  }
}
