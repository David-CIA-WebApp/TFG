<template>
  <div id="Public">
    <div id="menuPP" class="box"> 
      <div class="container">
        <div class="column"> 
          <img class="logo" v-bind:src="logo" alt="" />
        </div>
        <div class="column">
          <a @click="quienesSomosF" class="btn btn-primary">Conocenos</a>
          <a @click="valoracionesF" class="btn btn-primary">Valoraciones</a>
          <a @click="contactanosF" class="btn btn-primary">Contactanos</a>
        </div>
      </div>
    </div>
    <div id="quienesSomos" v-if="quienesSomos">
      <h1>¿Quiénes somos?</h1>

      <div class="column2">
        <pre style="font-size: 18px;">
          Somos una empresa con más de 20 años de valoraciones en el sector 
        del agua y el gas, con titulación oficial. Tenemos colaboradores para 
        llevar a cabo todo tipo de trabajos de albañilería, pintura y aluminio. 
        Ponemos a su disposición nuestra formación y valoraciones asesorandole en 
        sus reformas.

        <img src="@/assets/Fontaneria3.jpg"  style="width: 485px;" />
        </pre>
      </div>
      <div class="column2">
        <pre style="font-size: 18px;">
          Nuestra valoraciones nos permite ofrecerle un servicio de calidad y
        confiabilidad, con una amplia gama de trabajos realizados en el sector
        de la construcción. Realizamos desde reparaciones hasta instalaciones
        de gas, agua y electricidad. Así mismo, contamos con una amplia gama de
        trabajos de albañilería, pintura y aluminio, gracias a los cuales, puede 
        contar con nosotros para obras de gran envergadura.

        <img src="@/assets/foto1.jpg"  style="" />
        </pre>
      </div>
      
    </div>
    <div id="valoraciones" v-if="valoraciones">
      <h1>Valoraciones</h1>
      <div>
        <div class="column">
          <img src="@/assets/JavierEugenio.jpeg" style="width: 200px; margin-bottom: -50px;" />
        </div>
        <div class="column">
          <h2>Javier Eugenio</h2>
          <pre style="font-size: 15px;">
"Como fontaneros los considero el número 1, 
reúnen todos los requisitos. Buen trato 
hacia sus clientes y una gran dedicación."
          </pre>
        </div>
        <div class="column">
          <img src="@/assets/AntoniodeDiego.jpeg" style="width: 200px; margin-bottom: -50px;" />
        </div>
        <div class="column">
          <h2>Antonio de Diego</h2>
          <pre style="font-size: 15px;">
"¡Gran profesionalidad! Están al tanto 
de las últimas teconologías, materiales 
y herramientas tanto de gas como de agua."
          </pre>
        </div>
        <div class="column">
          <img src="@/assets/HEBRA.png" style="width: 200px; margin-bottom: -50px;" />
        </div>
        <div class="column">
          <h2>HEBRA</h2>
          <pre style="font-size: 15px;">
"Unos trabajadores excelentes y 
comprometidos. Máxima transparencia, 
eficiencia y calidad."
          </pre>
        </div>
      </div>
    </div>
    <div id="contactanos" v-if="contactanos" style="margin-top: 200px;">
      <div class="addM box">
        <div style="position: absolute; background: #044ca9; width: 700px; border-radius: 25px;">
          <h2 style="color: white; margin-left: 20px;">CONTACTANOS</h2>

          <pre style="color: white; margin-left: 20px;">Nombre: <input style="margin-left: 50px; width:30%;" v-model="contacto.nombre" required></pre>
          <pre style="color: white; margin-left: 20px;">Correo:    <input style="margin-left: 26px; width:50%;" v-model="contacto.correo" type="email" required></pre>
          <pre style="color: white; margin-left: 20px;">Descripcion:  <textarea v-model="contacto.descripcion" style="margin-left: 3px; width:70%; max-width:70%; resize: none; rows='4';"></textarea></pre>
          <button style="color: white; left: 570px; margin-bottom: 10px; margin-top: -5px;" @click="crearContacto">ENVIAR</button>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
//import axios from 'axios';

export default {
  data() {
    return {
      logo: "https://i.ibb.co/YpKv3mr/LOGO-DAVID-CIA.png",
      quienesSomos: true,
      valoraciones: false,
      contactanos: false,
      contacto: {
        nombre: "",
        correo: "",
        descripcion: ""
      },
      errorMessage: ""
    }
  },
  methods: {
    quienesSomosF() {
      this.quienesSomos = true;
      this.valoraciones = false;
      this.contactanos = false;
    },
    valoracionesF() {
      this.quienesSomos = false;
      this.valoraciones = true;
      this.contactanos = false;
    },
    contactanosF() {
      this.quienesSomos = false;
      this.valoraciones = false;
      this.contactanos = true;
    },
    validateEmail(email) {
      return String(email)
        .toLowerCase()
        .match(
          /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
        );
    },
    postConsulta() {
      var dateToday = new Date(Date.now());
      var fechaAEnviar = "";
      if ((dateToday.getMonth()+1) < 10) {
        if (dateToday.getDate() < 10) {
          fechaAEnviar = dateToday.getFullYear() + "-0" + (dateToday.getMonth()+1) + "-0" + dateToday.getDate();
        } else {
          fechaAEnviar = dateToday.getFullYear() + "-0" + (dateToday.getMonth()+1) + "-" + dateToday.getDate();
        }
      }
      this.errorMessage = "";
      axios.post(`${process.env.VUE_APP_BACK_URL}/consultas`, {"nombre": this.contacto.nombre, "descripcion": this.contacto.descripcion, "correo": this.contacto.correo}, {
        headers: {
          'Content-Type': 'application/json'
        }
      }).then(response => {
        console.log(response);
        
        axios.post(`${process.env.VUE_APP_BACK_URL}/alertas`, {"tipoAlerta": "Contacto", "descripcion": "Un nuevo usuario con correo X te ha contactado desde la web", "fecha": new Date(fechaAEnviar), "activa": 1, "id_access": this.contacto.correo}, {
          headers: {
            'Content-Type': 'application/json',
            'Authorization': ''
          }
        }).then(response => {
          console.log(response);
          
          this.contacto = {
            nombre: "",
            correo: "",
            descripcion: ""
          }
        }).catch(error => {
          console.log(error);
        });
      }).catch(error => {
        console.log(error);
      });
    },
    crearContacto() {
      if (!this.validateEmail(this.contacto.correo)) {
        this.errorMessage += "El correo no es valido\n";
      } 
      if (this.contacto.nombre == "") {
        this.errorMessage += "El nombre es requerido\n";
      } 
      if (this.contacto.descripcion == "") {
        this.errorMessage += "La descripción no puede estar vacia\n";
      } 
      if (this.errorMessage == "") {
        this.postConsulta();
      } else {
        alert(this.errorMessage);
        this.errorMessage = "";
      }
    }
  },
};
</script>

<style>
#menuPP {
  width: 100%;
  background-color: #102797;
}
.box {
  display: flex;
  align-items: center;
  justify-content: center;
}
.logo {
  width: 200px;
}
.btn {
  margin-top: 10px;
  margin-bottom: 10px;
  margin-left: 10px;
  margin-right: 10px;
  padding: 10px;
  border-radius: 10px;
  font-size: 20px;
  font-weight: bold;
  color: white;
  background-color: #102797;
}
.btn:hover {
  cursor: pointer;
  background-color: #0f0f0f;
}
.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 100%;
  height: 100%;
  max-width: 480px;
  margin: 0 auto;
  padding-left:15px;
  padding-right:15px;
}
.column {
  display: block;
  text-decoration: none;
  text-align: center;
  padding: 1rem 0;
  margin-bottom: 1rem;
}
.column2 {
  display: block;
  text-decoration: none;
  padding: 1rem 0;
  margin-bottom: 1rem;
}
</style>