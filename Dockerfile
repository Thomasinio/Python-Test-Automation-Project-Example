FROM python:3.8.12-slim-buster

ENV PYTHONUNBUFFERED=1

COPY . .

RUN apt-get update && apt-get install -y --no-install-recommends openjdk-11-jdk
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-interaction --no-ansi

CMD ["poetry", "run", "pytest"]
CMD ["allure_cli/bin/allure", "serve", "--host", "0.0.0.0", "--port", "8080", "tests/allure_results"]