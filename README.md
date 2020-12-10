# SYMCOM API

## INSTALLATION

Make sure you have python >= 3.8 installed as well as [poetry](https://python-poetry.org/).
Then from the project root directory run:

```bash
poetry shell
poetry install
```

Now you can startup the server with.

```bash
uvicorn app.main:app --reload
```

And access the API docs via at [localhost:8000](http://localhost:8000/docs)