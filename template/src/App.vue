<template>
  <div id="app">
    <!-- <img src="./assets/logo.png"> -->
    <!-- <h1>{{ datetime }}</h1> -->
    <router-view />
  </div>
</template>

<!-- <script>
export default {
  name: 'App'
  data () { return { datetime: 'eeeeeee' } },
  methods: {
    initData () { this.$ajax.get('/time', {}).then(res => { this.datetime = res.data.time }) } },
  mounted () { this.initData() } 
}
</script> -->

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
  height: 100%;
}
</style>
