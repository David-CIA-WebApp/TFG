<template>
  <div id="login">
    <div v-if="!logged">
      <p>ADMINISTRACIÓN</p>
      <Login @logging="logging"/>
      <p style="color: red;">{{messageAccess}}</p>
    </div>

    <table class="table table-striped" id="users" v-if="logged">
      <thead>
        <tr>
          <th>Nombre</th>
          <th>Apellidos</th>
          <th>DNI</th>
          <th>Correo</th>
          <th>Dirección</th>
          <th>Telefono</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(user,i) in users" :key="i">
          <td>{{ user.nombre }}</td> 
          <td>{{ user.apellidos }}</td> 
          <td>{{ user.dni }}</td> 
          <td>{{ user.email }}</td> 
          <td>{{ user.direccion }}</td> 
          <td>{{ user.telefono }}</td> 
        </tr>
      </tbody>
    </table>

    <br><br>

    <table class="table table-striped" id="users" v-if="logged">
      <thead>
        <tr>
          <th>Nombre</th>
          <th>Apellidos</th>
          <th>DNI</th>
          <th>Correo</th>
          <th>Dirección</th>
          <th>Telefono</th>
          <th>Contraseña</th>
          <th>Función</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(worker,i) in workers" :key="i">
          <td>{{ worker.nombre }}</td> 
          <td>{{ worker.apellidos }}</td> 
          <td>{{ worker.dni }}</td> 
          <td>{{ worker.email }}</td> 
          <td>{{ worker.direccion }}</td> 
          <td>{{ worker.telefono }}</td> 
          <td>{{ worker.pass }}</td> 
          <td>{{ worker.tipo }}</td> 
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import Login from "../components/Login";
import axios from 'axios';

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
    logging(data) {
      this.logged = data;
      if (!data) {
        this.messageAccess = "Acceso denegado. El usuario introducido no existe o la contraseña no es correcta";
      } else {
        this.messageAccess = "";
      }
    },
    loadUsers() {
      const path = `${process.env.VUE_APP_BACK_URL}/users`;
      const config = {
        method: 'get',
        url: path,
        data: {
          "mail": this.mail, 
          "password": this.password
        },
        headers: {
          "Content-Type": "application/JSON",
          "Access-Control-Allow-Origin": "*",
          "Authorization": "0i234c6c89"
        }
      }
      axios(config)
      .then((res) => {
        for (let index = 0; index < res.data.length; index++) {
          var element = res.data[index];
          this.users[index] = element;
        }
      });
      config.url = `${process.env.VUE_APP_BACK_URL}/workers`;
      axios(config)
      .then((res) => {
        for (let index = 0; index < res.data.length; index++) {
          var element = res.data[index];
          this.workers[index] = element;
        }
      });
      config.url = `${process.env.VUE_APP_BACK_URL}/externalWorkers`;
      axios(config)
      .then((res) => {
        for (let index = 0; index < res.data.length; index++) {
          var element = res.data[index];
          this.externalWorkers[index] = element;
        }
      });
      config.url = `${process.env.VUE_APP_BACK_URL}/clients`;
      axios(config)
      .then((res) => {
        for (let index = 0; index < res.data.length; index++) {
          var element = res.data[index];
          this.clients[index] = element;
        }
      });
      config.url = `${process.env.VUE_APP_BACK_URL}/gestores`;
      axios(config)
      .then((res) => {
        for (let index = 0; index < res.data.length; index++) {
          var element = res.data[index];
          this.economyManagers[index] = element;
        }
      });
    },
  },
  mounted() {
    this.loadUsers();
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
