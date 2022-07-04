<template>
    <v-container fluid fill-height style="background-color: black;">

        <!--Imagen de fondo-->
        <div id="background"></div>

        <!--Tarjeta en el centro-->
        <v-row justify="center">
            <v-col cols="12" xs="12" sm="8" md="5" lg="4" xl="3">
                <v-card class="rounded-lg">
                    <v-toolbar dark color="primary">
                        <v-toolbar-title>{{ title }}</v-toolbar-title>
                    </v-toolbar>

                    <v-card-text>
                        <slot/> <!-- The form -->
                    </v-card-text>

                    <v-card-actions >
                        <v-btn 
                            @click="action"
                            :disabled="!valid"
                            color="primary" style="width: 100%" x-large block class="rounded-lg"
                            >
                            {{ actionName }}
                        </v-btn>
                    </v-card-actions>

                    <v-card-text class="text-right">
                        <slot name="info" /> <!-- Other info to be displayed -->
                    </v-card-text>

                    <v-progress-linear v-if="loading" indeterminate/>
                </v-card>
                
            </v-col>
        </v-row>     
        <span class="version">v{{ version() }}</span>
    </v-container>
</template>

<script>
import { VERSION } from '@/global/Variables';
export default {
    props: {
        title: String,
        icon: String,
        action: Function,
        actionName: String,
        valid: Boolean,
        loading: Boolean,
    },
    methods: {
        version() {
            return VERSION
        }
    }
};
</script>

<style>
#background {
    position: fixed;
    top: 0;
    left: 0;
    height: 100%;
    width: 100%;
    opacity: 1;
    background-image: url("@/assets/folded-hands.jpg");
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
    filter: grayscale(0.5) brightness(0.7) blur(3px);
}
.version {
    position: absolute;
    bottom: 2px;
    right: 2px;
    color: #fff;
    font-size: 0.8rem;
}
</style>
