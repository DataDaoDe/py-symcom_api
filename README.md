# SYMCOM API

This project is a stepwise computer algebra system. It is designed with education purposes in mind and therefore is mainly focused on providing easy to follow, machine and human readable, step-by-step solutions to solving mathematical problems.

It can accept latex as input, parse that into sympy's symbolic expression language, and return latex as output for rendering nicely to a browser or other latex compatible rendering engines.


## INSTALLATION

Make sure you have python >= 3.8 installed as well as [poetry](https://python-poetry.org/).
Then from the project root directory run:

```bash
poetry shell
poetry install
```

Now you can run the tests.

```bash
pytest
```