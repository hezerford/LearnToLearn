FROM python:3.12-slim

RUN pip install poetry && mkdir /src

WORKDIR /src

COPY pyproject.toml poetry.lock* /src/

RUN poetry install 
# можно прописать флаги --no-dev чтобы избежать установки зависимостей таких как
# pytest, unittest, flake8, black, setuptools и т.д
# и еще флаг --no-root, чтобы проект не устанавливался как зависимость 

COPY . /src

CMD ["poetry", "run", "uvicorn", "src.main:main_app", "--host", "0.0.0.0", "--port", "8080", "--reload"]