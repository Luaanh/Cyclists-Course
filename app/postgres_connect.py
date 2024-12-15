def conectar_postgres():
    import psycopg2
    from psycopg2 import OperationalError
    try:
        conn = psycopg2.connect(dbname="postgres",user="postgres",password="74181",host="localhost",port="5432")
        print("Conexão ao PostgreSQL bem-sucedida!")
        return conn
    except OperationalError as e:
        print(f"Erro na conexão: {e}")
        return None
def criar_tabela(conn,cur):
    import pandas as pd
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS cyclists_data (
    rideable_type TEXT,
    started_at TIMESTAMP,
    ended_at TIMESTAMP,
    member_casual TEXT);''')
    conn.commit()
