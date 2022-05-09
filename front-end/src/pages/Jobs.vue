<template>
  <div id="jobs">
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

    <div>
    <p>Buscar trabajo: </p>
      <input type="text" id="myInput" @input="searchProveedor()">
      <select v-model="typeFilter">
        <option @click="searchProveedor()" value="">Cualquiera</option>
        <option @click="searchProveedor()" value="Instalacion de agua">Instalacion de agua</option>
        <option @click="searchProveedor()" value="Instalacion de gas">Instalacion de gas</option>
        <option @click="searchProveedor()" value="Revision de agua">Revision de agua</option>
        <option @click="searchProveedor()" value="Revision de gas">Revision de gas</option>
        <option @click="searchProveedor()" value="Reparacion">Reparacion</option>
        <option @click="searchProveedor()" value="otro">otro</option>
      </select>
    </div>
    <div v-if="forceReload && logged && searchedText" class="col-">
      <table class="table table-striped" id="jobs" v-if="jobsLoaded">
        <thead>
          <tr>
            <th>Id</th>
            <th>Tipo</th>
            <th>Descripcion</th>
            <th>Direccion</th>
            <th>Cliente</th>
            <th>Certificado</th>
            <th>Presupuesto</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(job,i) in searchedJobs" :key="i">
            <td><a style="color: blue;text-decoration: underline blue; cursor: pointer;" @click="redirectJob(job.id)"> {{job.id}} </a></td> 
            <td> {{job.tipo}} </td> 
            <td> {{job.descripcion}} </td> 
            <td> {{job.direccion}} </td> 
            <td><a style="color: blue;text-decoration: underline blue; cursor: pointer;" @click="redirectUser(job.id_cliente)">Ver cliente</a></td> 
            <td v-if="job.certificado == null"> <input type="file" id="certificado" name="certificado" ref="certificado" @change="uploadFile(job.id, i, 'certificado')" accept=".pdf"/> </td>
            <td v-if="job.certificado != null"> <a style="color: blue;text-decoration: underline blue; cursor: pointer;" @click="downloadPDF(job.id, 'certificado')">Ver certificado</a> <a @click="borrarDocumento(job.id, 'certificado')"> <svg viewBox="0 0 15 20" width="20" height="20"><path id="lineBC" d="M 3 4 L 3 16 C 3 19 3 19 6 19 L 11 19 C 14 19 14 19 14 16 L 14 4 L 12 4 L 12 16 L 11 16 L 11 4 L 9 4 L 9 16 L 8 16 L 8 4 L 6 4 L 6 16 L 5 16 L 5 4 L 3 4 M 3 3 L 14 3 L 14 2 C 10 0 7 0 3 2 L 3 3" stroke="black" stroke-width="0.01"  /></svg></a> </td>
            <td v-if="job.presupuesto == null"> <input type="file" id="presupuesto" name="presupuesto" ref="presupuesto" @change="uploadFile(job.id, i, 'presupuesto')" accept=".pdf"/> </td>
            <td v-if="job.presupuesto != null"> <a style="color: blue;text-decoration: underline blue; cursor: pointer;" @click="downloadPDF(job.id, 'presupuesto')">Ver presupuesto</a> <a @click="borrarDocumento(job.id, 'presupuesto')"> <svg viewBox="0 0 15 20" width="20" height="20"><path id="lineBC" d="M 3 4 L 3 16 C 3 19 3 19 6 19 L 11 19 C 14 19 14 19 14 16 L 14 4 L 12 4 L 12 16 L 11 16 L 11 4 L 9 4 L 9 16 L 8 16 L 8 4 L 6 4 L 6 16 L 5 16 L 5 4 L 3 4 M 3 3 L 14 3 L 14 2 C 10 0 7 0 3 2 L 3 3" stroke="black" stroke-width="0.01"  /></svg></a> </td>
            <td><a href="#miModal" @click="editar(job)"> Editar </a></td> 
          </tr>
        </tbody>
      </table>
    </div>
    
    <br><br>

    <h3>TRABAJOS</h3>
    <div class="lds-roller" style="position: absolute; margin-left: auto; left: 50%; top: 40%;" v-if="!forceReload"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
    <div v-if="forceReload && logged" class="col-">
      <table class="table table-striped" id="jobs" v-if="jobsLoaded">
        <thead>
          <tr>
            <th>Id</th>
            <th>Tipo</th>
            <th>Descripcion</th>
            <th>Direccion</th>
            <th>Cliente</th>
            <th>Certificado</th>
            <th>Presupuesto</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(job,i) in jobs" :key="i">
            <td><a style="color: blue;text-decoration: underline blue; cursor: pointer;" @click="redirectJob(job.id)"> {{job.id}} </a></td> 
            <td> {{job.tipo}} </td> 
            <td> {{job.descripcion}} </td> 
            <td> {{job.direccion}} </td> 
            <td><a style="color: blue;text-decoration: underline blue; cursor: pointer;" @click="redirectUser(job.id_cliente)">Ver cliente</a></td> 
            <td v-if="job.certificado == null"> <input type="file" id="certificado" name="certificado" ref="certificado" @change="uploadFile(job.id, i, 'certificado')" accept=".pdf"/> </td>
            <td v-if="job.certificado != null"> <a style="color: blue;text-decoration: underline blue; cursor: pointer;" @click="downloadPDF(job.id, 'certificado')">Ver certificado</a> <a @click="borrarDocumento(job.id, 'certificado')"> <svg viewBox="0 0 15 20" width="20" height="20"><path id="lineBC" d="M 3 4 L 3 16 C 3 19 3 19 6 19 L 11 19 C 14 19 14 19 14 16 L 14 4 L 12 4 L 12 16 L 11 16 L 11 4 L 9 4 L 9 16 L 8 16 L 8 4 L 6 4 L 6 16 L 5 16 L 5 4 L 3 4 M 3 3 L 14 3 L 14 2 C 10 0 7 0 3 2 L 3 3" stroke="black" stroke-width="0.01"  /></svg></a> </td>
            <td v-if="job.presupuesto == null"> <input type="file" id="presupuesto" name="presupuesto" ref="presupuesto" @change="uploadFile(job.id, i, 'presupuesto')" accept=".pdf"/> </td>
            <td v-if="job.presupuesto != null"> <a style="color: blue;text-decoration: underline blue; cursor: pointer;" @click="downloadPDF(job.id, 'presupuesto')">Ver presupuesto</a> <a @click="borrarDocumento(job.id, 'presupuesto')"> <svg viewBox="0 0 15 20" width="20" height="20"><path id="lineBC" d="M 3 4 L 3 16 C 3 19 3 19 6 19 L 11 19 C 14 19 14 19 14 16 L 14 4 L 12 4 L 12 16 L 11 16 L 11 4 L 9 4 L 9 16 L 8 16 L 8 4 L 6 4 L 6 16 L 5 16 L 5 4 L 3 4 M 3 3 L 14 3 L 14 2 C 10 0 7 0 3 2 L 3 3" stroke="black" stroke-width="0.01"  /></svg></a> </td>
            <td><a href="#miModal" @click="editar(job)"> Editar </a></td> 
          </tr>
        </tbody>
      </table>
    </div>

    <h3 v-if="individualJob">CITAS ASOCIADAS</h3>
    <div class="lds-roller" style="position: absolute; margin-left: auto; left: 50%; top: 40%;" v-if="individualJob && !forceReload"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
    <div v-if="individualJob && forceReload && logged">
      <table class="table table-striped" id="jobs" v-if="meetingsLoaded">
        <thead>
          <tr>
            <th>Descripcion</th>
            <th>Direccion</th>
            <th>Fecha</th>
            <th>Hora</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(cita,i) in citas" :key="i">
            <td>{{ cita.descripcion }}</td> 
            <td>{{ cita.direccion }}</td>
            <td>{{ cita.fechaCompleta }}</td>
            <td>{{ cita.dates.toLocaleTimeString() }}</td> 
          </tr>
        </tbody>
      </table>
    </div>

    <h3 v-if="individualJob">CITAS SIN ASOCIAR A NINGÚN TRABAJO</h3>
    <div class="lds-roller" style="position: absolute; margin-left: auto; left: 50%; top: 40%;" v-if="individualJob && !forceReload"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
    <div v-if="individualJob && forceReload && logged">
      <table class="table table-striped" id="jobs" v-if="NAMeetingsLoaded">
        <thead>
          <tr>
            <th>Descripcion</th>
            <th>Direccion</th>
            <th>Fecha</th>
            <th>Hora</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(citaSinAsociar,i) in citasSinAsociar" :key="i">
            <td>{{ citaSinAsociar.descripcion }}</td> 
            <td>{{ citaSinAsociar.direccion }}</td>
            <td>{{ citaSinAsociar.fechaCompleta }}</td>
            <td>{{ citaSinAsociar.dates.toLocaleTimeString() }}</td> 
            <button style="background-color: #207fdd; color: white;" @click="asociarCita(citaSinAsociar)">Añadir cita a este trabajo</button>
          </tr>
        </tbody>
      </table>
    </div>

    <br>
    <a v-if="!individualJob" href="#miModal" @click="setActualJob(newJob)" style="background-color: transparent; color: blue; width: 120px;">Crear trabajo</a>

    <div id="miModal" class="modal" v-if="forceReload">
      <div class="modal-contenido">
        <button style="background-color: rgba(21, 63, 117, 0.6); width: 8%; border: 2px solid #153f75; align-text: center;" @click="reloadSite">X</button>
        <p>Tipo:</p>
        <select v-model="actualJob.tipo">
          <option value="Instalacion de agua">Instalacion de agua</option>
          <option value="Instalacion de gas">Instalacion de gas</option>
          <option value="Revision de agua">Revision de agua</option>
          <option value="Revision de gas">Revision de gas</option>
          <option value="Reparacion">Reparacion</option>
          <option value="otro">otro</option>
        </select>
        <p>Descripcion:</p>
        <input v-model="actualJob.descripcion"/>
        <p>Direccion:</p>
        <input v-model="actualJob.direccion"/>

        <p v-if="crear">Cliente:      </p>
        <select v-if="crear" v-model="selectedUser"><option v-for="user in users" v-bind:key="user.dni" :value="user.dni">{{user.nombre}} {{user.apellidos}} - {{user.dni}}</option></select>


      <br>

      <button
        v-if="!crear"
        class="button"
        @click="actualizar(actualJob)"
        href="#">
          Actualizar
      </button>
      
      <button
        v-if="!crear"
        class="button red"
        @click="eliminar(actualJob)"
        href="#"  >
          Eliminar
      </button>

      
      <button
        v-if="crear"
        class="button"
        @click="createJob"
        href="#"  >
          Crear
      </button>
      <p v-if="errorInForm" style="color: red;"> {{errorMessage}} </p>
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
      citasSinAsociar: [],
      meetingsLoaded: false,
      NAMeetingsLoaded: false,
      individualJob: false,
      newJob: {
        new: true,
        tipo: null,
        descripcion: "",
        direccion: "",
        id_cliente: null,
        certificado: null
      },
      actualJob: {},
      users: [],
      selectedUser: null,
      crear: true,
      errorInForm: false,
      errorMessage: "",
      searchedJobs: [],
      searchedText: "",
      changeSearch: false,
      typeFilter: "",
    }
  },
  methods: {
    searchProveedor() {
      this.changeSearch = false;
      
      this.searchedJobs = [];
      this.searchedText = document.getElementById("myInput").value;
      if (this.searchedText != "") {
          for (let index = 0; index < this.jobs.length; index++) {
              var element = this.jobs[index];
              if (element.descripcion.toLowerCase().includes(this.searchedText.toLowerCase())) {
                if (this.typeFilter != "") {
                  if (element.tipo == this.typeFilter) {
                    this.searchedJobs[index] = element;
                  }
                } else {
                  this.searchedJobs[index] = element;
                }
              }
          }

          this.searchedJobs.sort((a, b) => a.descripcion >= b.descripcion);
          this.searchedJobs = this.searchedJobs.filter(function (el) {
            return el != null;
          });
      }
      this.changeSearch = true;
    },
    redirectJob(jobId) {
      this.$router.push("/jobs/" + jobId);
      this.$router.go();
    },
    borrarDocumento(job_id, tipo) {
      if (tipo == "certificado") {
        axios.delete(`${process.env.VUE_APP_BACK_URL}/certificados/${job_id}`, {
          headers: {
            "Access-Control-Allow-Origin": "*",
            "Authorization": this.token
          },
        })
        .then(response => {
          console.log(response);
            this.reloadSite();
        })
        .catch(error => {
          console.log(error);
        });
      } else if (tipo == "presupuesto") {
        axios.delete(`${process.env.VUE_APP_BACK_URL}/presupuestos/${job_id}`, {
          headers: {
            "Access-Control-Allow-Origin": "*",
            "Authorization": this.token
          },
        })
        .then(response => {
          console.log(response);
            this.reloadSite();
        })
        .catch(error => {
          console.log(error);
        });
      }
      
    },
    downloadPDF(job_id, tipo) {
      if (tipo == "certificado") {
        axios.get(`${process.env.VUE_APP_BACK_URL}/certificados/${job_id}`, {
          headers: {
            'Content-Type': 'application/pdf',
            "Access-Control-Allow-Origin": "*",
            "Authorization": this.token
          },
          responseType: 'blob',
          Accept: 'application/pdf'
        })
        .then((response) => {
          const url = window.URL.createObjectURL(new Blob([response.data]));
          const link = document.createElement('a');
          link.href = url;
          link.setAttribute('download', `certificado-trabajo${job_id}.pdf`); //or any other extension
          document.body.appendChild(link);
          link.click();
        });
      } else if (tipo == "presupuesto") {
        axios.get(`${process.env.VUE_APP_BACK_URL}/presupuestos/${job_id}`, {
          headers: {
            'Content-Type': 'application/pdf',
            "Access-Control-Allow-Origin": "*",
            "Authorization": this.token
          },
          responseType: 'blob',
          Accept: 'application/pdf'
        })
        .then((response) => {
          const url = window.URL.createObjectURL(new Blob([response.data]));
          const link = document.createElement('a');
          link.href = url;
          link.setAttribute('download', `certificado-trabajo${job_id}.pdf`); //or any other extension
          document.body.appendChild(link);
          link.click();
        });
      }
    },
    uploadFile(job_id, index, tipo) {
      var formData = new FormData();
      var file;
      if (tipo == "certificado") {
        file = this.$refs.certificado;
        formData.append("file", file[index].files[0]);
        axios.post(`${process.env.VUE_APP_BACK_URL}/certificados/${job_id}`, formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
            "Access-Control-Allow-Origin": "*",
            "Authorization": this.token
          }
        }).then(() => {
          this.reloadSite();
        }).catch((err) => {
          console.log(err);
        });
      } else if (tipo == "presupuesto") {
        file = this.$refs.presupuesto;
        formData.append("file", file[index].files[0]);
        axios.post(`${process.env.VUE_APP_BACK_URL}/presupuestos/${job_id}`, formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
            "Access-Control-Allow-Origin": "*",
            "Authorization": this.token
          }
        }).then(() => {
          this.reloadSite();
        }).catch((err) => {
          console.log(err);
        });
      }
      
    },
    modifyDateTime(meeting) {
        var year = meeting.dates.toISOString().split("T")[0].split("-")[0];
        var day = meeting.dates.toISOString().split("T")[0].split("-")[1];
        var month = meeting.dates.toISOString().split("T")[0].split("-")[2];
        var hour = meeting.dates.toISOString().split("T")[1].split(":")[0];
        var minutes = meeting.dates.toISOString().split("T")[1].split(":")[1];
        
  
        if (Date().includes("GMT+0100")) {
          hour = (Number(hour) + 1) + "";
        }
        else if (Date().includes("GMT+0200")) {
          hour = (Number(hour) + 2) + "";
        }

        if (hour < 10) hour = "0" + hour;
        var dateFormat =  year + "-" + day + "-" + month + "T" + hour + ":" + minutes;
        return dateFormat;
    },
    asociarCita(cita) {
      var uri = window.location.href;

      const path = `${process.env.VUE_APP_BACK_URL}/editMeetings/`+cita.id;
      const config = {
        method: 'put',
        url: path,
        data: {
          "fecha": this.modifyDateTime(cita),
          "descripcion": cita.descripcion,
          "direccion": cita.direccion,
          "id_trabajo": uri.split("jobs/")[1],
          "id_tecnico": cita.id_tecnico,
          "id_perito": cita.id_perito,
          "id_administrador": null,
          "certificado": null
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
          console.log(res);
          this.reloadSite();
        }
      })
      .catch((error) => {
        // eslint-disable-next-line
        console.error(error);
      });
    },
    editar(job) {
      this.crear = false;
      this.setActualJob(job);
    },
    createJob() {
      var path = "";
        const config = {
          method: 'post',
          url: "",
          data: {
            "dni": this.selectedUser,
            "tipo": this.actualJob.tipo,
            "descripcion": this.actualJob.descripcion,
            "direccion": this.actualJob.direccion
          },
          headers: {
            "Content-Type": "application/JSON",
            "Access-Control-Allow-Origin": "*",
            "Authorization": this.token
          }
        }

      path = `${process.env.VUE_APP_BACK_URL}/addJobs`;

      config.url = path;
      if (this.selectedUser == null) {
        this.errorInForm = true;
        this.errorMessage = "Debe seleccionar un cliente";
      } else {
        this.errorInForm = false;
        axios(config)
        .then((res) => {
          console.log(res);
          this.reloadSite();
        });
      }
      
    },
    reloadSite() {
      var ruta = ("/jobs/"+window.location.href.split("/jobs/")[1]).split("#")[0];
      if (ruta.includes("undefined")) {
        ruta = "/jobs";
      }
      this.$router.push(ruta);
      this.$router.go();
    },
    actualizar() {
        const path = `${process.env.VUE_APP_BACK_URL}/editJobs/${this.actualJob.id}`;
        const config = {
          method: 'put',
          url: path,
          data: {
            "tipo": this.actualJob.tipo,
            "descripcion": this.actualJob.descripcion,
            "direccion": this.actualJob.direccion,
            "certificado": null
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
            console.log(res);
            this.reloadSite();
          }
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });

    },
    eliminar() {
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
        const path = `${process.env.VUE_APP_BACK_URL}/deleteJob/${this.actualJob.id}`;
        config.url = path;
        axios(config)
        .then((res) => {
          console.log(res);
          this.reloadSite();
        });
    },
    setActualJob(job) {
      this.actualJob = job;
    },
    loadJobs() {
      var uri = window.location.href;
      this.thisUri = uri.split("jobs/")[0];
      var extension;
      var extCitas;
      var NACitas = "/citasSinAsociar";
      if (uri.split("jobs/")[1]) {
        this.individualJob = true;
        extension = "/trabajo/" + uri.split("jobs/")[1];
        extCitas = "/citas/" + uri.split("jobs/")[1];
      } else {
        extension = "/trabajos";
        extCitas = "/citas";
      }
      const path = `${process.env.VUE_APP_BACK_URL}` + extension;
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

          if (Date().includes("GMT+0100")) element.fecha += "+0100";
          else if (Date().includes("GMT+0200")) element.fecha += "+0200";
          
          var cita = {
            dot: true,
            dates: new Date(element.fecha),
            descripcion: element.descripcion,
            direccion: element.direccion,
            id_trabajo: element.id_trabajo,
            id_cita: element.id,
            certificado: element.certificado,
            id_perito: element.id_perito,
            id_tecnico: element.id_tecnico,
          }

          cita.fechaCompleta = ("0" + cita.dates.getDate()).slice(-2) + "/" + ("0" + (cita.dates.getMonth() + 1)).slice(-2) + "/" +  cita.dates.getFullYear();
          this.citas[index] = cita;
        }
        this.meetingsLoaded = true;
        this.jobsLoaded = true;
      });

      
      const path3 = `${process.env.VUE_APP_BACK_URL}` + NACitas;
      const config3 = {
        method: 'get',
        url: path3,
        headers: {
          "Content-Type": "application/JSON",
          "Access-Control-Allow-Origin": "*",
          "Authorization": this.token
        }
      }
      axios(config3)
      .then((res) => {
        for (let index = 0; index < res.data.length; index++) {
          var element = res.data[index];

          if (Date().includes("GMT+0100")) element.fecha += "+0100";
          else if (Date().includes("GMT+0200")) element.fecha += "+0200";
          
          var cita = {
            id: element.id,
            dot: true,
            dates: new Date(element.fecha),
            descripcion: element.descripcion,
            direccion: element.direccion,
            id_trabajo: element.id_trabajo,
            id_cita: element.id,
            certificado: element.certificado,
            id_perito: element.id_perito,
            id_tecnico: element.id_tecnico,
          }

          cita.fechaCompleta = ("0" + cita.dates.getDate()).slice(-2) + "/" + ("0" + (cita.dates.getMonth() + 1)).slice(-2) + "/" +  cita.dates.getFullYear();
          this.citasSinAsociar[index] = cita;
        }
        this.NAMeetingsLoaded = true;
      });

      
      config.url = `${process.env.VUE_APP_BACK_URL}/clients`;
      axios(config)
      .then((res) => {
        for (let index = 0; index < res.data.length; index++) {
          var element = res.data[index];
          this.users[index] = element;
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
