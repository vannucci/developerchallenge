<template>
  <v-app>
    <v-toolbar app>
      <v-toolbar-title class="headline text-uppercase">
        <span>Top Ten Twitter</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
        flat
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
      >
        <span class="mr-2">Latest Release</span>
      </v-btn>
    </v-toolbar>

    <v-content>
      <HelloWorld/>
      <Topten/>
      <Searchresults/>
    </v-content>
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld'
import Topten from './components/Topten.vue'
import Searchresults from './components/Searchresults'



export default {
  name: 'App',
  components: {
    HelloWorld,
    Topten,
    Searchresults
  },
  data () {
    return {
      //
    }
  }
}
</script>
