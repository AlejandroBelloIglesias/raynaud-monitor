<template>
    <v-navigation-drawer
        clipped
        absolute temporary 
        permanent
    >
        <v-list
        dense
        >
            <v-list-item-group
                v-model="group"
                active-class="deep-purple--text text--accent-4"
            >
                <v-list-item
                    v-for="(item, k) in items"
                    :key="k"
                    :to="item.to"
                >
                    <v-list-item-content>
                        <v-list-item-title>
                            <v-icon left>{{ item.icon }}</v-icon>
                            <span>{{ item.text }}</span>
                        </v-list-item-title>
                    </v-list-item-content>
                </v-list-item>


            </v-list-item-group>
        </v-list>
    </v-navigation-drawer>
</template>

<script>
export default {
    data() {
        return {
            group: null,
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