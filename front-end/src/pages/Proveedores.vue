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

        
        <table class="table table-striped" id="users">
            <thead>
                <th>Comercio</th>
                <th>Direccion</th>
                <th>Email</th>
                <th>Telefono</th>
            </thead>
            <tbody v-for="proveedor in proveedores" v-bind:key="proveedor">
                <tr>
                    <td>{{ proveedor.nombre }}</td>
                    <td>{{ proveedor.direccion }}</td>
                    <td>{{ proveedor.email }}</td>
                    <td>{{ proveedor.telefono }}</td>
                    <td><a href="#miModal" @click="editarProveedor(proveedor)"> Editar </a></td> 
                </tr>
            </tbody>
        </table>

            
        <div id="miModal" class="modal" v-if="forceReload">
        <div class="modal-contenido">
            <button style="background-color: rgba(21, 63, 117, 0.6); width: 8%; border: 2px solid #153f75; align-text: center;" @click="reloadSite">X</button>
            <h3 style="margin-bottom: -2%;">{{proveedorActual.nombre}}</h3>
            <p>Comercio:</p>
            <input v-model="proveedorActual.nombre"/>
            <p>Direccion:</p>
            <input v-model="proveedorActual.direccion"/>
            <p>Email:</p>
            <input v-model="proveedorActual.email"/>
            <p>Telefono:</p>
            <input v-model="proveedorActual.telefono"/>


            <br>
        </div>  
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
            proveedores: [],
            proveedorActual: {
                nombre: '',
                direccion: '',
                email: '',
                telefono: ''
            }
        }
    },
    methods: {
        reloadSite() {
            this.$router.push('');
            this.$router.go();
        },
        editarProveedor(proveedor) {
            this.proveedorActual = proveedor;
            console.log(this.proveedorActual);
        },
        loadProveedores() {
            console.log("Debug");
            this.proveedores = [];
            axios.get(`${process.env.VUE_APP_BACK_URL}/proveedores`, {headers:{
                "Content-Type": "application/JSON",
                "Access-Control-Allow-Origin": "*",
                "Authorization": this.token
            }}).then(response => {
                for (let i = 0; i < response.data.length; i++) {
                    var element = response.data[i];
                    this.proveedores.push(element);
                }
                
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
                this.loadProveedores();
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

</style>