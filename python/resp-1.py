# Implementação de LRUCache
# A implementação do LRUCache (Least Recently Used Cache) utiliza a classe OrderedDict do Python, que mantém a ordem 
# de inserção dos elementos. O objetivo aqui é criar uma estrutura de cache com capacidade limitada, onde os elementos menos
#  recentemente acessados são removidos quando o limite de capacidade é atingido.
# No método construtor, inicializamos um OrderedDict vazio e definimos a capacidade máxima do cache. 
# O método get recupera o valor de uma chave, movendo-a para o final do dicionário para marcar seu uso recente. 
# Se a chave não existir, retorna -1. O método put insere ou atualiza um valor, removendo a entrada mais antiga 
#  caso o cache atinja sua capacidade máxima.

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value


  ##***********************************************************************************************************
# Cálculo de Média Salarial
# Para calcular a média salarial dos funcionários com idade superior a 30 anos, pode -se utilizar 
# uma função que utiliza as capacidades de filtragem e agregação do pandas. A função recebe o DataFrame,
# aplica um filtro para selecionar apenas funcionários acima de 30 anos e calcula a média dos salários desse grupo.


import pandas as pd

def calcular_media_salario_acima_30(df):
    return df[df['idade'] > 30]['salario'].mean()

data = {
    'id': [1, 2, 3, 4, 5],
    'nome': ['Alice', 'Bob', 'Carlos', 'Daniel', 'Eva'],
    'idade': [25, 30, 35, 40, 45],
    'salario': [5000, 7000, 8000, 10000, 12000]
}
df = pd.DataFrame(data)

media_salario = calcular_media_salario_acima_30(df)
print(f"Média salarial (acima 30 anos): {media_salario}")


#***********************************************************************************************************

# Requisições HTTP Assíncronas
# A função assíncrona para buscar conteúdo de múltiplas URLs simultaneamente utiliza
#  as bibliotecas asyncio e aiohttp. Ela cria uma sessão de cliente assíncrona, gera tarefas para
#   cada URL e usa asyncio.gather para executar as requisições em paralelo, melhorando 
#   significativamente o desempenho em comparação com requisições sequenciais.
# A função retorna o conteúdo de todas as URLs, permitindo processamento posterior.

import asyncio
import aiohttp

async def fetch_urls(urls: list):
    async with aiohttp.ClientSession() as session:
        tasks = [session.get(url) for url in urls]
        responses = await asyncio.gather(*tasks)
        return [await resp.text() for resp in responses]

# Exemplo de uso
async def main():
    urls = [
        'https://api.example.com/data1',
        'https://api.example.com/data2',
        'https://api.example.com/data3'
    ]
    resultados = await fetch_urls(urls)
    for resultado in resultados:
        print(resultado)

asyncio.run(main())

#***********************************************************************************************************

# Otimização de Processamento de Logs
# Para otimizar o processamento de logs, criei uma classe DatabaseManager que implementa várias 
# melhorias de performance. Foi utilizado connection pooling para gerenciar eficientemente as conexões
#  com o banco de dados, reduzindo o overhead de criar e fechar conexões para cada operação.
# A estratégia é usar executemany para inserir múltiplos logs em uma única operação 
# de banco de dados, substituindo a abordagem comum de inserção individual. 
# Foi implementado também tratamento de erros com rollback e liberação adequada das conexões.

import psycopg2
from psycopg2 import pool

class DatabaseManager:
    def __init__(self, connection_params):
        self.connection_pool = psycopg2.pool.SimpleConnectionPool(
            1, 20, **connection_params
        )
    
    def process_logs(self, logs):
        conn = self.connection_pool.getconn()
        try:
            with conn.cursor() as cursor:
                cursor.executemany(
                    "INSERT INTO logs (timestamp, level, message) VALUES (%s, %s, %s)",
                    [(log['timestamp'], log['level'], log['message']) for log in logs]
                )
                conn.commit()
        except Exception as e:
            conn.rollback()
            print(f"Erro ao processar logs: {e}")
        finally:
            self.connection_pool.putconn(conn)

# Exemplo de uso
db_params = {
    "dbname": "test",
    "user": "postgres",
    "password": "secret",
    "host": "localhost"
}

manager = DatabaseManager(db_params)
logs = [
    {'timestamp': '2023-01-01', 'level': 'INFO', 'message': 'Sistema iniciado'},
    {'timestamp': '2023-01-01', 'level': 'ERROR', 'message': 'Falha na conexão'}
]
manager.process_logs(logs)


#***********************************************************************************************************

