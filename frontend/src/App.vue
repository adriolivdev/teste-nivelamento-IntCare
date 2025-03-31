<template>
  <div id="app">
    <h1>Busca de Operadoras</h1>
    <!-- Componente de busca que se conecta à API -->
    <SearchComponent/>
  </div>
</template>

<script>
// Importo o componente de busca
import SearchComponent from './components/SearchComponent.vue';

export default {
  name: 'App',
  components: {
    SearchComponent
  }
};
</script>

<style scoped>
/* Estilos básicos para o App */
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  margin: 20px;
}
</style>
