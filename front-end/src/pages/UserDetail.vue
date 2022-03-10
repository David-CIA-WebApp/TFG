<template>
  <div id="users">
    <div id="menu" v-if="forceReload && logged">
      <button 
      v-if="logged"
      style="background-color: blue; color: white; margin-top: 0px; margin-left: 0px;"
      @click="redirectHome">
        INICIO
      </button>
      <button 
      v-if="logged"
      style="background-color: transparent; color: red; margin-top: 0px; float: right;"
      @click="closeSession">
        Cerrar Sesión
      </button>
    </div>  

    <br><br><br>

    <div class="lds-roller" style="position: absolute; margin-left: auto; left: 50%; top: 40%;" v-if="!forceReload"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
    <div v-if="logged" class="col-">
    <h3>USUARIO</h3>
      <table class="table table-striped" id="users" v-if="usersLoaded">
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
            <td> {{ user.nombre }} </td> 
            <td>{{ user.apellidos }}</td> 
            <td>{{ user.dni }}</td> 
            <td>{{ user.email }}</td> 
            <td>{{ user.direccion }}</td> 
            <td>{{ user.telefono }}</td> 
            <td><a href="#miModal" @click="setActualUser(user)">Editar usuario</a></td> 
          </tr>
        </tbody>
      </table>
    </div>

    
    <h3>TRABAJOS</h3>
    <div class="lds-roller" style="position: absolute; margin-left: auto; left: 50%; top: 40%;" v-if="!forceReload"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
    <div v-if="forceReload && logged">
      <table class="table table-striped" id="jobs" v-if="jobsLoaded">
        <thead>
          <tr>
            <th>Id</th>
            <th>Tipo</th>
            <th>Descripcion</th>
            <th>Direccion</th>
            <th>Certificado</th>
            <th>Trabajo</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(job,i) in jobs" :key="i">
            <td> {{job.id}} </td> 
            <td> {{job.tipo}} </td> 
            <td> {{job.descripcion}} </td> 
            <td> {{job.direccion}} </td> 
            <td v-if="job.certificado == null"> <input type="file" id="certificado" name="certificado" @change="previewFile(job.id)" accept=".pdf"/> </td>
            <td v-if="job.certificado != null"> <a style="color: blue;text-decoration: underline blue; cursor: pointer;" @click="downloadPDF(job.id)">Ver certificado</a> </td>
            <td><a style="color: blue;text-decoration: underline blue; cursor: pointer;" @click="redirectJob(job.id)">Ver trabajo</a></td> 
          </tr>
        </tbody>
      </table>
    </div>


    <div style="width: 420px; margin-left: auto; margin-right: auto; margin-top: 200px; font-size: 10px;" class="typewriter" v-if="!logged">
      <h1>Sorry! This page is not available</h1>
    </div>

    <div id="miModal" class="modal" v-if="forceReload">
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
      forceReload: true,
      usersLoaded: false,
      actualUser: {},
      userType: "",
      dniArray: [],
      dniSelected: null,
      searchedUsers: [],
      changeSearch: false,
      token: null,
      jobs: [],
      jobsLoaded: false,
    }
  },
  methods: {
    downloadPDF(job_id) {
      axios.get(`${process.env.VUE_APP_BACK_URL}/certificados/${job_id}`, {
        headers: {
          'Content-Type': 'multipart/form-data',
          "Access-Control-Allow-Origin": "*",
          "Authorization": this.token
        }
      })
      .then((response) => {
        console.log(response);
      });
    },
    previewFile(job_id) {
      var file = document.querySelector('#certificado');
      var formData = new FormData();
      formData.append("file", file.files[0]);
      
      axios.post(`${process.env.VUE_APP_BACK_URL}/certificados/${job_id}`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
          "Access-Control-Allow-Origin": "*",
          "Authorization": this.token
        }
      });
    },
    actualizar(actualUser) {  
      if (actualUser.pass == null) {
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
    loadUsers() {
      this.users = [];
      this.workers = [];
      this.externalWorkers = [];
      this.clients = [];
      this.economyManagers = [];

      var userId = window.location.href.split("user/")[1];
      const path = `${process.env.VUE_APP_BACK_URL}/user/` + userId;
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
      



      const path2 = `${process.env.VUE_APP_BACK_URL}/trabajos/` + userId;
      const config2 = {
        method: 'get',
        url: path2,
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
      axios(config2)
      .then((res) => {
        for (let index = 0; index < res.data.length; index++) {
          var element = res.data[index];
          this.jobs[index] = element;
        }
        this.jobsLoaded = true;
      });

    },
    setActualUser(user) {
      this.actualUser = user;
      this.actualUser.oldDNI = user.dni;
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
      this.$router.push({ path: '/admin' });
    },
    closeSession() {
      localStorage.userMail = "";
      localStorage.userPass = "";
      localStorage.userType = "";
      this.redirectHome();
    }, 
    reloadSite() {
      this.$router.push('');
      this.$router.go();
    },
    redirectJob(jobId) {
      this.$router.push("/jobs/" + jobId);
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

</style>
