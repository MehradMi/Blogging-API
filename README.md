# Blogging REST API

A simple make believe blogging RESTful API built with FastAPI.

This project was created as a learning exercise to understand the fundamentals of back-end and REST API concepts.

## Features

- Create a blog post
- Get all available blog post
- Get a single blog post
- Update a blog post
- Delete a blog post

## Technologies

- Python
- FastAPI
- Pydantic
- uv

## Getting Started

### Clone the repository

```bash
git clone git@github.com:MehradMi/Blogging-API.git
cd Blogging-API
```

### Install dependencies

```bash
uv sync
```

### Run the development server

```bash
uv run uvicorn main:app --reload
```

or

```bash
source .venv/bin/activate # on mac/linux
fastapi dev &
```

The API will be available at:

```
http://127.0.0.1:8000
https://localhost:8000
```

Main documentation:

```
http://127.0.0.1:8000/docs
```

Alternative documentation:

```
http://127.0.0.1:8000/redoc
```

## Project Status

This project currently uses an in-memory Python list as its data store.

Planned improvements (TODO):

- Replace the in-memory list with a SQLite database
- Add SQLAlchemy ORM
- Implement search functionality (`GET /posts?term=...`)
- Improve error handling
- Add automated tests
