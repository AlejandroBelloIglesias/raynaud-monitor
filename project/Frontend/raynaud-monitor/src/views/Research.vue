<template>
<div>
    
    <Header @drawertoggle="drawerToggle()"/>
    <Drawer v-if="drawer" />

    <v-container>
        <!-- Grid of cards -->
        <v-row>
            <v-col 
                v-for="(study, i) in studies" :key="i"
                class=" col-12 col-sm-6 col-md-4 col-lg-3"
            >
            <v-card 
                :class="i%2==0 ? 'list-odd' : 'list-even'"
                >
                <v-img height="250" :src="study.img"/>
                <v-card-title>{{ study.title }}</v-card-title>
                <v-card-subtitle>{{ study.subtitle }}</v-card-subtitle>
                <v-card-text>{{ study.text }}</v-card-text>
                <v-card-actions>
                    <v-btn text :href="study.url" target="_blank" color="blue">
                        <v-icon class="mr-2">mdi-link</v-icon> Ir al estudio
                    </v-btn>
                </v-card-actions>
            </v-card>
            </v-col>
        </v-row>

    </v-container>

    <Navigation />

</div>
</template>
<script>

// Components
import InsertButton from '../components/InsertButton.vue'
import Header from '../components/Header.vue'
import Drawer from '../components/Drawer.vue'
import Navigation from '../components/Navigation.vue'

export default {
    data () {
      return {
        drawer: false,
      }
    },
    components: {
        InsertButton,
        Header,
        Drawer,
        Navigation
    },
    computed: {
        items() {
            return [
                {
                    text: 'Episodes',
                    icon: 'mdi-text-box-outline',
                    to: '/'
                },
                {
                    text: 'Charts',
                    icon: 'mdi-chart-line',
                    to: '/charts'
                },
                {
                    text: 'Studies',
                    icon: 'mdi-flask',
                    to: '/research'
                }
            ]
        },
        studies() {
            return [
                {
                    url: 'https://pubmed.ncbi.nlm.nih.gov/10789602/',
                    img: 'https://www.lavozdegalicia.es/default/2019/03/18/00121552944542761937120/Foto/GM19P48F2_222729.jpg',
                    title: 'Tratamiento con Nifedipino.',
                    subtitle: 'Reduce en un 66% el número de ataques.',
                    text: 'Nifedipino es un medicamento prescrito que reduce el ritmo cardiaco y la presión arterial.\n'
                        + 'El tratamiento con Nifedipino reduce en un 66% el número de ataques según este estudio de 313 personas.'
                },
                {
                    url: 'https://pubmed.ncbi.nlm.nih.gov/2182173/',
                    img: 'https://www.collinsdictionary.com/images/full/cigarette_364716302.jpg',
                    title: 'Fumar aumenta el riesgo de ataques.',
                    subtitle: 'Reduce el flujo sanguíneo y dificulta la circulación.',
                    text: 'En los fumadores regulares, se demostró una marcada caída en el flujo sanguíneo de los dedos, a diferencia de los no fumadores o en los fumadores irregulares.'
                },
                {
                    url: 'https://pbs.twimg.com/media/EcmOZEOXsAAvbJg.jpg',
                    img: 'https://pbs.twimg.com/media/EcmOZEOXsAAvbJg.jpg',
                    title: 'Lorem ipsum dolor sit amet',
                    subtitle: 'Consectetur adipiscing elit. Morbi ut diam faucibus',
                    text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi ut diam faucibus, dignissim tellus non, sodales elit. Praesent venenatis diam et ex pharetra, ut malesuada lorem finibus. Quisque venenatis nunc egestas eros sollicitudin facilisis. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Etiam pharetra facilisis arcu, eget scelerisque sapien hendrerit sed. Duis augue leo, imperdiet ac sem vitae, cursus venenatis turpis. Praesent a orci a mi porttitor viverra et laoreet sem.'
                },
                                {
                    url: 'https://preview.redd.it/0z7q7w1e1so61.jpg?auto=webp&s=f906dd86e31f103347aeb97ca7a7aa08ba80dce8',
                    img: 'https://preview.redd.it/0z7q7w1e1so61.jpg?auto=webp&s=f906dd86e31f103347aeb97ca7a7aa08ba80dce8',
                    title: 'Lorem ipsum dolor sit amet',
                    subtitle: 'Consectetur adipiscing elit. Morbi ut diam faucibus',
                    text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi ut diam faucibus, dignissim tellus non, sodales elit. Praesent venenatis diam et ex pharetra, ut malesuada lorem finibus. Quisque venenatis nunc egestas eros sollicitudin facilisis. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Etiam pharetra facilisis arcu, eget scelerisque sapien hendrerit sed. Duis augue leo, imperdiet ac sem vitae, cursus venenatis turpis. Praesent a orci a mi porttitor viverra et laoreet sem.'
                },

            ]
        }
    },
    methods: {
        drawerToggle() {
            this.drawer = !this.drawer
        },
    }
}
</script>