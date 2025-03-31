Nesta etapa, desenvolvi o backend da aplicação usando FastAPI para criar uma API RESTful que se conecta ao banco de dados MySQL. Meu objetivo principal foi construir uma camada de serviços que permita a busca dinâmica dos dados cadastrais das operadoras.
api_backend/
├── app.py               # Arquivo principal da aplicação FastAPI
├── docs.md              # Documentação da API (explica rotas, como executar, etc.)
└── requirements.txt     # Lista de dependências necessárias para rodar a API (FastAPI, Uvicorn, etc.)


## Objetivo
- Criar uma API capaz de receber requisições de busca, filtrando os dados da tabela de operadoras com base em um termo fornecido.
- Retornar os resultados no formato JSON para serem consumidos por uma futura interface (frontend).

## Tecnologias Utilizadas
- **FastAPI:** Para construir a API, oferecendo alta performance, validação automática com Pydantic e documentação interativa.
- **Uvicorn:** Para rodar a aplicação FastAPI como um servidor ASGI.
- **MySQL:** Banco de dados onde os dados das operadoras foram previamente importados.
- **MySQL Connector/Python:** Biblioteca para conectar a API ao banco de dados.

## O Que Eu Fiz
- **Configuração do Servidor:**  
  Criei uma instância do FastAPI definindo título, descrição e versão, o que possibilitou a geração automática da documentação interativa (acessível via `/docs`).
  
- **Criação de Endpoints:**  
  Implementei um endpoint `/search` que recebe um parâmetro de consulta (`q`). Este endpoint executa uma consulta SQL que utiliza o operador `LIKE` para filtrar a coluna `Razao_Social` na tabela `operadoras` e retorna até 10 registros correspondentes.

- **Conexão com o Banco de Dados:**  
  Desenvolvi uma função para estabelecer a conexão com o MySQL, garantindo que a API possa acessar os dados armazenados no banco `ans_data`.

- **Tratamento de Erros:**  
  Incluí tratamento de exceções para lidar com falhas na conexão e na execução de consultas, garantindo que a API retorne mensagens de erro claras caso algo dê errado.

## Principais Desafios
- **Integração e Validação de Dados:**  
  Utilizar o FastAPI com Pydantic facilitou a validação dos dados de entrada e saída, mas exigiu atenção à formatação correta dos dados.
- **Documentação Automática:**  
  Aproveitei a funcionalidade do FastAPI para gerar a documentação interativa, o que foi essencial para testar e validar os endpoints durante o desenvolvimento.
- **Conexão com o MySQL:**  
  Garantir que a conexão estivesse correta e que as credenciais fossem configuradas adequadamente para que a API acessasse os dados do banco sem problemas.

## Conclusão
Desenvolvi com sucesso uma API backend robusta e moderna usando FastAPI, que permite buscar e retornar dados das operadoras armazenadas no MySQL. Essa camada de serviços está pronta para ser integrada com um frontend e fornece uma base sólida para futuras expansões e funcionalidades adicionais.




