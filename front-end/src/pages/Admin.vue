<template>
  <div id="login" v-if="!logged">
    <p>ADMINISTRACIÓN</p>
    <Login @logging="logging"/>
  </div>
</template>

<script>
import Login from "../components/Login";

export default {
  name: 'Admin',
  components: {
    Login
  },
  data() {
    return {
      logged: Login.logged
    }
  },
  methods: {
    logging(data) {
      this.logged = data;
      console.log(this.logged)
    }
  },
  mounted() {

  }
}
</script>

<style>
#login {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
