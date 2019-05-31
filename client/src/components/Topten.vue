<template>
    <v-container>
        <v-layout
          text-xs-center
          wrap
        >

        <v-flex mb-4>
            <v-layout justify-center>
            <ol>
                <li
                    v-for="(next, i) in topTenData"
                    :key="i"
                    class="subheading mx-3"
                    target="_blank"
                >
                    {{ next.word }} : {{next.value}}
                </li>
            </ol>
            </v-layout>
        </v-flex>

        </v-layout>
    </v-container>
</template>

<script>
export default {
    data: () => ({
        topTenData: [
            {word: "the", value: 10},
            {word: "and", value: 9},
            {word: "power", value: 8},
        ]
    }),
    methods: {
        fetchTopTen: function() {
            const getTopTenURI = ''
            this.$http.get(getTopTenURI)
            .then((result) => {
                this.topTenData = result
            })
        }
    }
}
</script>

<style scoped>
    ol {
        border: 2px solid black;
    }
</style>


