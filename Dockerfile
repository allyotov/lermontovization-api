
FROM ghcr.io/astral-sh/uv:python3.12-alpine

WORKDIR /app

COPY uv.lock .
COPY pyproject.toml .

RUN uv pip install --system -r pyproject.toml

COPY src/ ./src

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
