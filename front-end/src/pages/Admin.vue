<template>
  <div id="login">
    <div v-if="!logged">
      <p>ADMINISTRACIÓN</p>
      <Login @logging="loggingFunction"/>
      <p style="color: red;">{{messageAccess}}</p>
    </div>

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
      logged: false,
      messageAccess: "",
      users: [],
      workers: [],
      externalWorkers: [],
      economyManagers: [],
      clients: [],
      load: false
    }
  },
  methods: {
    loggingFunction(data) {
      this.logged = data;
      if (!data) {
        this.messageAccess = "Acceso denegado. El usuario introducido no existe o la contraseña no es correcta";
      } else {
        this.messageAccess = "";
      }
    },
    loadData() {
      this.logged = localStorage.logged == 'true';
    }
  },
  mounted() {
    this.loadData();
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
#users {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#users td, #users th {
  border: 1px solid #ddd;
  padding: 8px;
}

#users tr:nth-child(even){background-color: #f2f2f2;}

#users tr:hover {background-color: #ddd;}

#users th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: hsl(214, 95%, 34%);
  color: white;
}

</style>
