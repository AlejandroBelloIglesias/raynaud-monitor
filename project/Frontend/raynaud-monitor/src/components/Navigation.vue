<template>
    <v-bottom-navigation app background-color="primary" dark v-if="$vuetify.breakpoint.smAndDown">

        <v-btn v-for="item, k in items" :key="k"
            :to="item.to"
            class="no-hover"
        >
            <span>{{ item.text }}</span>
            <v-icon>{{ item.icon }}</v-icon>
        </v-btn>

    </v-bottom-navigation>
</template>

<script>
export default {
    data () {
      return {
        active: true,
      }
    },
    computed: {
        items() {
            return [
                {
                    text: 'Episodios',
                    icon: 'mdi-text-box-outline',
                    to: '/'
                },
                {
                    text: 'Gráficos',
                    icon: 'mdi-chart-line',
                    to: '/charts'
                },
                {
                    text: 'Estudios',
                    icon: 'mdi-flask',
                    to: '/research'
                }
            ]
        }
    },
}
</script>
<style scoped>
.no-hover::before {
   background-color: transparent !important;
}
</style>