<template>
  <div id="Public">
    <div id="menuPP" class="box"> 
      <div class="container">
        <div class="column"> 
          <img class="logo" v-bind:src="logo" alt="" />
        </div>
        <div class="column">
          <a @click="quienesSomosF" class="btn btn-primary">¿Quiénes somos?</a>
          <a @click="experienciaF" class="btn btn-primary">Experiencia</a>
          <a @click="contactanosF" class="btn btn-primary">Contactanos</a>
        </div>
      </div>
    </div>
    <div id="quienesSomos" v-if="quienesSomos">
      <h1>¿Quiénes somos?</h1>
<pre>
   Lorem ipsum dolor sit amet consectetur adipiscing elit, 
nibh nullam eget sapien proin auctor aliquet, quam turpis 
et praesent enim tempus. Congue purus odio bibendum 
inceptos tristique blandit ornare parturient cras cubilia, 
senectus tincidunt leo ultricies egestas sodales ante netus 
fusce, himenaeos justo eleifend donec felis tempor magnis 
volutpat praesent. Himenaeos eleifend ac potenti 
condimentum semper suscipit sapien, fringilla conubia 
aenean cubilia scelerisque odio lobortis, porta justo 
tincidunt praesent vestibulum lectus. 

  Natoque himenaeos aptent in commodo est per 
elementum senectus viverra gravida, congue nascetur 
ligula maecenas quis diam faucibus aliquet. Neque 
hendrerit a consequat vulputate curabitur taciti torquent, 
posuere nullam cras sed varius justo, ac duis non natoque 
ligula tellus. Nulla parturient iaculis dui eros dictumst, vitae 
tellus bibendum senectus aliquet, himenaeos nullam 
</pre>
    </div>
    <div id="experiencia" v-if="experiencia">
      <h1>Experiencia</h1>
<pre>
   Lorem ipsum dolor sit amet consectetur adipiscing elit, 
nibh nullam eget sapien proin auctor aliquet, quam turpis 
et praesent enim tempus. Congue purus odio bibendum 
inceptos tristique blandit ornare parturient cras cubilia, 
senectus tincidunt leo ultricies egestas sodales ante netus 
fusce, himenaeos justo eleifend donec felis tempor magnis 
volutpat praesent. Himenaeos eleifend ac potenti 
condimentum semper suscipit sapien, fringilla conubia 
aenean cubilia scelerisque odio lobortis, porta justo 
tincidunt praesent vestibulum lectus. 

  Natoque himenaeos aptent in commodo est per 
elementum senectus viverra gravida, congue nascetur 
ligula maecenas quis diam faucibus aliquet. Neque 
hendrerit a consequat vulputate curabitur taciti torquent, 
posuere nullam cras sed varius justo, ac duis non natoque 
ligula tellus. Nulla parturient iaculis dui eros dictumst, vitae 
tellus bibendum senectus aliquet, himenaeos nullam 
</pre>
    </div>
    <div id="contactanos" v-if="contactanos" style="margin-top: 250px;">
      <div class="addM box">
        <div style="position: absolute; background: #044ca9; width: 700px; border-radius: 25px;">
          <h2 style="color: white; margin-left: 20px;">CONTACTANOS</h2>
          <form>
          <pre style="color: white; margin-left: 20px;">Nombre: <input style="margin-left: 50px; width:30%;" v-model="contacto.nombre" required></pre>
          <pre style="color: white; margin-left: 20px;">Correo:    <input style="margin-left: 26px; width:50%;" v-model="contacto.correo" type="email" required></pre>
          <pre style="color: white; margin-left: 20px;">Descripcion:  <textarea style="margin-left: 3px; width:70%; max-width:70%; resize: none; rows='4';" v-model="contacto.descripcion" required></textarea></pre>
          <button style="color: white; left: 570px; margin-bottom: 20px;" @click="crearContacto">ENVIAR</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
//import axios from 'axios';

export default {
  data() {
    return {
      logo: "https://i.ibb.co/YpKv3mr/LOGO-DAVID-CIA.png",
      quienesSomos: true,
      experiencia: false,
      contactanos: false,
      contacto: {
        nombre: "",
        correo: "",
        descripcion: ""
      }
    }
  },
  methods: {
    quienesSomosF() {
      this.quienesSomos = true;
      this.experiencia = false;
      this.contactanos = false;
    },
    experienciaF() {
      this.quienesSomos = false;
      this.experiencia = true;
      this.contactanos = false;
    },
    contactanosF() {
      this.quienesSomos = false;
      this.experiencia = false;
      this.contactanos = true;
    },
    crearContacto() {
      console.log(this.contacto);
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
</style>