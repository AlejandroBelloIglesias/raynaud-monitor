<template>
    <div>
        <Header @drawertoggle="drawerToggle()"/>
        <Drawer v-if="drawer" />
        
        <v-container>
            <v-row dense>
                <v-col class="col-12 col-md-6">
                    <v-card>
                        <!-- Centered tabs -->
                        <v-tabs centered>
                            <v-tab 
                                v-for="(tab, k) in summaryTabs" :key="k"
                                @click="tab.action"
                            >
                                {{ tab.name }}
                            </v-tab>
                        </v-tabs>
                        <apexchart type="bar" :options="summaryChart.options" :series="summaryChart.series"></apexchart>
                    </v-card>
                </v-col>
                <v-col class="col-12 col-md-6">
                    <v-card>
                        <apexchart type="bar" :options="episodesByTemperature.options" :series="episodesByTemperature.series"></apexchart>
                    </v-card>
                </v-col>
            </v-row>
        </v-container>
        
        <Navigation/>
    </div>
</template>


<script>
    // Components
    import Header from '../components/Header.vue'
    import Navigation from '../components/Navigation.vue'
    import Drawer from '@/components/Drawer.vue'

    // Utils
    import DataProcessor from '@/global/utils/DataProcessor.js'

    // Import vuex getters
    import { mapGetters, mapMutations } from 'vuex'

    export default {
        components: {
            Header,
            Navigation,
            Drawer
        },
        data() {
            return {
                drawer: false,
                summaryTab: 'year',
            }
        },
        methods: {
            ...mapMutations(['setGenericSnackbar']),
            drawerToggle() {
                this.drawer = !this.drawer
            },
            
        },
        computed: {
            ...mapGetters(['getEpisodes']),
            summaryTabs() {
                return [
                    {
                        name: 'Año',
                        action: () => {
                            this.summaryTab = 'year'
                        }
                    },
                    {
                        name: 'Mes',
                        action: () => {
                            this.summaryTab = 'month'
                        }
                    },
                ]
            },
            summaryChart() {
                switch (this.summaryTab) {
                    case 'year':
                        return this.yearSummaryByMonth
                    case 'month':
                        return this.monthSummaryByDay
                }
            },
            yearSummaryByMonth() {
                const thisYear = new Date().getFullYear()
                let data = DataProcessor.yearSummaryByMonth(this.getEpisodes, thisYear)
                return {
                    options: {
                        chart: {
                            id: 'yearSummaryByMonth',
                        },
                        xaxis: {
                            categories: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
                        },
                        yaxis: {
                            title: {
                                text: 'Número de episodios'
                            }
                        },
                    },
                    series: [{
                        name: thisYear,
                        data: data
                    }]
                }
            },
            monthSummaryByDay() {
                const thisMonth = new Date().getMonth()
                let data = DataProcessor.monthSummaryByDay(this.getEpisodes, thisMonth)
                let categories = []
                for (let i = 1; i <= data.length; i++) {
                    categories.push(i)
                }
                return {
                    options: {
                        chart: {
                            id: 'monthSummaryByDay',
                        },
                        xaxis: {
                            categories: categories,
                            labels: {
                                rotate: -80
                            },
                        },
                        yaxis: {
                            title: {
                                text: 'Número de episodios'
                            }
                        },
                    },
                    series: [{
                        name: thisMonth,
                        data: data
                    }]
                }
            },
            episodesByTemperature() {
                let epByTemp = DataProcessor.episodesByTemperature(this.getEpisodes)
                return {
                    options: {
                        chart: {
                            id: 'episodesByTemperature',
                        },
                        xaxis: {
                            categories: epByTemp.map(ep => ep.temp)
                        },
                        yaxis: {
                            title: {
                                text: 'Nº de episodios por temperatura'
                            }
                        },
                    },
                    series: [{
                        name: 'Episodios',
                        data: epByTemp.map(ep => ep.episodes.length)
                    }]
                }
            }
        },
        mounted() {
            if (this.getEpisodes.length < 50) {
                this.setGenericSnackbar({
                    show: true,
                    type: 'warning',
                    message: 'No hay suficientes episodios para generar buenos gráficos',
                })
            }
        }
    }

</script>