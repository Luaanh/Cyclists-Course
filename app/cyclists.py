import pandas as pd
import matplotlib.pyplot as plt
import psycopg2
from postgres_connect import conectar_postgres, criar_tabela
import arquivos
import subprocess
import pymsgbox
def contagem_bicicletas_por_dia(conn):
    query = '''
    SELECT 
        EXTRACT(DOW FROM started_at) AS day_of_week,
        member_casual,
        COUNT(rideable_type) AS count_bicicletas,
        rideable_type
    FROM 
        public.cyclists_data
    WHERE rideable_type != 'electric_scooter'
    GROUP BY 
        day_of_week, member_casual,rideable_type
    ORDER BY 
        day_of_week, member_casual,rideable_type
    '''
    df = pd.read_sql_query(query, conn)
    mapear_dia = {
        0: ('Domingo', 0),
        1: ('Segunda', 1),
        2: ('Terça', 2),
        3: ('Quarta', 3),
        4: ('Quinta', 4),
        5: ('Sexta', 5),
        6: ('Sábado', 6)
    }
    df['day_of_week'] = df['day_of_week'].map(lambda x: mapear_dia[x][0])
    df['day_order'] = df['day_of_week'].map({name: order for order, (name, order) in mapear_dia.items()})
    pivot_df = df.pivot_table(index=['day_of_week', 'rideable_type'], columns='member_casual', values='count_bicicletas')
    pivot_df = pivot_df.reindex(sorted(pivot_df.index, key=lambda x: df['day_order'][df['day_of_week'] == x[0]].values[0]))
    plt.figure(figsize=(12, 8))
    for member_type in pivot_df.columns:
        for rideable_type in pivot_df.index.get_level_values(1).unique():
            data = pivot_df.xs(rideable_type, level='rideable_type')
            plt.plot(data.index, data[member_type], marker='o', label=f'{rideable_type} - {member_type}')
    plt.title('Contagem de Bicicletas por Dia da Semana e Tipo de Usuário')
    plt.xlabel('Dia da Semana')
    plt.ylabel('Contagem de Bicicletas')
    plt.xticks(rotation=45)
    plt.legend(title='Tipo de Bicicleta e Usuário', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.grid()
    plt.show()
def tempo_medio_viagens(conn):
    query = '''
    SELECT 
        EXTRACT(DOW FROM started_at) AS day_of_week,
        member_casual,
        AVG(EXTRACT(EPOCH FROM (ended_at - started_at))) AS avg_duration_seconds
    FROM 
        public.cyclists_data
    GROUP BY 
        day_of_week, member_casual
    ORDER BY 
        day_of_week, member_casual;
    '''
    df = pd.read_sql_query(query, conn)
    mapear_dia = {
        0: ('Domingo', 0),
        1: ('Segunda', 1),
        2: ('Terça', 2),
        3: ('Quarta', 3),
        4: ('Quinta', 4),
        5: ('Sexta', 5),
        6: ('Sábado', 6)
    }
    df['day_of_week'] = df['day_of_week'].map(lambda x: mapear_dia[x][0])
    df['day_order'] = df['day_of_week'].map({name: order for order, (name, order) in mapear_dia.items()})
    pivot_df = df.pivot(index='day_of_week', columns='member_casual', values='avg_duration_seconds')
    pivot_df = pivot_df.reindex(sorted(pivot_df.index, key=lambda x: df['day_order'][df['day_of_week'] == x].values[0]))
    plt.figure(figsize=(10, 6))
    for member_type in pivot_df.columns:
        plt.plot(pivot_df.index, pivot_df[member_type], marker='o', label=member_type)
    plt.title('Média de Duração das Viagens por Dia da Semana')
    plt.xlabel('Dia da Semana')
    plt.ylabel('Média de Duração (segundos)')
    plt.xticks(rotation=45)
    plt.legend(title='Tipo de Usuário')
    plt.tight_layout()
    plt.grid()
    plt.show()
def main():
    arquivos_encontrados = arquivos.procurar_arquivos_extrair(r'.\Zip', '.zip')
    print(f'Arquivos encontrados ({len(arquivos_encontrados)}):')
    for arquivo in arquivos_encontrados:
        arquivos.extrair(arquivo, r'.\Data')
    arquivos.juntar_tabelas()
    with conectar_postgres as conn: 
        cur = conn.cursor()
        criar_tabela(conn,cur)
        pymsgbox.alert(text='Utilize o comando no PSQL')
        tempo_medio_viagens(conn)
        contagem_bicicletas_por_dia(conn)
        cur.close()
        plt.close()
if __name__ == "__main__":
    main()