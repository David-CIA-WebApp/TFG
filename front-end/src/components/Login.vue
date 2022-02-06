<template>
  <div class="login">
      <div>
        <img v-bind:src="logo" alt="" />
        <input v-model="mail" type="text" placeholder="correo"/>
        <br>
        <input v-model="password" type="password" placeholder="contraseña"/>
      </div>
        <br>
      <button
      class="button"
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
      password: "",
      logo: "https://i.ibb.co/YpKv3mr/LOGO-DAVID-CIA.png",
      token: null
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
          if (res.data.accepted) { 
            this.logged = true;
            localStorage.userMail = res.data.user[4];
            localStorage.userPass = res.data.user[8];
            localStorage.userType = res.data.user[10];
            this.token = res.data.token;
          }

          this.$emit("logging", this.logged);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    }, 
    firstCharge() {
            localStorage.userMail = localStorage.userMail || " ";
            localStorage.userPass = localStorage.userPass || " ";
            localStorage.userType = localStorage.userType || " ";
    },
  },
  mounted() {
    this.firstCharge();
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
img {
  max-width: 100%;
  height: 300px;
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
  color: #ffffff;
}
.login {
  background-color: #102797;
  width: 30%;
  position: relative;
  margin-left: auto;
  margin-right: auto;
  padding: 1%;
  border-radius: 12px;
}
input {
  font-size: 18px;
  margin-top: 20px;
  width: 80%;
  height: 30px;
  border-style: none;
  border-radius: 5px;
}
button {
  position: relative;
  background-color: #90cbee;
  border: none;
  font-size: 18px;
  color: #000000;
  padding: 10px;
  width: 150px;
  text-align: center;
  -webkit-transition-duration: 0.4s; /* Safari */
  transition-duration: 0.4s;
  text-decoration: none;
  overflow: hidden;
  cursor: pointer;
}
.button:after {
    content: "";
    background: #FFFFFF;
    display: block;
    position: absolute;
    padding-top: 300%;
    padding-left: 350%;
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
