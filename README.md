# api-py

Basic api with python.

## Commands

How to run the api.

#### Start database

```sh
docker compose up -d
```

#### Setup poetry

```sh
pip install poetry
```

#### Install dependencies

```sh
poetry install
```

#### Run database migrations

```sh
alembic upgrade head
```

#### Run api

```sh
poetry run app
```
