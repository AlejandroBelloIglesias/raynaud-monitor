<!--
    Common button component for inserting registers into any crud view.
    Props:
        action: The function to be triggered when user clicks the component. For example: newUser(), addBuilding(), addAccount() ...
-->
<template>    
    <v-hover v-slot="{ hover }">
        <v-btn
            @click="action"
            fab fixed
            class="btn-fix"
            :style="position"
            :color="hover ? 'secondary' : 'primary'"
        >
            <v-icon>mdi-plus</v-icon>
        </v-btn>
    </v-hover>
</template>
<script>
export default {
    props: {
        action: Function
    },
    computed: {
        position() {
            const bottom = (this.$vuetify.breakpoint.smAndDown) ? '80px' : '40px';
            const right = (this.$vuetify.breakpoint.smAndDown) ? '20px' : '40px';
            return {
                position: 'fixed',
                bottom: bottom,
                right: right
            }
        }
    },
}
</script>
<style scoped>
.btn-fix:focus::before { 
    /* Fix porque se quedaba focus/pulsado al volver */
    opacity: 0 !important; 
}
</style>