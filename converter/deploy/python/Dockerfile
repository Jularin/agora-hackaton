FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY poetry.lock /app/
COPY pyproject.toml /app/
RUN pip install poetry==1.1.13
RUN poetry config virtualenvs.create false
RUN poetry install
COPY . /app/
