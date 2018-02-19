# Script para geração de gráficos 

### Tecnologias
  - Python 2.7.14
  - PostgreSQL 9.6.3

### Depências

  - psycopg2==2.7.3.2
  - pygal==2.4.0
  - lxml==4.1.0
  - CairoSVG==1.0.22
  - cssselect==1.0.3
  - tinycss==0.4

### Instalação

Instale as bibliotecas de desenvolvimento do Python 2:

```sh
$ sudo apt install libpq-dev python-dev
```
Após isso instale as depências:

```sh
$ pip install requirements.txt
```
Para configurar o usuário de conexão com o PG, basta editar o arquivo confs.py.

### Execução

Para rodar o script:

```sh
$ cd generate_line_chart
$ python generate.py
```
Os arquivos em PNG serão gerados dentro da pasta que contém o script.
