<template>
  <div id="jobs">
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
            <th>Cliente</th>
            <th>Certificado</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(job,i) in jobs" :key="i">
            <td> {{job.id}} </td> 
            <td> {{job.tipo}} </td> 
            <td> {{job.descripcion}} </td> 
            <td> {{job.direccion}} </td> 
            <td><a style="color: blue;text-decoration: underline blue; cursor: pointer;" @click="redirectUser(job.id_cliente)">Ver cliente</a></td> 
            <td> {{job.id_certificado}} </td>
          </tr>
        </tbody>
      </table>
    </div>

    <h3>CITAS ASOCIADAS</h3>
    <div class="lds-roller" style="position: absolute; margin-left: auto; left: 50%; top: 40%;" v-if="!forceReload"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
    <div v-if="forceReload && logged">
      <table class="table table-striped" id="jobs" v-if="meetingsLoaded">
        <thead>
          <tr>
            <th>Descripcion</th>
            <th>Direccion</th>
            <th>Hora</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(cita,i) in citas" :key="i">
            <td>{{ cita.descripcion }}</td> 
            <td>{{ cita.direccion }}</td>
            <td>{{ cita.dates.toLocaleTimeString() }}</td> 
          </tr>
        </tbody>
      </table>
    </div>

    <div style="width: 420px; margin-left: auto; margin-right: auto; margin-top: 200px; font-size: 10px;" class="typewriter" v-if="!logged">
      <h1>Sorry! This page is not available</h1>
    </div>

  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Jobs',
  components: {
    
  },
  data() {
    return {
      logged: false,
      jobs: [],
      forceReload: false,
      token: null,
      thisUri: "",
      jobsLoaded: false,
      citas: [],
      meetingsLoaded: false,
    }
  },
  methods: {
    loadJobs() {
      var uri = window.location.href;
      this.thisUri = uri.split("jobs/")[0];
      var extension;
      var extCitas;
      if (uri.split("jobs/")[1]) {
        extension = "/trabajo/" + uri.split("jobs/")[1];
        extCitas = "/citas/" + uri.split("jobs/")[1];
      } else {
        extension = "/trabajos";
        extCitas = "/citas";
      }
      const path = `${process.env.VUE_APP_BACK_URL}` + extension;
      console.log(path);
      const config = {
        method: 'get',
        url: path,
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
          this.jobs[index] = element;
        }
        this.forceReload = true;
        this.jobsLoaded = true;
      });


      const path2 = `${process.env.VUE_APP_BACK_URL}` + extCitas;
      console.log(path2);
      const config2 = {
        method: 'get',
        url: path2,
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
          
          var cita = {
            dot: true,
            dates: new Date(element.fecha),
            descripcion: element.descripcion,
            direccion: element.direccion,
            id_trabajo: element.id_trabajo,
            id_cita: element.id,
            id_certificado: element.id_certificado,
            id_perito: element.id_perito,
            id_tecnico: element.id_tecnico,
          }
          this.citas[index] = cita;
        }
        this.meetingsLoaded = true;
        this.jobsLoaded = true;
      });
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
            this.loadJobs();
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
    redirectUser(userId) {
      this.$router.push("/user/" + userId);
    },
    closeSession() {
      localStorage.userMail = "";
      localStorage.userPass = "";
      localStorage.userType = "";
      this.redirectHome();
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
#jobs {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#jobs td, #jobs th {
  border: 1px solid #ddd;
  padding: 8px;
}

#jobs tr:nth-child(even){background-color: #f2f2f2;}

#jobs tr:hover {background-color: #ddd;}

#jobs th {
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
