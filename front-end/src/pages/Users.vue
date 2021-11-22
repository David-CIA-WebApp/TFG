<template>
  <div id="users">

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
            <td><a href="#miModal" @click="test(user)"> {{ user.nombre }} </a></td> 
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
            <td><a href="#miModal" @click="test(worker)"> {{ worker.nombre }} </a></td> 
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
            <td><a href="#miModal" @click="test(ew)"> {{ ew.nombre }} </a></td> 
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
            <td><a href="#miModal" @click="test(em)"> {{ em.nombre }} </a></td> 
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
            <td><a href="#miModal" @click="test(client)"> {{ client.nombre }} </a></td> 
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

    <div style="width: 420px; margin-left: auto; margin-right: auto; margin-top: 200px; font-size: 10px;" class="typewriter" v-if="!logged">
      <h1>Sorry! This page is not available</h1>
    </div>

    <div id="miModal" class="modal">
      <div class="modal-contenido">
        <a href="#">X</a>
        <h3 style="margin-bottom: -2%;">{{actualUser.nombre}} - {{actualUser.dni}}</h3>
        <p>Nombre:</p>
        <input v-model="actualUser.nombre"/>
        <p>Apellidos:</p>
        <input v-model="actualUser.apellidos"/>
        <p>DNI:</p>
        <input v-model="actualUser.dni"/>
        <p>Dirección:</p>
        <input v-model="actualUser.direccion"/>
        <p>Teléfono:</p>
        <input v-model="actualUser.telefono"/>
        <p>Correo:</p>
        <input v-model="actualUser.email"/>

        <p v-if="actualUser.pass != null">Contraseña:</p>
        <input v-if="actualUser.pass != null" v-model="actualUser.pass"/>

        <p v-if="actualUser.tipo != null">Ocupación:</p>
        <input v-if="actualUser.tipo != null" v-model="actualUser.tipo"/>

        <p v-if="actualUser.ocupacion != null">Ocupación:</p>
        <input v-if="actualUser.ocupacion != null" v-model="actualUser.ocupacion"/>

        
      <button
        class="button"
        @click="actualizar()">
          Actualizar
      </button>
      
      <button
        class="button red"
        @click="eliminar()">
          Eliminar
      </button>
      </div>  
    </div>

  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Users',
  components: {
    
  },
  data() {
    return {
      logged: false,
      users: [],
      workers: [],
      externalWorkers: [],
      economyManagers: [],
      clients: [],
      forceReload: false,
      actualUser: {}
    }
  },
  methods: {
    loadUsers() {
      this.logged = localStorage.logged == 'true';

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
      this.actualUser = user;
    },
    actualizar() {

    },
    eliminar() {
      
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

.typewriter h1 {
  overflow: hidden; /* Ensures the content is not revealed until the animation */
  border-right: .15em solid orange; /* The typwriter cursor */
  white-space: nowrap; /* Keeps the content on a single line */
  margin: 0 auto; /* Gives that scrolling effect as the typing happens */
  letter-spacing: .15em; /* Adjust as needed */
  animation: 
    typing 3s steps(50, end),
    blink-caret .75s step-end infinite;
}
 
/* The typing effect */
@keyframes typing {
  from { width: 0 }
  to { width: 100% }
}
 
/* The typewriter cursor effect */
@keyframes blink-caret {
  from, to { border-color: transparent }
  50% { border-color: orange; }
}

.modal-contenido{
  background-color: #207fdd;
  width:300px;
  padding: 10px 20px;
  margin: 1% auto;
  position: relative;
}
.modal{
  background-color: rgba(0,0,0,.8);
  position:fixed;
  top:0;
  right:0;
  bottom:0;
  left:0;
  opacity:0;
  pointer-events:none;
  transition: all 1s;
}
#miModal:target{
  opacity:1;
  pointer-events:auto;
}
.modal-contenido p {
  margin-top: 5%;
  margin-bottom: 1%;
  color: white;
}
.modal-contenido input {
  width: 90%;
}

button {
  margin-top: 5%;
  position: relative;
  background-color: #129232;
  border: none;
  font-size: 15px;
  color: #000000;
  padding: 5px;
  width: 100px;
  text-align: center;
  -webkit-transition-duration: 0.4s; /* Safari */
  transition-duration: 0.4s;
  text-decoration: none;
  overflow: hidden;
  cursor: pointer;
}

.red {
  background-color: #921212;
}
.button:after {
    content: "";
    background: #FFFFFF;
    display: block;
    position: absolute;
    padding-top: 100%;
    padding-left: 150%;
    margin-left: -20px!important;
    margin-top: -120%;
    opacity: 0;
    transition: all 0.8s
}
.button:active:after {
    padding: 0;
    margin: 0;
    opacity: 1;
    transition: 0s
}
</style>
