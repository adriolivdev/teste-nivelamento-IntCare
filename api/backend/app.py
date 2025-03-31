# Importo as bibliotecas necessárias para a API.
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List
import mysql.connector
from mysql.connector import Error
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Crio a instância do FastAPI, definindo título, descrição e versão da API.
app = FastAPI(
    title="API de Busca de Operadoras",
    description="API desenvolvida com FastAPI para buscar dados cadastrais das operadoras armazenadas no MySQL.",
    version="1.0"
)

# Adiciono o middleware CORS para permitir requisições de diferentes origens.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite requisições de qualquer origem.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Defino um modelo Pydantic para a resposta que será enviada para o cliente.
class Operadora(BaseModel):
    Registro_ANS: str
    Razao_Social: str
    CNPJ: str

# Função para obter uma conexão com o banco de dados MySQL.
def get_db_connection():
    try:
        # Estabelece a conexão utilizando as variáveis de ambiente definidas no arquivo .env.
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),           # Ex: "localhost"
            user=os.getenv("DB_USER"),           # Ex: "root"
            password=os.getenv("DB_PASSWORD"),   # Ex: "MinhaSenhaSecreta!!"
            database=os.getenv("DB_NAME")        # Ex: "ans_data"
        )
        return connection
    except Error as e:
        # Se ocorrer erro na conexão, imprimo o erro e retorno None.
        print("Erro ao conectar com o MySQL:", e)
        return None

# Endpoint para realizar a busca de operadoras.
@app.get("/search", response_model=List[Operadora], summary="Busca de Operadoras", 
         description="Retorna até 10 operadoras cuja Razao_Social contenha o termo de busca informado.")
def search_operadoras(q: str = Query(..., description="Termo de busca para a Razao_Social da operadora")):
    # Obtenho a conexão com o banco
    connection = get_db_connection()
    if not connection:
        raise HTTPException(status_code=500, detail="Erro ao conectar com o banco de dados")
    
    # Crio um cursor com dicionário para obter resultados em formato de dicionário
    cursor = connection.cursor(dictionary=True)
    try:
        # Query SQL para buscar as operadoras utilizando LIKE para filtrar pela Razao_Social
        query = """
        SELECT Registro_ANS, Razao_Social, CNPJ
        FROM operadoras
        WHERE Razao_Social LIKE %s
        LIMIT 10;
        """
        # Preparo o termo de busca com os caracteres '%' para a operação LIKE
        search_term = f"%{q}%"
        cursor.execute(query, (search_term,))
        resultados = cursor.fetchall()
    except Error as e:
        raise HTTPException(status_code=500, detail=f"Erro na consulta: {e}")
    finally:
        # Fecho o cursor e a conexão
        cursor.close()
        connection.close()
    
    return resultados

# Bloco principal para rodar o servidor FastAPI usando Uvicorn.
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)  # Altere a porta se necessário
    # Para rodar a API, você também pode executar:
    # uvicorn api.backend.app:app --reload
