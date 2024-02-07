# Django-Boilerplate
Django-Boilerplate for start a new project

## How to set up project (with Docker)

Give permission to docker script: ```chmod +x ./docker-compose```
Give permission to docker script: ```chmod +x entrypoint.dev.sh```

### Docker compose file
Build and docker up containers: ```docker-compose -f docker-compose.dev.yml up -d --build```

### Use docker-compose file
```./docker-compose makemigrations``` or ```docker-compose -f docker-compose.dev.yml exec backend python manage.py makemigrations```

## How to run project locally bash script (Linux, Mac)

### install requirements

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements/develop.text
```

### create .env file

```bash
cp .env.example .env
```

### create database

```bash
sudo -u postgres psql
CREATE DATABASE django_boilerplate;
CREATE USER django_boilerplate WITH PASSWORD 'django_boilerplate';
ALTER ROLE django_boilerplate SET client_encoding TO 'utf8';
ALTER ROLE django_boilerplate SET default_transaction_isolation TO 'read committed';
ALTER ROLE django_boilerplate SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE django_boilerplate TO django_boilerplate;
\q
```

### set up .env file with your database credentials

```bash
nano .env
```

### run migrations

```bash
python manage.py migrate
```

### run server

```bash
python manage.py runserver
```

## Pre-commit  must be installed for all projects

```bash
pip install pre-commit
pre-commit install
```

# [Back-End checklist](https://ruzimurodovnodirjon.notion.site/ruzimurodovnodirjon/Backend-Checklist-90f8dd9a09744d19a7b43cd0aa77d9ad) you must check your project by checklist

