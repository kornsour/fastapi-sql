# tdd-fastapi

Test-driven development with the FastAPI Python web framework and Docker

## Development Environment

This app can be run in either a dev container or virtual environment

### Dev Container

Learn how to use a [dev container](https://code.visualstudio.com/docs/remote/containers#_quick-start-try-a-development-container)

### Virtual Environment

Learn how to use a [virtual envionrment](https://docs.python.org/3/tutorial/venv.html)

## Starting the App

Once your dev env is set up, run `uvicorn app.main:app`

### Environment Variables

By default the app has a settings class that sets the env vars `ENVIRONMENT` to `dev` and `TESTING` to `0` (False)

For a production environment, we can override these variables with something similar to this:

`export ENVIRONMENT=prod`
`export TESTING=1`

## Docker

### Building the Container

`docker-compose build`

### Starting the container

`docker-compose up -d`

### Check logs
`docker-compose logs web`





