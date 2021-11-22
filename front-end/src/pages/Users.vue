<template>
  <div id="login">

    <p style="color: red;">{{messageAccess}}</p>
    <div v-if="forceReload && logged">
    <h3>USUARIOS</h3>
      <table class="table table-striped" id="users">
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
            <td @click="test(user)">{{ user.nombre }}</td> 
            <td>{{ user.apellidos }}</td> 
            <td>{{ user.dni }}</td> 
            <td>{{ user.email }}</td> 
            <td>{{ user.direccion }}</td> 
            <td>{{ user.telefono }}</td> 
          </tr>
        </tbody>
      </table>

      <br><br>

      <h3>TRABAJADORES INTERNOS</h3>
      <table class="table table-striped" id="users">
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

      <br><br>

      <h3>TRABAJADORES EXTERNOS</h3>
      <table class="table table-striped" id="users">
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Apellidos</th>
            <th>DNI</th>
            <th>Correo</th>
            <th>Dirección</th>
            <th>Telefono</th>
            <th>Función</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(ew,i) in externalWorkers" :key="i">
            <td>{{ ew.nombre }}</td> 
            <td>{{ ew.apellidos }}</td> 
            <td>{{ ew.dni }}</td> 
            <td>{{ ew.email }}</td> 
            <td>{{ ew.direccion }}</td> 
            <td>{{ ew.telefono }}</td> 
            <td>{{ ew.ocupacion }}</td> 
          </tr>
        </tbody>
      </table>

      <br><br>

      <h3>GESTORES</h3>
      <table class="table table-striped" id="users">
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
          <tr v-for="(em,i) in economyManagers" :key="i">
            <td>{{ em.nombre }}</td> 
            <td>{{ em.apellidos }}</td> 
            <td>{{ em.dni }}</td> 
            <td>{{ em.email }}</td> 
            <td>{{ em.direccion }}</td> 
            <td>{{ em.telefono }}</td> 
          </tr>
        </tbody>
      </table>

      <br><br>

      <h3>CLIENTES</h3>
      <table class="table table-striped" id="users">
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Apellidos</th>
            <th>DNI</th>
            <th>Correo</th>
            <th>Dirección</th>
            <th>Telefono</th>
            <th>Cliente potencial</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(client,i) in clients" :key="i">
            <td>{{ client.nombre }}</td> 
            <td>{{ client.apellidos }}</td> 
            <td>{{ client.dni }}</td> 
            <td>{{ client.email }}</td> 
            <td>{{ client.direccion }}</td> 
            <td>{{ client.telefono }}</td> 
            <td>{{ client.clientePotencial }}</td> 
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Admin',
  components: {
    
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
      forceReload: false
    }
  },
  methods: {
    loadUsers() {
      this.logged = localStorage.logged;
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
      
      setTimeout(() => {
      this.forceReload = true;
      }, 100);
    },
    test(user) {
      console.log(user.nombre);
    }
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
