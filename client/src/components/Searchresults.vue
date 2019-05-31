<template>
  <div class="text-xs-center">
    <p>
        here: {{queryResult}}
    </p>

    <v-pagination
      v-model="page"
      :length="6"
    ></v-pagination>
  </div>
</template>

<script>
    import { serverBus } from '../main'

    export default {
        data () {
            return {
                page: 1,
                queryResult: null
            }
        },
        created() {
            serverBus.$on('queryCompleted', (queryResult) => {
                this.queryResult = queryResult
            })
            serverBus.$on('resetQuery', (reset) => {
                this.queryResult = reset
            })
        }
    }
</script>

<style>

</style>


