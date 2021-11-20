<template>
  <div class="login">
      <p>Inicia sesión</p>
      <div>
        <input v-model="mail" type="text" placeholder="correo"/>
        <br>
        <input v-model="password" type="password" placeholder="contraseña"/>
      </div>
        <br>
      <button
      @click="login()">
        Entrar
      </button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Login',
  props: {
    msg: String
  },
  data() {
    return {
      logged: false,
      mail: "",
      password: ""
    }
  },
  methods: {
    login() {
      const path = `${process.env.VUE_APP_BACK_URL}/login`;
      const config = {
        method: 'post',
        url: path,
        data: {
          "mail": this.mail, 
          "password": this.password
        },
        headers: {
          "Content-Type": "application/JSON",
          "Access-Control-Allow-Origin": "*"
        }
      };
      axios(config)
        .then((res) => {
          console.log(res.data);
          if (res.data.accepted) this.logged = true;
          this.$emit("logging", this.logged);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    }
  },
  mounted() {

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
p {
  color: #5419c2;
}
.login {
  background-color: rgba(0, 255, 255, 0.212);
  width: 30%;
  position: relative;
  margin-left: auto;
  margin-right: auto;
  padding: 1%;
  border-radius: 12px;
}
input {
  border-style: none;
  border-radius: 5px;
}
</style>
