FROM python:3.10-alpine
WORKDIR /app
COPY requirements/backend.in /app/requirements/backend.in
RUN python -m venv .venv && . .venv/bin/activate && pip install -r requirements/backend.in
COPY . /app
CMD ["uvicorn", "spaceship.main:app", "--host=0.0.0.0", "--port=8080"]