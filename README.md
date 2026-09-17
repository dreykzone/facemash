# Facemash

Aplicação Flask na qual usuários votam entre duas pessoas e o ranking é calculado por Elo.

## Executar com Docker

O SQLite fica em um volume Docker para que os dados persistam entre reinicializações.

```bash
docker compose up --build
```

A aplicação estará disponível em `http://localhost:5000`.

Ao iniciar, o container executa `flask db upgrade` e o seed. O seed só insere dados quando a tabela está vazia.

## Executar localmente

```bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
flask --app run.py db upgrade
flask --app run.py seed
flask --app run.py run
```

O banco padrão é `instance/facemash.db`. Para usar outro arquivo, defina `SQLALCHEMY_DATABASE_URI`, por exemplo:

```bash
SQLALCHEMY_DATABASE_URI=sqlite:///outro.db flask --app run.py db upgrade
```

O seed também pode ser executado diretamente com `python3 seed.py`.

## Migrations

Depois de alterar um modelo, gere uma migration com:

```bash
flask --app run.py db migrate -m "descreva a alteração"
flask --app run.py db upgrade
```
