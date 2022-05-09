<template>
    <div id="consultas" v-if="logged">
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
        
        <br>

        <div v-for="consulta in consultas" v-bind:key="consulta">
            <p class="alert">El usuario <strong>{{consulta.nombre}}</strong> con correo electrónico <strong>{{consulta.correo}}</strong> ha dicho: <strong>{{consulta.descripcion}}</strong></p>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            logged: false,
            forceReload: false,
            token: null,
            userType: null,
            consultas: []
        }
    },
    methods: {
        loadConsultas() {
            this.consultas = [];
            axios.get(`${process.env.VUE_APP_BACK_URL}/consultas`, {headers:{
                "Content-Type": "application/JSON",
                "Access-Control-Allow-Origin": "*",
                "Authorization": this.token
            }}).then(response => {
                for (let i = 0; i < response.data.length; i++) {
                    var element = response.data[i];
                    this.consultas.push(element);
                }
                
                this.consultas.sort((a, b) => parseInt(a.id) < parseInt(b.id));
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
                this.forceReload = true;
                this.userType = localStorage.userType;
                this.token = res.data.token;
                this.loadConsultas();
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
    },
      
    mounted() {
        this.loadData();
    }
}
</script>

<style scoped>
.alert {
    background-color: #aaccfd;
    color: rgb(0, 0, 0);
    padding: 15px;
    margin-bottom: 15px;
}
</style>