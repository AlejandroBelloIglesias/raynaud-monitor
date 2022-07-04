<template>
  <div>
    
    <Header @drawertoggle="drawerToggle()"/>
    <Drawer v-if="drawer" />


    <v-container>
      <!-- Grid of cards -->
    <v-expansion-panels style="margin-bottom: 100px;">
      <v-row dense>
        <v-col 
          v-for="(episode, i) in getEpisodes"
          :key="i"
          class=" col-12 col-sm-6 col-md-4 col-lg-3"
        >
          <v-expansion-panel :class="i%2==0 ? 'list-odd' : 'list-even'">
            <v-expansion-panel-header disable-icon-rotate>
              <v-container>

                <v-row class="text-h6">
                  {{ format(episode.date_time) }}
                </v-row>

                <!-- Grid of body_parts -->
                <v-row class="text-body-1 pt-4 grey--text text--darken-2">
                  <v-col 
                    v-for="(body_part, k) in episode.body_parts" :key="k" 
                    class="col-4 pa-0 "
                  >
                    -{{ body_part.name }}
                  </v-col>
                </v-row>
                </v-container>
                
                <!--Buttons-->
                <template v-slot:actions>
                    <v-tooltip top v-for="(action, i) in tooltips" :key="i" @click.stop="action.callback(episode)">
                        <template #activator="{ on }">
                            <v-hover v-slot="{ hover }">
                                <v-btn
                                    @click.stop="action.callback(episode)"
                                    v-on="on"
                                    :color="hover ? 'primary' : ''"
                                    small
                                    icon
                                    class="ml-2"
                                >
                                    <v-icon>{{ action.icon }}</v-icon>
                                </v-btn>
                            </v-hover>
                        </template>
                        <span>{{ action.text }}</span>
                    </v-tooltip>
                </template>
              
            </v-expansion-panel-header>
            <v-expansion-panel-content class="text-body-1 pt-4 grey--text text--darken-2">
              
              <v-row ><v-divider/></v-row>

              <v-row >
                <v-col>
                  Duración:
                </v-col>
                <v-col>
                  {{ episode.duration }} min
                </v-col>
              </v-row>

              <v-row >
                <v-col>
                  Temperatura:
                </v-col>
                <v-col>
                  {{ episode.temperature }} ºC
                </v-col>
              </v-row>

              <v-row >
                <v-col>
                  Estrés:
                </v-col>
                <v-col>
                  {{ episode.stress_level }}
                </v-col>
              </v-row>

              <v-row >
                <v-col>
                  Cigarros / día:
                </v-col>
                <v-col>
                  {{ episode.daily_cigarette_smoked }}
                </v-col>
              </v-row>

            </v-expansion-panel-content>
            
          </v-expansion-panel>
        </v-col>
      </v-row>
      </v-expansion-panels>

      <!-- Insert button opens a dialog -->
      <insert-button
        :action="openEpisodeForm"
      />

      <!-- Insert dialog -->
      <v-scale-transition hide-on-leave>
        <episode-form
          ref="episodeForm"
        />
      </v-scale-transition>
      <Navigation/>
    </v-container>
  </div>
</template>

<script>
// Fetch
import Episodes from '@/global/fetch/Episodes'

// Utils
import DateFormatter from '@/global/utils/DateFormatter'

// Components
import InsertButton from '../components/InsertButton.vue'
import Header from '../components/Header.vue'
import Drawer from '../components/Drawer.vue'
import Navigation from '../components/Navigation.vue'
import EpisodeForm from '@/views/dialogs/EpisodeForm.vue'

// Import vuex getters
import { mapGetters, mapMutations } from 'vuex'

export default {
  components: { 
    InsertButton,
    Header,
    Drawer,
    Navigation,
    EpisodeForm
  },
  data() {
    return {
      drawer: false,
    }
  },
  computed: {
    ...mapGetters(['getEpisodes']),
    tooltips() {
      return [
        {
          text: 'Editar',
          icon: 'mdi-pencil',
          callback: this.openModifyDialog
        },
        {
          text: 'Eliminar',
          icon: 'mdi-delete',
          callback: this.delete,
          color: 'error'
        }
      ]
    },
  },
  methods: {
    ...mapMutations(['addEpisode', 'deleteEpisode', 'modifyEpisode', 'setGenericSnackbar']),
    ...DateFormatter,
    openEpisodeForm() {
      this.$refs.episodeForm.open(null, this.insert)
    },
    openModifyDialog(episode) {
      this.$refs.episodeForm.open(episode, this.modify)
    },
    async insert(episode) {
      const response = await Episodes.insert(episode)
      if (response) {
        this.addEpisode(response)
        this.setGenericSnackbar({
          show: true,
          type: 'success',
          message: 'Episodio insertado correctamente'
        })
      } else {
        this.setGenericSnackbar({
            show: true,
            type: 'error',
            message: 'Error al insertar episodio'
        })
      }
    },
    async delete(episode) {
      console.log(episode);
      const response = await Episodes.delete(episode.id)
      if (response) {
        this.deleteEpisode(episode.id)
        this.setGenericSnackbar({
          show: true,
          type: 'success',
          message: 'Episodio eliminado correctamente'
        })
      } else {
        this.setGenericSnackbar({
            show: true,
            type: 'error',
            message: 'Error al eliminar episodio'
        })
      }
    },
    async modify(episode) {
      // Take only string from body_parts
      episode.body_parts = episode.body_parts.map(body_part => body_part.name)
      const response = await Episodes.modify(episode)
      if (response) {
        this.modifyEpisode(episode)
        this.setGenericSnackbar({
          show: true,
          type: 'success',
          message: 'Episodio modificado correctamente'
        })
      } else {
        this.setGenericSnackbar({
            show: true,
            type: 'error',
            message: 'Error al modificar episodio'
        })
      }
    },
    drawerToggle() {
      this.drawer = !this.drawer
    },
  },
}
</script>
