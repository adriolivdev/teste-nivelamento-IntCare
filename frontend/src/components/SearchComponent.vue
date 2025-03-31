<template>
  <div class="search-component">
    <!-- Barra de Pesquisa -->
    <div class="search-bar">
      <input 
        type="text" 
        v-model="query" 
        placeholder="Digite o termo de busca..."
        @keyup.enter="search"
      />
      <button @click="search">Buscar</button>
    </div>

    <!-- Carregando -->
    <div v-if="loading" class="loading">
      Carregando...
    </div>
    
    <!-- Resultados -->
    <div v-else>
      <h2>Resultados</h2>
      <ul>
        <li v-for="operadora in operadoras" :key="operadora.Registro_ANS">
          <div class="operadora-card">
            <div class="operadora-name">{{ operadora.Razao_Social }}</div>
            <div class="operadora-cnpj">CNPJ: {{ operadora.CNPJ }}</div>
          </div>
        </li>
      </ul>

      <!-- Nenhum resultado -->
      <div v-if="!operadoras.length && query" class="no-result">
        Nenhum resultado encontrado.
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'SearchComponent',
  data() {
    return {
      query: '',
      operadoras: [],
      loading: false
    };
  },
  methods: {
    async search() {
      if (!this.query) return;
      this.loading = true;
      try {
        const response = await axios.get('http://192.168.1.4:8000/search', {
          params: { q: this.query }
        });
        this.operadoras = response.data;
      } catch (error) {
        console.error("Erro ao buscar operadoras:", error);
        this.operadoras = [];
      } finally {
        this.loading = false;
      }
    }
  }
};
</script>

<style scoped>
/* Importando a fonte Montserrat, similar à usada no site da Intuitive Care */
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600&display=swap');

.search-component {
  max-width: 700px;
  margin: 50px auto;
  padding: 30px;
  background-color: #ffffff;
  border-radius: 8px;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.08);
  font-family: 'Montserrat', sans-serif;
  color: #7341b0; /* Texto em tom escuro */
}

/* Barra de pesquisa */
.search-bar {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 20px;
}

.search-bar input {
  flex: 1;
  padding: 12px 16px;
  border: 2px solid #eaeaea;
  border-radius: 6px;
  font-size: 16px;
  transition: border-color 0.3s ease;
}

.search-bar input:focus {
  border-color: #7341b0; /* Roxo inspirado na identidade */
  outline: none;
}

.search-bar button {
  padding: 12px 20px;
  font-size: 16px;
  font-weight: 600;
  color: #fff;
  background: #7341b0; /* Roxo inspirado na identidade */ 
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: background 0.3s ease;
}

.search-bar button:hover {
  background: #c8a4f4; /* Roxo mais claro para hover */;
}

/* Título dos resultados */
h2 {
  text-align: center;
  margin-top: 20px;
  font-size: 24px;
  color: #7341b0; /* Destaque no roxo */
}

/* Lista de resultados */
ul {
  list-style: none;
  padding: 0;
  margin: 20px 0;
}

li {
  margin-bottom: 20px;
}

/* Card de cada operadora */
.operadora-card {
  padding: 16px;
  border: 1px solid #f2f2f2;
  border-radius: 6px;
  transition: box-shadow 0.3s ease;
}

.operadora-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.operadora-name {
  font-size: 18px;
  font-weight: 600;
  color: #333;
}

.operadora-cnpj {
  margin-top: 6px;
  font-size: 14px;
  color: #555;
}

/* Mensagem de carregando / sem resultados */
.loading,
.no-result {
  text-align: center;
  font-size: 16px;
  color: #7341b0; /* Roxo para destaque */
  margin-top: 20px;
}
</style>
