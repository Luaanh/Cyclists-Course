def juntar_tabelas():
    import pandas as pd
    arquivos = procurar_arquivos_extensao('./Data','.csv')
    tabelas = []
    for arquivo in arquivos:
        csv = pd.read_csv(arquivo)
        csv = csv[['rideable_type', 'started_at', 'ended_at', 'member_casual']]
        tabelas.append(csv)
    df_unido = pd.DataFrame()
    for tabela in tabelas:
        df_unido = pd.concat([df_unido, tabela], ignore_index=True)
    df_unido.to_csv('csv_unificado.csv',index=False,encoding='utf-8')
def procurar_arquivos_extensao(pasta, extensao=None):
    import os
    encontrados = []
    try:
        for arquivo in os.listdir(pasta):
            caminho_completo = os.path.join(pasta, arquivo)
            if os.path.isfile(caminho_completo):
                if extensao is None or arquivo.endswith(extensao):
                    encontrados.append(caminho_completo)
    except FileNotFoundError:
        print(f'A pasta {pasta} não foi encontrada.')
    except PermissionError:
        print(f'Permissão negada para acessar {pasta}.')
    return encontrados
def extrair(arquivo_zip, destino):
    import zipfile
    with zipfile.ZipFile(arquivo_zip, 'r') as zip_ref:
        zip_ref.extractall(destino)
    print(f'Arquivo extraído {arquivo_zip} para: {destino}')
def procurar_arquivos_extrair(pasta, extensao=None):
    import os
    encontrados = []
    for raiz, _, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            if extensao is None or arquivo.endswith(extensao):
                encontrados.append(os.path.join(raiz, arquivo))
    return encontrados