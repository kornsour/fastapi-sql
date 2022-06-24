# tdd-fastapi

Test-driven development with FastAPI, Docker, and PostgreSQL

## Development Environment

This app can be run in either a dev container or on Docker locally

### Dev Container

Learn how to use a [dev container](https://code.visualstudio.com/docs/remote/containers#_quick-start-try-a-development-container)

### Docker

Learn how to use a [Docker](https://docs.docker.com/get-started/overview/)

## Starting the App

Once your dev env is set up, run `docker-compose up -d --build`

### Environment Variables

By default the app has a settings class that sets the env vars `ENVIRONMENT` to `dev` and `TESTING` to `0` (False)

For a production environment, we can override these variables with something similar to this:

`export ENVIRONMENT=prod`
`export TESTING=1`

## Docker Commands

- Building the container
  - `docker-compose build`
- Starting the container
  - `docker-compose up -d`
- Build and start container
  - `docker-compose up -d --build`
- Check logs
  `docker-compose logs web`
- Connect to database
  - `docker-compose exec web-db psql -U postgres`
  - `\c web_dev`
  - `\q`
- Run pytest
  - `docker-compose exec web python -m pytest`
- Run code coverage
  - `docker-compose exec web python -m pytest --cov="."`
- View code coverage as HTML
  - `docker-compose exec web python -m pytest --cov="." --cov-report html`
- Flake8 linting
  - `docker-compose exec web flake8 .`

## Database

Commands (in no specific order):

- Init
  - `docker-compose exec web aerich init -t app.db.TORTOISE_ORM`
  - Creates a config file: `project/pyproject.toml`
- Create first migration
  - `docker-compose exec web aerich init-db`
  - Should see new file `migrations/models`
- Apply migration with Aerich
  - `docker-compose exec web aerich upgrade`
- Manually generate schema
  - `docker-compose exec web python app/db.py`
  - May be times where you just want to apply the schema to the database in its final state

Tortoise:

- [Tortoise.init](https://tortoise-orm.readthedocs.io/en/latest/setup.html?highlight=init#tortoise.Tortoise.init)
- [Generate Schemas](https://tortoise-orm.readthedocs.io/en/latest/setup.html?highlight=init#tortoise.Tortoise.generate_schemas)
- [Aerich Migrations](https://tortoise-orm.readthedocs.io/en/latest/migration.html)
- [Values](https://tortoise-orm.readthedocs.io/en/latest/query.html?highlight=values#tortoise.queryset.QuerySet.values)
  - [Values Query](https://tortoise-orm.readthedocs.io/en/latest/query.html?highlight=values#tortoise.queryset.ValuesQuery)

## Testing

- [Starlette Test Client](https://www.starlette.io/testclient/)
- [FastAPI Dependency Overrides](https://fastapi.tiangolo.com/advanced/testing-dependencies/#use-the-appdependency_overrides-attribute)
- [Fixtures](https://docs.pytest.org/en/stable/explanation/fixtures.html#scope-sharing-fixtures-across-classes-modules-packages-or-session)
  - [All You Need to Know to Start Using Fixtures in Your pytest Code](https://pybit.es/pytest-fixtures.html)
  - [Fixture finalization / executing teardown code](https://docs.pytest.org/en/latest/explanation/fixtures.html#improvements-over-xunit-style-setup-teardown-functions)
- [Given-When-Then framework](https://martinfowler.com/bliki/GivenWhenThen.html)
- [HTTPie](https://httpie.io/)
- [Coverage.py](https://coverage.readthedocs.io/en/6.4.1/)

## FastAPI

- [Event Handlers](https://fastapi.tiangolo.com/advanced/events/)

## Pydantic

- [Overview](https://pydantic-docs.helpmanual.io/)
- [Models](https://pydantic-docs.helpmanual.io/usage/models/)

## Gunicorn

- [Overview](https://gunicorn.org/)
- [Worker class](https://www.uvicorn.org/#running-with-gunicorn)

## Heroku

- [Non-root user](https://devcenter.heroku.com/articles/container-registry-and-runtime#run-the-image-as-a-non-root-user)
- [Port binding](https://devcenter.heroku.com/articles/dynos#web-dynos)
- [CLI](https://devcenter.heroku.com/articles/heroku-cli)
- [Container Registry](https://devcenter.heroku.com/articles/container-registry-and-runtime)
- [Postgres Plan](https://devcenter.heroku.com/articles/heroku-postgres-plans#hobby-tier)
- [Dynos](https://www.heroku.com/dynos)
