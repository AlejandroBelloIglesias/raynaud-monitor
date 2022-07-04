import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const initialState = {
  episodes: [],
  genericSnackbar: { show: false, message: '', type: 'info' },
}

export default new Vuex.Store({
  state: initialState,
  getters: {
    getEpisodes: state => state.episodes,
    genericSnackbar: state => state.genericSnackbar,
  },
  mutations: {
    setEpisodes: (state, episodes) => { state.episodes = episodes },
    addEpisode: (state, episode) => { state.episodes.push(episode) },
    deleteEpisode: (state, id) => { state.episodes = state.episodes.filter(episode => episode.id !== id) },
    modifyEpisode: (state, episode) => { state.episodes = state.episodes.map(e => (e.id === episode.id ? episode : e)) },
    setGenericSnackbar: (state, value) => (state.genericSnackbar = value),
  },
  actions: {
  },
  modules: {
  }
})
