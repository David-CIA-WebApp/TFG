<template>
  <div>
      <button 
      style="background-color: transparent; color: red; margin-top: 0px; float: right; top: -300px;"
      @click="closeSession">
        Cerrar Sesión
      </button>

    <div id="menu">
      <div v-if="logged">
        <Menu @handleClick="handleClick"/>
        <a href="/alertas" class="alertasAdmin"><svg viewBox="0 0 15 1" width="32" height="30"><path id="lineBC" d="M 1 1 L 1 2 L 11 2 L 11 1 L 10 0 C 9 -8 3 -8 2 0 L 1 1 M 6 3 A 1 1 0 0 0 6 6 A 1 1 0 0 0 6 3" stroke="black" stroke-width="0.01"  /></svg></a>
      </div>
    </div>

    <div id="login">
      <div v-if="!logged">
        <Login @logging="loggingFunction"/>
        <p style="color: red;">{{messageAccess}}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Login from "../components/Login";
import Menu from "../components/Menu";

export default {
  name: 'Admin',
  components: {
    Login,
    Menu
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
      load: false,
      token: null
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
      const path = `${process.env.VUE_APP_BACK_URL}/login`;
      const config = {
        method: 'post',
        url: path,
        data: {
          "mail": localStorage.userMail, 
          "password": localStorage.userPass
        },
        headers: {
          "Content-Type": "application/JSON",
          "Access-Control-Allow-Origin": "*"
        }
      };
      axios(config)
        .then((res) => {
          if (res.data.accepted) { 
            this.logged = true;
            this.token = res.data.token;
          }
          
          this.$emit("logging", this.logged);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    closeSession() {
      localStorage.userMail = "";
      localStorage.userPass = "";
      localStorage.userType = "";
      this.$router.go();
    },
    handleClick (item) {
        if (item == 'USUARIOS') this.redirectUser();
        else if (item == 'MATERIALES') this.redirectMaterial();
        else if (item == 'AGENDA') this.redirectAgenda();
        else if (item == 'TRABAJOS') this.redirectJobs();
        else if (item == 'CONSULTAS') this.redirectConsults();
        else if (item == 'PROVEEDORES') this.redirectProveedores();
    },
    redirectUser() {
      this.$router.push('users');
    },
    redirectMaterial() {
      this.$router.push('materials');
    },
    redirectAgenda() {
      this.$router.push('agenda');
    },
    redirectJobs() {
      this.$router.push('jobs');
    },
    redirectConsults() {
      this.$router.push('consultas');
    },
    redirectProveedores() {
      this.$router.push('proveedores');
    },
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
.alertasAdmin {
    position: absolute;
    top: 7px;
    left: 10px;
    margin-top: 0px;
    margin-right: 0px;
    padding: 0px;
    width: 30px;
    height: 30px;
    border-radius: 50%;
    color: white;
    font-size: 20px;
    text-align: center;
    line-height: 30px;
    cursor: pointer;
}
</style>
