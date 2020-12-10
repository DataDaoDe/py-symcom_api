# SYMCOM API

This project is a wrapper around computer algebra and symbolic computation libraries. It allows us
to automatically solve equations. It also parses latex and converts from latex to symbolic math and from
symbolic math back to latex for rendering purposes.

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

And access the API docs via at [localhost:8000/docs](http://localhost:8000/docs)