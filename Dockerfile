FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml uv.lock README.md ./
COPY alembic.ini .
COPY alembic ./alembic
COPY src ./src

RUN pip install --no-cache-dir uv \
    && uv sync --frozen

EXPOSE 8000

CMD ["/app/.venv/bin/uvicorn", "bookverse.main:app", "--host", "0.0.0.0", "--port", "8000"]
