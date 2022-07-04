<template>
    <v-dialog v-model="show" persistent scrollable :fullscreen="$vuetify.breakpoint.smAndDown" width="700">
        <v-card tile>

            <v-card-title class="py-2 primary">
                <v-icon left dark>mdi-text-box-plus-outline</v-icon>
                <span class="white--text">{{ modifying ? 'Modificar' : 'Insertar' }} episodio</span>
                <v-spacer />
                <v-btn dark icon @click="close()">
                    <v-icon>mdi-close</v-icon>
                </v-btn>
            </v-card-title>


            <v-card-text>
                <v-form v-model="valid" class="mt-5" :disabled="loading" lazy-validation >
                    
                    <!-- DATE PICKER -->
                    <v-menu
                        v-model="date_menu"
                        :close-on-content-click="false"
                        transition="scale-transition"
                        :nudge-right="40" offset-y
                        min-width="auto"
                    >
                        <template v-slot:activator="{ on, attrs }">
                            <v-text-field
                                v-model="episode.date"
                                label="Fecha"
                                prepend-icon="mdi-calendar"
                                counter="10"
                                v-bind="attrs"
                                v-on="on"
                                readonly
                                outlined
                            />
                        </template>

                        <v-date-picker
                        v-model="episode.date"
                        />
                    </v-menu>

                    <!-- TIME PICKER -->
                    <v-menu
                        v-model="time_menu"
                        :close-on-content-click="false"
                        transition="scale-transition"
                        :nudge-right="40" offset-y
                        min-width="auto"
                    >
                        <template v-slot:activator="{ on, attrs }">
                            <v-text-field
                                v-model="episode.time"
                                label="Hora"
                                prepend-icon="mdi-clock"
                                required counter="5"
                                v-bind="attrs"
                                v-on="on"
                                outlined
                            />
                        </template>

                        <v-time-picker
                        v-model="episode.time"
                        format="24hr"
                        />
                    </v-menu>

                    <!-- DURATION -->
                    <v-text-field
                        v-model.number="episode.duration"
                        label="Duración en minutos"
                        :rules="[rules.required, rules.min]" 
                        required counter="3" type="number"
                        prepend-icon="mdi-timer"
                        outlined
                    />

                    <!-- TEMPERATURE (pickeable)-->
                    <v-text-field
                        v-model.number="episode.temperature"
                        label="Temperatura"
                        :rules="[rules.notEmpty]"
                        required counter="3" type="number"
                        prepend-icon="mdi-thermometer"
                        outlined
                    >
                    <v-icon slot="append" color="primary" @click="getTemperature()">mdi-target</v-icon>
                    </v-text-field>
                    
                    <!-- DELIBERATED -->
                    <v-checkbox
                        v-model="episode.deliberated"
                        label="Deliberado"
                        color="primary"
                    />

                    <!-- STRESS LEVEL (0 to 5) -->
                    <v-slider
                        v-model="episode.stress_level"
                        label="Nivel de estrés"
                        :min="0" :max="5" ticks 
                        thumb-label
                        color="primary" 
                    />
            
                    <!-- DAILY CIGARETTES -->
                    <v-text-field
                        v-model.number="episode.daily_cigarette_smoked"
                        label="Cigarrillos diarios"
                        :rules="[rules.min]" 
                        required counter="2" type="number"
                        prepend-icon="mdi-smoking"
                        outlined
                    />

                    <!-- BODY PARTS AFFECTED required -->
                    <v-select
                        v-model="episode.body_parts"
                        :items="body_parts"
                        item-value="name" item-text="name"
                        multiple chips
                        label="Partes afectadas"
                        hint="Selecciona las partes afectadas"
                        required :rules="[rules.selectAtLeastOne]"
                        outlined
                    ></v-select>
                </v-form>
            </v-card-text>

            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn @click="close()" color="primary" dark>Cancelar</v-btn>
                <v-btn @click="doAction()" :disabled="!valid" color="primary" :dark="valid">
                    {{ modifying ? 'Modificar' : 'Insertar' }}
                </v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>

<script>
import Weather from '@/global/fetch/Weather'
export default {
    data() {
        return {
            action: null,
            show: false, loading: false, valid: false,
            date_menu: false, time_menu: false,
            episode: this.cleanEpisode(),
            body_parts: [],
            rules: {
                required: value => !!value || 'El campo es requerido.',
                notEmpty: value => value!=='' || 'El campo es requerido.',
                min: value => (parseInt(value) >= 0 || 'El campo debe ser mayor o igual a 0.'),
                selectAtLeastOne: value => value.length > 0 || 'Selecciona al menos una opción.'
            },
            modifying: false,
        }
    },
    methods: {
        async open(episode, action) {
            this.action = action
            if (episode) {
                this.body_parts = JSON.parse(await this.getBodyParts())
                this.episode = episode
                
                // Converting date_time to date and time
                this.episode.date = new Date(episode.date_time - new Date(episode.date_time).getTimezoneOffset() * 60000).toISOString().substr(0, 10)
                this.episode.time = new Date(episode.date_time - new Date(episode.date_time).getTimezoneOffset() * 60000).toISOString().substr(11, 5)

                this.modifying = true
                this.show = true
            } else {
                this.show = true
                this.body_parts = JSON.parse(await this.getBodyParts())
                this.getTemperature()
                this.episode = this.cleanEpisode()
            }
        },
        close() {
            this.show = false
            this.episode = this.cleanEpisode()
        },
        async doAction() {
            this.loading = true

            //Make date with date and time
            this.episode.date_time = new Date(this.episode.date + ' ' + this.episode.time).getTime()
            //Delete unnecessary properties
            delete this.episode.date
            delete this.episode.time
            
            // Encapsulate each body_part into an object with 'name'
            this.episode.body_parts = this.episode.body_parts.map(part => {
                return { name: part }
            })

            await this.action(this.episode)
            this.loading = false
            this.close()
        },
        cleanEpisode() {
            return {
                date: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
                time: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(11, 5),
                duration: 20,
                temperature: 0,
                deliberated: false,
                stress_level: 0,
                daily_cigarette_smoked: 0,
                body_parts: [],
            }
        },
        async getBodyParts() {
            return localStorage.getItem('bodyParts')
        },
        getTemperature() {
            this.loading = true
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition((position) => {
                    
                     Weather.getWeather(position.coords.latitude, position.coords.longitude )
                    .then(response => {
                        this.episode.temperature = Math.round(response.current.temp - 273.15)
                    })
                    .catch(error => {
                        console.log(error)
                    })

                })
            } else { 
                console.log("Geolocation is not supported by this browser.")
            }
            this.loading = false
        }
    },
}
</script>