FROM python:3.12-slim

RUN pip install poetry

RUN mkdir /src

WORKDIR /src

COPY pyproject.toml poetry.lock* /src/

RUN poetry install

COPY . /src

CMD ["poetry", "run", "uvicorn", "src.main:main_app", "--host", "0.0.0.0", "--port", "8080"]