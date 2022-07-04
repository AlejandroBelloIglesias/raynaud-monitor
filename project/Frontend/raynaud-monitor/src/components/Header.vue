<template>
   <div>
      <v-app-bar app color="primary" dark > 
         
         <div class="d-flex align-center">
            <!-- Este div impide que el título baje en shrink on scroll-->
            <v-btn icon dark @click="switchDrawer()" v-if="$vuetify.breakpoint.mdAndUp">  
               <v-icon>{{ drawer ? 'mdi-close' : 'mdi-menu' }}</v-icon>
            </v-btn>

            <v-img alt="Raynaud Monitor Logo" class="mr-2" src="@/../public/ice-icon.svg" width="50" v-if="$vuetify.breakpoint.smAndDown"/>
            <v-toolbar-title>Raynaud Monitor</v-toolbar-title>
            <v-img alt="Raynaud Monitor Logo" class="ml-2" src="@/../public/ice-icon.svg" width="30" v-if="$vuetify.breakpoint.mdAndUp"/>
         </div>

         <v-spacer />

         <!-- Menu logout -->
         <v-menu v-model="userMenu" transition="slide-y-transition" offset-y nudge-bottom="10">
            <template #activator="{ on }">
               <v-btn v-on="on" text icon>
                  <v-icon>mdi-account-circle</v-icon>
               </v-btn>
            </template>

            <v-card width="275">
               <v-card-subtitle class="d-flex flex-nowrap secondary">
                  <span class="text-truncate white--text">{{ accountEmail }}</span>
                  <v-btn @click="userMenu = false" dark icon absolute right style="top: 10px">
                     <v-icon>mdi-close</v-icon>
                  </v-btn>
               </v-card-subtitle>

               <v-divider />

               <v-list-item v-for="(item, i) in compressedActions" :key="i" @click="item.onClick">
                  <v-list-item-icon>
                     <v-icon>{{ item.icon }}</v-icon>
                  </v-list-item-icon>
                  <v-list-item-content>
                     <v-list-item-title>{{ item.label }}</v-list-item-title>
                  </v-list-item-content>
               </v-list-item>

            </v-card>
         </v-menu>

      </v-app-bar>
      
         
  </div>
</template>
<script>
import { mapState } from "vuex";
import Access from "@/global/fetch/Access";

// Utils
import DataProcessor from '@/global/utils/DataProcessor.js'

// Vuex mutations
import { mapMutations } from "vuex";

export default {
   data() {
      return {
         userMenu: false, drawer: false,
         accountEmail: "undefined",
         group: null,
      }
   },
   methods: {
      ...mapMutations(["setEpisodes"]),
      logout() {
         Access.logout();
      },
      demoData() {
         this.setEpisodes(DataProcessor.demoData());
      },
      switchDrawer() {
         this.drawer = !this.drawer;
         this.$emit("drawertoggle", this.drawer);
      },
   },
   mounted() {
      if (localStorage.getItem("user")) {
         this.accountEmail = JSON.parse(localStorage.getItem("user")).email;
      } else {
         this.$router.push("/login");
      }
   },
   computed: {
      compressedActions() {
         return [
            {
               icon: 'mdi-database-clock',
               onClick: this.demoData,
               label: 'Demostración de datos',
            },
            {
               icon: 'mdi-logout',
               onClick: this.logout,
               label: 'Salir de la cuenta',
            },
         ]
      },
   },
};
</script>