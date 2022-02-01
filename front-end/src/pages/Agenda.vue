<template>
  <div>
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
    <br>
    <v-date-picker
      mode='range'
      v-model='date'
      :show-day-popover=false
      is-double-paned
      show-caps
      locale="es"
      :attributes="citas"
      @dayclick="onDayClick">
    </v-date-picker>
      <table class="table table-striped" id="users" v-if="citasMostradas.length != 0">
        <thead>
          <tr>
            <th>Descripcion</th>
            <th>Direccion</th>
            <th>Hora</th>
            <th>Trabajo</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(cita,i) in citasMostradas" :key="i">
            <td>{{ cita.descripcion }}</td> 
            <td>{{ cita.direccion }}</td>
            <td>{{ cita.dates.toLocaleTimeString() }}</td> 
            <td><a :href="'jobs/'+cita.id_trabajo">Ver trabajo</a></td> 
          </tr>
        </tbody>
      </table>
  </div>
</template>

<script>
  import axios from 'axios';
  import Vue from 'vue';
  import VCalendar from 'v-calendar'
    
    Vue.use(VCalendar);

  export default {
    data() {
        return {
          date: Date.now(),
          logged: false,
          forceReload: false,
          token: null,
          citas: [],
          citasMostradas: [],
          userType: null
        }
    },
    methods: {
      onDayClick: function () {
          this.citasMostradas = [];
        for (let i = 0; i < this.citas.length; i++) {
          var cita = this.citas[i];
          if (this.date.getFullYear() == cita.dates.getFullYear() && this.date.getMonth() == cita.dates.getMonth() && this.date.getUTCDate() == cita.dates.getUTCDate()) {
            this.citasMostradas.push(cita);
          }
        }
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
            this.loadAgenda();
          }
          
          this.$emit("logging", this.logged);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
      },
      loadAgenda() {
        const path = `${process.env.VUE_APP_BACK_URL}/citas`;
        const config = {
          method: 'get',
          url: path,
          headers: {
            "Content-Type": "application/JSON",
            "Access-Control-Allow-Origin": "*",
            "Authorization": this.token
          }
        };
        axios(config)
        .then((res) => {
          if (res.data) { 
            for (let i = 0; i < res.data.length; i++) {
              const element = res.data[i];

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

              this.citas.push(cita);
            }
          }
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


<style lang="postcss" scoped>
::-webkit-scrollbar {
  width: 0px;
}

::-webkit-scrollbar-track {
  display: none;
}

/deep/ .custom-calendar.vc-container {
  --day-border: 1px solid #b8c2cc;
  --day-border-highlight: 1px solid #b8c2cc;
  --day-width: 90px;
  --day-height: 90px;
  --weekday-bg: #f8fafc;
  --weekday-border: 1px solid #eaeaea;

  border-radius: 0;
  width: 100%;

  & .vc-header {
    background-color: #f1f5f8;
    padding: 10px 0;
  }
  & .vc-weeks {
    padding: 0;
  }
  & .vc-weekday {
    background-color: var(--weekday-bg);
    border-bottom: var(--weekday-border);
    border-top: var(--weekday-border);
    padding: 5px 0;
  }
  & .vc-day {
    padding: 0 5px 3px 5px;
    text-align: left;
    height: var(--day-height);
    min-width: var(--day-width);
    background-color: white;
    &.weekday-1,
    &.weekday-7 {
      background-color: #eff8ff;
    }
    &:not(.on-bottom) {
      border-bottom: var(--day-border);
      &.weekday-1 {
        border-bottom: var(--day-border-highlight);
      }
    }
    &:not(.on-right) {
      border-right: var(--day-border);
    }
  }
  & .vc-day-dots {
    margin-bottom: 5px;
  }
}
</style>
