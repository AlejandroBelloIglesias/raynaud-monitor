<template>
  <v-app>
    <v-snackbar
            transition="scale-transition"
            v-model="genericSnackbar.show"
            color="transparent"
            elevation="0"
            :timeout="3000"
            bottom
            app
            style="z-index: 999"
        >
        <v-alert
            transition="scale-transition"
            v-model="genericSnackbar.show"
            :type="genericSnackbar.type"
            border="left"
            dismissible
        >
            {{ genericSnackbar.message }}
        </v-alert>
    </v-snackbar>
    
    <v-main>
      <router-view/> 
    </v-main>
  </v-app>
</template>

<script>
// Fetch
import BodyParts from '@/global/fetch/BodyParts'
import Episodes from '@/global/fetch/Episodes'

// Vuex
import { mapMutations, mapGetters } from 'vuex'

export default {
  methods: {
    ...mapMutations(['setEpisodes']),
  },
  computed: {
    ...mapGetters(['genericSnackbar']),
  },
  async mounted() {
    localStorage.setItem('bodyParts', JSON.stringify(await BodyParts.getAll()))

    const token = localStorage.getItem('token')
    const sessionExpires = localStorage.getItem('sessionExpires')
    const now = new Date().getTime()

    if (token && sessionExpires && now < sessionExpires) {
      const episodes = await Episodes.getAll() //Fetch episodes
      this.setEpisodes(episodes) //Save them into vuex
    }
  }
}

</script>
<style>
html {
  overflow-y: auto !important; /* Fix, quita la barra de scroll innecesaria */
}
</style>