<template>
    <v-flex mb-12>
        <v-form
          ref="form"
        >
          <v-text-field
            v-model="query"
            label="Search term"
            required
          ></v-text-field>

          <v-btn
            color="success"
            @click="submit"
          >
            Validate
          </v-btn>

          <v-btn
            color="error"
            @click="reset"
          >
            Reset Form
          </v-btn>

        </v-form>
    </v-flex>
</template>

<script>

import { serverBus } from '../main'


export default {
    data: () => ({
        query: '',
        server: 'this is a server'
    }),
    methods: {
      submit() {
        const baseURI = "https://api.coindesk.com/v1/bpi/currentprice.json"
        this.$http.get(baseURI)
        .then((result) => {
          serverBus.$emit('queryCompleted',JSON.stringify(result))
        })
      },
      reset() {
        this.query = ''
        serverBus.$emit('resetQuery','')
      },
    }
}
</script>

<style>

</style>


