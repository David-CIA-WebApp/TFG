<template>
  <div id="app">
    <radial-menu
      style="margin: auto; margin-top: 300px; background-color: white; "
      :itemSize="110"
      :radius="120"
      :angle-restriction="360">
        <radial-menu-item 
          v-for="(item, index) in items" 
          :key="index" 
          style="margin-left: -60px; background-color: blue;" 
          @click="() => handleClick(item)">
          <span style="font-size: 13px; color: white;">{{item}}</span>
        </radial-menu-item>
      </radial-menu>
  </div>
</template>
 
<script>
import { RadialMenu,  RadialMenuItem } from 'vue-radial-menu'
 
export default {
  name: 'app',
  components: {
    RadialMenu,
    RadialMenuItem
  },
  data () {
    return {
      items: ['AGENDA', 'USUARIOS', 'MATERIALES', 'TRABAJOS', 'PRESUPUESTOS', 'PROVEEDORES']
    }
  },
  methods: {
    handleClick (item) {
        this.$emit("handleClick", item);
    },
  }
}
</script> 