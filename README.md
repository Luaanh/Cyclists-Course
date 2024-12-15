# Estudo de Caso da Cyclistic

## Ferramentas
- **Python**
- **Postgres**
- **SQL**

## Bibliotecas
As bibliotecas utilizadas estão listadas no arquivo **`Requirements.txt`**.

## Objetivo
Responder à seguinte pergunta: **"Como os membros anuais e casuais ciclistas usam bicicletas Cyclistic de forma diferente?"**, que foi dividida em duas sub-perguntas:

1. **"Qual seria a diferença no tempo médio de viagem de ambos os tipos de assinaturas?"**
2. **"Qual seria o tempo médio da bicicleta utilizada por cada tipo de assinatura?"**

## Estrutura do Projeto

### Arquivos e Funções Principais

- **`arquivos.py`**
  - Função `procurar_arquivos_extrair`: Identifica arquivos com extensão `.zip`, cria uma lista e utiliza um laço `for` para extrai-los com a função `extrair`.
  - Função `juntar_tabelas`: Junta todas as tabelas extraídas e filtra apenas as colunas necessárias dos arquivos `.csv`.

- **`postgres_connect.py`**
  - Função `conectar_postgres`: Estabelece a conexão com o banco de dados Postgres.
  - Função `criar_tabela`: Cria a tabela **`cyclists_data`** com as informações necessárias.

  Após criar a tabela, o arquivo **`csv_unificado.csv`** é importado para o Postgres utilizando o seguinte comando no PSQL:

  ```sql
  \COPY cyclists_data (rideable_type, started_at, ended_at, member_casual) FROM 'caminho\csv_unificado.csv' DELIMITER ',' CSV HEADER;
  ```

- **`cyclists.py`**
  - Arquivo principal que integra as funcionalidades dos outros dois arquivos.
  - Responsável por criar os gráficos para responder às perguntas do estudo de caso.

## Fluxo do Processo
1. Identificar e extrair os arquivos `.zip`.
2. Unificar os dados relevantes em um único arquivo `.csv`.
3. Conectar ao banco de dados Postgres e criar a tabela necessária.
4. Importar os dados para o banco de dados.
5. Analisar os dados e gerar gráficos para responder às perguntas do estudo de caso.

---

## Dados
Os dados utilizados neste estudo de caso são fornecidos como parte de um curso na plataforma Coursera. Por questões de direitos autorais e de privacidade, esses dados não podem ser disponibilizados neste repositório.

Se você deseja replicar este estudo de caso, recomendo se inscrever no curso [Google Data Analytics Professional Certificate](https://www.coursera.org/professional-certificates/google-data-analytics) na Coursera, onde os dados originais podem ser acessados. Alternativamente, você pode adaptar o código para trabalhar com conjuntos de dados públicos semelhantes.

---

## Notas
- Certifique-se de que o banco de dados Postgres está configurado corretamente antes de executar os scripts.
- As bibliotecas necessárias podem ser instaladas utilizando:

  ```bash
  pip install -r Requirements.txt
  ```

- O caminho do arquivo **`csv_unificado.csv`** deve ser ajustado conforme a localização no seu sistema.
