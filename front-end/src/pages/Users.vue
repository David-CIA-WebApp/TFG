<template>
  <div id="users">
    <div id="menu" v-if="forceReload && logged">
      <button 
      v-if="logged"
      style="background-color: blue; color: white; margin-top: 0px; margin-left: 0px;"
      @click="redirectHome">
        INICIO
      </button>
      <a href="/alertas" class="alertas"><svg viewBox="0 0 15 1" width="32" height="30"><path id="lineBC" d="M 1 1 L 1 2 L 11 2 L 11 1 L 10 0 C 9 -8 3 -8 2 0 L 1 1 M 6 3 A 1 1 0 0 0 6 6 A 1 1 0 0 0 6 3" stroke="black" stroke-width="0.01"  /></svg></a>

      <button 
      v-if="logged"
      style="background-color: transparent; color: red; margin-top: 0px; float: right;"
      @click="closeSession">
        Cerrar Sesión
      </button>
    </div>  

    <div>
      <p>Buscar usuario: </p>
      <input type="text" id="myInput" @input="searchUser()">
    </div>
    <div>
      <table class="table table-striped" id="searchedUsers" v-if="changeSearch">
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Apellidos</th>
            <th>DNI</th>
            <th v-if="!isMobile">Correo</th>
            <th v-if="!isMobile">Dirección</th>
            <th v-if="!isMobile">Telefono</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(user,i) in searchedUsers" :key="i">
            <td><a style="color: blue;text-decoration: underline blue; cursor: pointer;" @click="redirectUser(user.id)"> {{ user.nombre }} </a></td> 
            <td>{{ user.apellidos }}</td> 
            <td>{{ user.dni }}</td> 
            <td v-if="!isMobile">{{ user.email }}</td> 
            <td v-if="!isMobile">{{ user.direccion }}</td> 
            <td v-if="!isMobile">{{ user.telefono }}</td> 
          </tr>
        </tbody>
      </table>
    </div>

    <br><br><br>

    <div class="lds-roller" style="position: absolute; margin-left: auto; left: 50%; top: 40%;" v-if="!forceReload"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
    <div id="tables-div" v-if="logged" class="col-">
      <h3>USUARIOS</h3>
      <table class="table table-striped" id="users" v-if="usersLoaded">
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Apellidos</th>
            <th>DNI</th>
            <th v-if="!isMobile">Correo</th>
            <th v-if="!isMobile">Dirección</th>
            <th v-if="!isMobile">Telefono</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(user,i) in users" :key="i">
            <td><a style="color: blue;text-decoration: underline blue; cursor: pointer;" @click="redirectUser(user.id)"> {{ user.nombre }} </a></td> 
            <td>{{ user.apellidos }}</td> 
            <td>{{ user.dni }}</td> 
            <td v-if="!isMobile">{{ user.email }}</td> 
            <td v-if="!isMobile">{{ user.direccion }}</td> 
            <td v-if="!isMobile">{{ user.telefono }}</td> 
            <td><a href="#miModal" @click="setActualUser(user)">Editar usuario</a></td> 
          </tr>
        </tbody>
      </table>
      <div :class="selects">
        <button
        style="background-color: transparent; color: blue;"
        @click="createUser('USUARIOS')">
          Crear usuario
        </button>
      </div>

      <br><br><br><br>

      <h3>TRABAJADORES INTERNOS</h3>
      <table class="table table-striped" id="users" v-if="workersLoaded">
        <thead>
          <tr>
            <th>Nombre</th>
            <th v-if="!isMobile">Apellidos</th>
            <th v-if="!isMobile">DNI</th>
            <th v-if="!isMobile">Correo</th>
            <th v-if="!isMobile">Dirección</th>
            <th>Telefono</th>
            <th>Función</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(worker,i) in workers" :key="i">
            <td><a style="color: blue;text-decoration: underline blue; cursor: pointer;" @click="redirectUser(worker.id)"> {{ worker.nombre }} </a></td> 
            <td v-if="!isMobile">{{ worker.apellidos }}</td> 
            <td v-if="!isMobile">{{ worker.dni }}</td> 
            <td v-if="!isMobile">{{ worker.email }}</td> 
            <td v-if="!isMobile">{{ worker.direccion }}</td> 
            <td>{{ worker.telefono }}</td> 
            <td>{{ worker.tipo }}</td> 
            <td><a href="#miModal" @click="setActualUser(worker)">Editar usuario</a></td> 
          </tr>
        </tbody>
      </table>
      <div :class="selects">
        <select v-model="dniSelected" id="dniSelected">
          <option v-for="user in users" v-bind:key="user.dni" :value="user.dni">{{user.nombre}} {{user.apellidos}} - {{user.dni}}</option>
        </select>
        <button
        style="background-color: transparent; color: blue;"
        @click="createUser('TRABJADOR')">
          Crear trabajador
        </button>
      </div>

      <br><br><br><br>

      <h3>TRABAJADORES EXTERNOS</h3>
      <table class="table table-striped" id="users" v-if="externalWorkersLoaded">
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Apellidos</th>
            <th v-if="!isMobile">DNI</th>
            <th v-if="!isMobile">Correo</th>
            <th v-if="!isMobile">Dirección</th>
            <th>Telefono</th>
            <th>Función</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(ew,i) in externalWorkers" :key="i">
            <td><a style="color: blue;text-decoration: underline blue; cursor: pointer;" @click="redirectUser(ew.id)"> {{ ew.nombre }} </a></td> 
            <td>{{ ew.apellidos }}</td> 
            <td v-if="!isMobile">{{ ew.dni }}</td> 
            <td v-if="!isMobile">{{ ew.email }}</td> 
            <td v-if="!isMobile">{{ ew.direccion }}</td> 
            <td>{{ ew.telefono }}</td> 
            <td>{{ ew.ocupacion }}</td> 
            <td><a href="#miModal" @click="setActualUser(ew)">Editar usuario</a></td> 
          </tr>
        </tbody>
      </table>
      <div :class="selects">
        <select v-model="dniSelected" id="dniSelected" style="margin-top: 5px;">
          <option v-for="user in users" v-bind:key="user.dni" :value="user.dni">{{user.nombre}} {{user.apellidos}} - {{user.dni}}</option>
        </select>
        <button
        style="background-color: transparent; color: blue;"
        @click="createUser('TRABJADOR EXTERNO')">
          Crear trabajador externo
        </button>
      </div>

      <br><br><br><br>

      <h3>GESTORES</h3>
      <table class="table table-striped" id="users" v-if="managersLoaded">
        <thead>
          <tr>
            <th>Nombre</th>
            <th v-if="!isMobile">Apellidos</th>
            <th v-if="!isMobile">DNI</th>
            <th>Correo</th>
            <th v-if="!isMobile">Dirección</th>
            <th>Telefono</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(em,i) in economyManagers" :key="i">
            <td><a style="color: blue;text-decoration: underline blue; cursor: pointer;" @click="redirectUser(em.id)"> {{ em.nombre }} </a></td> 
            <td v-if="!isMobile">{{ em.apellidos }}</td> 
            <td v-if="!isMobile">{{ em.dni }}</td> 
            <td>{{ em.email }}</td> 
            <td v-if="!isMobile">{{ em.direccion }}</td> 
            <td>{{ em.telefono }}</td> 
            <td><a href="#miModal" @click="setActualUser(em)">Editar usuario</a></td> 
          </tr>
        </tbody>
      </table>

      <div :class="selects">
        <select v-model="dniSelected" id="dniSelected" style="margin-top: 5px;">
          <option v-for="user in users" v-bind:key="user.dni" :value="user.dni">{{user.nombre}} {{user.apellidos}} - {{user.dni}}</option>
        </select>
        <button
        style="background-color: transparent; color: blue;"
        @click="createUser('GESTOR')">
          Crear gestor
        </button>
      </div>

      <br><br><br><br>

      <h3>CLIENTES</h3>
      <table class="table table-striped" id="users" v-if="clientsLoaded">
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Apellidos</th>
            <th v-if="!isMobile">DNI</th>
            <th v-if="!isMobile">Correo</th>
            <th>Dirección</th>
            <th>Telefono</th>
            <th v-if="!isMobile">Cliente potencial</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(client,i) in clients" :key="i">
            <td><a style="color: blue;text-decoration: underline blue; cursor: pointer;" @click="redirectUser(client.id)"> {{ client.nombre }} </a></td> 
            <td>{{ client.apellidos }}</td> 
            <td v-if="!isMobile">{{ client.dni }}</td> 
            <td v-if="!isMobile">{{ client.email }}</td> 
            <td>{{ client.direccion }}</td> 
            <td>{{ client.telefono }}</td> 
            <td v-if="!isMobile">{{ client.clientePotencial }}</td> 
            <td><a href="#miModal" @click="setActualUser(client)">Editar usuario</a></td> 
          </tr>
        </tbody>
      </table>
      <div :class="selects">
        <select v-model="dniSelected" id="dniSelected" style="margin-top: 5px;">
          <option v-for="user in users" v-bind:key="user.dni" :value="user.dni">{{user.nombre}} {{user.apellidos}} - {{user.dni}}</option>
        </select>
        <button
        style="background-color: transparent; color: blue;"
        @click="createUser('CLIENTE')">
          Crear cliente
        </button>
      </div>  
    </div>

    <div style="width: 420px; margin-left: auto; margin-right: auto; margin-top: 200px; font-size: 10px;" class="typewriter" v-if="!logged">
      <h1>Sorry! This page is not available</h1>
    </div>

    <div id="miModal" class="modal col-" v-if="forceReload">
      <div class="modal-contenido">
        <button style="background-color: rgba(21, 63, 117, 0.6); width: 8%; border: 2px solid #153f75; align-text: center;" @click="reloadSite">X</button>
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
        <p v-if="actualUser.pass != null">Repita Contraseña:</p>
        <input v-if="actualUser.pass != null" v-model="actualUser.repitpass"/>

        <p v-if="actualUser.tipo != null">Ocupación:</p>
        <select
          v-if="actualUser.tipo != null"
          class="border rounded-sm ml-2 p-1"
          v-model="actualUser.tipo"
        >
          <option value="Administrador">Administrador</option>
          <option value="Técnico">Técnico</option>
          <option value="Perito">Perito</option>
        </select>

        <p v-if="actualUser.ocupacion != null">Ocupación:</p>
        <input v-if="actualUser.ocupacion != null" v-model="actualUser.ocupacion"/>

      <br>
      <button
        v-if="userType == 'Administrador'"
        class="button"
        @click="actualizar(actualUser)"
        href="#">
          Actualizar
      </button>
      
      <button
        v-if="userType == 'Administrador'"
        class="button red"
        @click="eliminar(actualUser)"
        href="#"  >
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
      forceReload: true,
      usersLoaded: false,
      workersLoaded: false,
      externalWorkersLoaded: false,
      managersLoaded: false,
      clientsLoaded: false,
      actualUser: {},
      userType: "",
      dniArray: [],
      dniSelected: null,
      searchedUsers: [],
      changeSearch: false,
      token: null,
      windowWidth: window.innerWidth,
      isMobile: false,
      selects: "selectsNotMobile"
    }
  },
  watch() {
    this.windowWidth = window.innerWidth;
  },
  methods: {
    loadUsers() {
      this.users = [];
      this.workers = [];
      this.externalWorkers = [];
      this.clients = [];
      this.economyManagers = [];

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
          "Authorization": this.token
        }
      }
      axios(config)
      .then((res) => {
        for (let index = 0; index < res.data.length; index++) {
          var element = res.data[index];
          this.users[index] = element;
          this.dniArray.push(element.dni);
        }
        this.usersLoaded = true;
      });
      
      config.url = `${process.env.VUE_APP_BACK_URL}/workers`;
      axios(config)
      .then((res) => {
        for (let index = 0; index < res.data.length; index++) {
          var element = res.data[index];
          this.workers[index] = element;
        }
        this.workersLoaded = true;
      });
      
      config.url = `${process.env.VUE_APP_BACK_URL}/externalWorkers`;
      axios(config)
      .then((res) => {
        for (let index = 0; index < res.data.length; index++) {
          var element = res.data[index];
          this.externalWorkers[index] = element;
        }
        this.externalWorkersLoaded = true;
      });
      
      config.url = `${process.env.VUE_APP_BACK_URL}/clients`;
      axios(config)
      .then((res) => {
        for (let index = 0; index < res.data.length; index++) {
          var element = res.data[index];
          this.clients[index] = element;
        }
        this.clientsLoaded = true;
      });
      
      config.url = `${process.env.VUE_APP_BACK_URL}/gestores`;
      axios(config)
      .then((res) => {
        for (let index = 0; index < res.data.length; index++) {
          var element = res.data[index];
          this.economyManagers[index] = element;
        }
        this.managersLoaded = true;
      });
      
    },
    setActualUser(user) {
      this.actualUser = user;
      this.actualUser.oldDNI = user.dni;
      if (this.actualUser.pass == "") this.actualUser.repitpass = "";
    },
    actualizar(actualUser) {  
      if (actualUser.pass != actualUser.repitpass || actualUser.pass == null) {
        actualUser.pass = "";
      }
      if (actualUser.tipo == null) {
        actualUser.tipo = "";
      }
      if (actualUser.ocupacion == null) {
        actualUser.ocupacion = "";
      }

      const path = `${process.env.VUE_APP_BACK_URL}/editUser/${actualUser.oldDNI}`;
      const config = {
        method: 'put',
        url: path,
        data: {
          "apellidos": actualUser.apellidos,
          "direccion": actualUser.direccion,
          "dni": actualUser.dni,
          "email": actualUser.email,
          "nombre": actualUser.nombre,
          "pass": actualUser.pass,
          "telefono": actualUser.telefono,
          "tipo": actualUser.tipo,
          "ocupacion": actualUser.ocupacion,
          "tabla":  actualUser.tabla,
          "clientePotencial": false // TODO Aqui y en el formulario, añadir
        },
        headers: {
          "Content-Type": "application/JSON",
          "Access-Control-Allow-Origin": "*",
          "Authorization": this.token
        }
      }
      axios(config)
      .then((res) => {
        console.log(res);
        if (this.actualUser.pass == "") {
          this.actualUser.pass = null;
        }
        if (this.actualUser.tipo == "") {
          this.actualUser.tipo = null;
        }
        if (this.actualUser.ocupacion == "") {
          this.actualUser.ocupacion = null;
        }
        this.reloadSite();
      });
      

      
      //this.$router.go();
    },
    eliminar(actualUser) {
      const config = {
          method: 'delete',
          url: "",
          data: {
            
          },
          headers: {
            "Content-Type": "application/JSON",
            "Access-Control-Allow-Origin": "*",
            "Authorization": this.token
          }
        }
      if (actualUser.tabla == "trabajador") {
        const path = `${process.env.VUE_APP_BACK_URL}/deleteWorker/${actualUser.dni}`;
        config.url = path;
        axios(config)
        .then((res) => {
          console.log(res);
          this.reloadSite();
        });
      }
      else if (actualUser.tabla == "trabajador externo") {
        const path = `${process.env.VUE_APP_BACK_URL}/deleteExternalWorker/${actualUser.dni}`;
        config.url = path;
        axios(config)
        .then((res) => {
          console.log(res);
          this.reloadSite();
        });
      } 
      else if (actualUser.tabla == "gestor") {
        const path = `${process.env.VUE_APP_BACK_URL}/deleteManager/${actualUser.dni}`;
        config.url = path;
        axios(config)
        .then((res) => {
          console.log(res);
          this.reloadSite();
        });
      }
      else if (actualUser.tabla == "usuario") {
        const path = `${process.env.VUE_APP_BACK_URL}/deleteUser/${actualUser.dni}`;
        config.url = path;
        axios(config)
        .then((res) => {
          console.log(res);
          this.reloadSite();
        });
      }
      
      //this.$router.go();
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
            this.userType = localStorage.userType;
            this.token = res.data.token;
            this.loadUsers();
          }
          
          this.$emit("logging", this.logged);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    redirectHome() {
      this.$router.push('admin');
    },
    closeSession() {
      localStorage.userMail = "";
      localStorage.userPass = "";
      localStorage.userType = "";
      this.redirectHome();
    }, 
    createUser(entrada) { 
      console.log(entrada);
      var path = "";
        const config = {
          method: 'post',
          url: "",
          data: {
            "apellidos": "nuevo",
            "direccion": "sin especificar",
            "dni": "123456789X",
            "email": "sin mail",
            "nombre": "nuevo",
            "pass": "pass",
            "telefono": 670123456,
            "tipo": "Técnico",
            "ocupacion": "Técnico",
            "tabla":  "usuario",
            "clientePotencial": false // TODO Aqui y en el formulario, añadir
          },
          headers: {
            "Content-Type": "application/JSON",
            "Access-Control-Allow-Origin": "*",
            "Authorization": this.token
          }
        }
      if (entrada == 'USUARIOS') {
        path = `${process.env.VUE_APP_BACK_URL}/addUsers`; 
      }
      else if (entrada == 'TRABJADOR') {
        path = `${process.env.VUE_APP_BACK_URL}/addWorkers`;
        config.data.dni = this.dniSelected;
      }
      else if (entrada == 'TRABJADOR EXTERNO') {
        path = `${process.env.VUE_APP_BACK_URL}/addExternalWorkers`;
        config.data.dni = this.dniSelected;
      }
      else if (entrada == 'GESTOR') {
        path = `${process.env.VUE_APP_BACK_URL}/addManager`;
        config.data.dni = this.dniSelected;
      }
      else if (entrada == 'CLIENTE') {
        path = `${process.env.VUE_APP_BACK_URL}/addClients`;
        config.data.dni = this.dniSelected;
      }


      config.url = path;
      axios(config)
      .then((res) => {
        console.log(res);
        this.reloadSite();
      });
    }, 
    reloadSite() {
      this.$router.push('users');
      this.$router.go();
    },
    searchUser() {
      this.changeSearch = false;
      var text = document.getElementById("myInput").value;

      this.searchedUsers = [];
      
      if (text != "") {
        const path = `${process.env.VUE_APP_BACK_URL}/users/` + text;
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
            "Authorization": this.token
          }
        }
        axios(config)
        .then((res) => {
          for (let index = 0; index < res.data.length; index++) {
            var element = res.data[index];
            this.searchedUsers[index] = element;
          }
          this.changeSearch = true;
        });
      }
    },
    redirectUser(userId) {
      this.$router.push("/user/" + userId);
    },
    onResize() {
      this.windowWidth = window.innerWidth;
      if (this.windowWidth < 768) {
        this.isMobile = true;
        this.selects = "selectsMobile";
      }
      else {
        this.isMobile = false;
        this.selects = "selectsNotMobile";
      }
    }
  },
  mounted() {
    this.loadData();
    this.onResize();
    this.$nextTick(() => {
      window.addEventListener('resize', this.onResize);
    });
  },
  beforeDestroy() { 
    window.removeEventListener('resize', this.onResize); 
  },
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

.lds-roller {
  display: inline-block;
  position: relative;
  width: 80px;
  height: 80px;
}
.lds-roller div {
  animation: lds-roller 1.2s cubic-bezier(0.5, 0, 0.5, 1) infinite;
  transform-origin: 40px 40px;
}
.lds-roller div:after {
  content: " ";
  display: block;
  position: absolute;
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: rgb(0, 0, 0);
  margin: -4px 0 0 -4px;
}
.lds-roller div:nth-child(1) {
  animation-delay: -0.036s;
}
.lds-roller div:nth-child(1):after {
  top: 63px;
  left: 63px;
}
.lds-roller div:nth-child(2) {
  animation-delay: -0.072s;
}
.lds-roller div:nth-child(2):after {
  top: 68px;
  left: 56px;
}
.lds-roller div:nth-child(3) {
  animation-delay: -0.108s;
}
.lds-roller div:nth-child(3):after {
  top: 71px;
  left: 48px;
}
.lds-roller div:nth-child(4) {
  animation-delay: -0.144s;
}
.lds-roller div:nth-child(4):after {
  top: 72px;
  left: 40px;
}
.lds-roller div:nth-child(5) {
  animation-delay: -0.18s;
}
.lds-roller div:nth-child(5):after {
  top: 71px;
  left: 32px;
}
.lds-roller div:nth-child(6) {
  animation-delay: -0.216s;
}
.lds-roller div:nth-child(6):after {
  top: 68px;
  left: 24px;
}
.lds-roller div:nth-child(7) {
  animation-delay: -0.252s;
}
.lds-roller div:nth-child(7):after {
  top: 63px;
  left: 17px;
}
.lds-roller div:nth-child(8) {
  animation-delay: -0.288s;
}
.lds-roller div:nth-child(8):after {
  top: 56px;
  left: 12px;
}
@keyframes lds-roller {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.selectsNotMobile{
  margin-top: -75px;
}

.alertas {
    position: absolute;
    top: 7px;
    left: 120px;
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
