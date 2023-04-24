FROM python:3.10

WORKDIR /app/power9bot

ENV POETRY_VIRTUALENVS_CREATE=false

RUN pip install poetry

COPY ["pyproject.toml", "poetry.lock", "/app/"]

RUN poetry install --no-ansi --no-interaction

COPY . /app

CMD ["python", "main.py"]

