# Estrutura do Projeto – Frontend

A pasta **`frontend/`** contém o código da interface web desenvolvida com Vue.js. A seguir, apresento a estrutura atual do projeto:
frontend/
├── public/
│   └── index.html        # Arquivo HTML principal que carrega a aplicação Vue
├── src/
│   ├── components/
│   │   └── SearchComponent.vue   # Componente responsável pela busca e exibição dos resultados
│   ├── App.vue           # Componente raiz da aplicação Vue
│   └── main.js           # Arquivo de entrada que inicializa a aplicação Vue
├── docs.md               # Documentação do frontend (explicação, instruções de instalação, etc.)
├── package.json          # Gerenciamento de dependências e scripts do projeto
└── README.md             # Documentação geral do projeto (visão geral, objetivos, etc.)


## Descrição dos Arquivos

1. **`SearchComponent.vue`**  
   - **Objetivo:**  
     Componente que implementa a funcionalidade de busca, incluindo um campo de entrada para o termo de pesquisa e a lógica para enviar requisições à API.  
   - **Como funciona:**  
     - Possui um campo `<input>` para que o usuário digite o termo de busca.  
     - Usa a biblioteca Axios (ou `fetch`) para fazer requisições ao endpoint `/search` da API.  
     - Recebe e exibe os resultados em uma lista ou tabela, de forma reativa.

2. **`App.vue`**  
   - **Objetivo:**  
     É o componente raiz da aplicação Vue.  
   - **Como funciona:**  
     - Importa e utiliza o `SearchComponent.vue` (ou outros componentes) para compor a interface final.  
     - Geralmente contém a estrutura principal da aplicação, como cabeçalho, rodapé e roteamento (caso seja usado Vue Router).

3. **`main.js`**  
   - **Objetivo:**  
     Arquivo de inicialização da aplicação.  
   - **Como funciona:**  
     - Cria a instância do Vue (`new Vue(...)` ou `createApp(...)` dependendo da versão do Vue).  
     - Monta a aplicação no elemento HTML (por exemplo, `#app`) definido no `index.html`.  
     - Importa o `App.vue` e define se há uso de bibliotecas como Vue Router ou Vuex.

4. **`docs.md`**  
   - **Objetivo:**  
     Documento de apoio que descreve a finalidade do frontend, as bibliotecas utilizadas, instruções de instalação e execução.  
   - **Como funciona:**  
     - Pode conter detalhes sobre como instalar as dependências (`npm install` ou `yarn`), como rodar o servidor de desenvolvimento (`npm run serve` ou `yarn serve`) e como fazer o build para produção (`npm run build` ou `yarn build`).

---

## Fluxo Básico

1. **Usuário acessa o frontend:**  
   - A aplicação Vue é carregada no navegador a partir de um servidor local (por exemplo, `npm run serve`).

2. **Termo de busca:**  
   - O usuário digita o termo no `SearchComponent.vue` e clica em um botão ou pressiona Enter.

3. **Requisição à API:**  
   - O componente envia uma requisição GET ao endpoint `/search?q=<termo>` do backend (FastAPI).

4. **Recebimento de dados:**  
   - A API retorna um JSON com as operadoras correspondentes.  
   - O componente exibe os resultados na tela.

5. **Iteração contínua:**  
   - O usuário pode refinar o termo de busca, ver resultados em tempo real e interagir com outros componentes (se existirem).

---

## Conclusão

Esta estrutura permite um desenvolvimento modular e organizado no Vue.js, separando cada parte da aplicação em componentes reutilizáveis e mantendo um fluxo claro de dados. O arquivo `SearchComponent.vue` concentra a lógica de busca, enquanto `App.vue` orquestra a aplicação e `main.js` configura e inicia o app Vue.
