<template>
  <div>
    <div id="menu" v-if="logged">
      <button 
      style="background-color: blue; color: white; margin-top: 0px; margin-left: 0px;"
      @click="redirectUser">
        USUARIOS
      </button>
      <button 
      style="background-color: blue; color: white; margin-top: 0px; margin-left: 0px;"
      @click="redirectMaterial">
        MATERIALES
      </button>
      <button 
      style="background-color: transparent; color: red; margin-top: 0px; float: right;"
      @click="closeSession">
        Cerrar Sesión
      </button>
    </div>  

    <div id="login">
      <div v-if="!logged">
        <p>ADMINISTRACIÓN</p>
        <Login @logging="loggingFunction"/>
        <p style="color: red;">{{messageAccess}}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
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
          }
          
          this.$emit("logging", this.logged);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    redirectUser() {
      this.$router.push('users');
    },
    redirectMaterial() {
      this.$router.push('materials');
    },
    closeSession() {
      localStorage.userMail = "";
      localStorage.userPass = "";
      localStorage.userType = "";
      this.$router.go();
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
