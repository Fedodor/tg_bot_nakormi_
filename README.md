

![Python](https://img.shields.io/badge/Python-Async%20Bot-informational?logo=python)
![aiogram](https://img.shields.io/badge/aiogram-3-informational?logo=telegram)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-informational?logo=sqlalchemy)
![Alembic](https://img.shields.io/badge/Alembic-Migrations-informational)
![Redis](https://img.shields.io/badge/Redis-Cache%20Layer-informational?logo=redis)
![Docker](https://img.shields.io/badge/Docker-Compose-informational?logo=docker)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI-informational?logo=githubactions)

Telegram bot for a pet-help project. The bot is designed to support communication and simple workflows around helping domestic animals.

The project is useful for showing async Python, aiogram, environment-based configuration, database migrations and Docker setup.

## Current status

The repository is still in an early stage. The setup is prepared, but the README and product description should be improved as the bot logic grows.

## Tech stack

| Area | Tools |
| --- | --- |
| Bot | Python, aiogram 3 |
| Database layer | SQLAlchemy |
| Migrations | Alembic |
| Config | Pydantic Settings, python-dotenv |
| Cache / broker-ready layer | Redis |
| Infrastructure | Docker, Docker Compose |
| CI | GitHub Actions |

## Setup

Create a Telegram bot through [@BotFather](https://t.me/BotFather), then add the token to your environment file.

Clone the repository:

```bash
git clone git@github.com:Fedodor/tg_bot_nakormi_.git
cd tg_bot_nakormi_
```

Create environment variables from the example file:

```bash
cp .env.example .env
```

Start the development environment:

```bash
docker compose -f docker-compose-dev.yml up --build
```
