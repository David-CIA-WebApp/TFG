<template>
  <div id="materials">
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

    <h3>MATERIALES</h3>
    <div class="lds-roller" style="position: absolute; margin-left: auto; left: 50%; top: 40%;" v-if="!forceReload"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
    <div v-if="forceReload && logged" class="col-">
      <table class="table table-striped" id="materials">
        <thead>
          <tr>
            <th>Material</th>
            <th style="width: 10%;">Cantidad</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(material,i) in materials" :key="i">
            <td> <a href="#miModal" @click="setMaterial(material)"> {{material.nombre}} </a> </td> 
            <td style="text-align: center;"><button @click="reducirMaterial(i)" style="background: transparent; width: 30%; font-size: 16 px;">—</button> {{material.cantidad}} <button @click="aumentarMaterial(i)" style="background: transparent; width: 30%; font-size: 20px;">+</button></td>
          </tr>
        </tbody>
      </table>
    </div>

    <br>
    <a href="#miModal" @click="setMaterial(newMaterial)" style="background-color: transparent; color: blue; width: 120px;">Crear material</a>


    <div id="miModal" class="modal" v-if="forceReload">
      <div class="modal-contenido">
        <button style="background-color: rgba(21, 63, 117, 0.6); width: 8%; border: 2px solid #153f75; align-text: center;" @click="reloadSite">X</button>
        <p>Nombre:</p>
        <input v-model="actualMaterial.nombre"/>
        <p>Cantidad:</p>
        <input v-model="actualMaterial.cantidad" type="number"/>
        <p>Stock de seguridad:</p>
        <input v-model="actualMaterial.stockSeguridad" type="number"/>
        

      <br>

      <button
        class="button"
        v-if="!crear"
        @click="editMaterial(actualMaterial)"
        href="#">
          Actualizar
      </button>
      
      <button
        class="button red"
        v-if="!crear"
        @click="eliminar(actualMaterial)"
        href="#"  >
          Eliminar
      </button>
      
      <button
        class="button"
        v-if="crear"
        @click="crearMaterial(actualMaterial)"
        href="#"  >
          Crear
      </button>
      </div>  
    </div>

    <div style="width: 420px; margin-left: auto; margin-right: auto; margin-top: 200px; font-size: 10px;" class="typewriter" v-if="!logged">
      <h1>Sorry! This page is not available</h1>
    </div>

  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Materials',
  components: {
    
  },
  data() {
    return {
      logged: false,
      materials: [],
      forceReload: false,
      newMaterial: {
        nombre: "",
        cantidad: 0,
        stockSeguridad: 0
      },
      crear: false,
      actualMaterial: {},
      token: null
    }
  },
  methods: {
    crearMaterial(material) {
      this.forceReload = false;
      const path = `${process.env.VUE_APP_BACK_URL}/addMaterials`;
        const config = {
          method: 'post',
          url: path,
          data: {
            "nombre": material.nombre,
            "cantidad": material.cantidad,
            "stockSeguridad": material.stockSeguridad
          },
          headers: {
            "Content-Type": "application/JSON",
            "Access-Control-Allow-Origin": "*",
            "Authorization": this.token
          }
        };
        axios(config)
        .then((res) => {
          if (res) { 
            this.forceReload = true;
            this.reloadSite();
          }
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    reloadSite() {
      this.$router.push('materials');
      this.$router.go();
    },
    eliminar(material) {
      this.forceReload = false;
      const path = `${process.env.VUE_APP_BACK_URL}/deleteMaterial`;
        const config = {
          method: 'delete',
          url: path,
          data: {
            "nombre": material.nombre
          },
          headers: {
            "Content-Type": "application/JSON",
            "Access-Control-Allow-Origin": "*",
            "Authorization": this.token
          }
        };
        axios(config)
        .then((res) => {
          if (res) { 
            this.forceReload = true;
            this.reloadSite();
          }
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    loadMaterials() {
      const path = `${process.env.VUE_APP_BACK_URL}/materials`;
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
          this.materials[index] = element;
        }
        this.forceReload = true;
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
            this.loadMaterials();
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
    editMaterial(material) {
      this.forceReload = false;
      const path = `${process.env.VUE_APP_BACK_URL}/editMaterial`;
        const config = {
          method: 'put',
          url: path,
          data: {
            "antiguo_nombre": material.antiguo_nombre,
            "nombre": material.nombre,
            "cantidad": material.cantidad,
            "stockSeguridad": material.stockSeguridad
          },
          headers: {
            "Content-Type": "application/JSON",
            "Access-Control-Allow-Origin": "*",
            "Authorization": this.token
          }
        };
        axios(config)
        .then((res) => {
          if (res) { 
            this.forceReload = true;
          }
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    reducirMaterial(index) {
      this.materials[index].cantidad -= 1;
      this.materials[index].antiguo_nombre = this.materials[index].nombre;

      this.editMaterial(this.materials[index]);
    },
    aumentarMaterial(index) {
      this.materials[index].cantidad += 1;
      this.materials[index].antiguo_nombre = this.materials[index].nombre;

      this.editMaterial(this.materials[index]);
    },
    setMaterial(material) {
      if (!material.nombre) this.crear = true;
      material.antiguo_nombre = material.nombre;
      this.actualMaterial = material;
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
#materials {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#materials td, #materials th {
  border: 1px solid #ddd;
  padding: 8px;
}

#materials tr:nth-child(even){background-color: #f2f2f2;}

#materials tr:hover {background-color: #ddd;}

#materials th {
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
