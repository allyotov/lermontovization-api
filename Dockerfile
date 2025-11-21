FROM ghcr.io/astral-sh/uv:python3.12-alpine

COPY uv.lock pyproject.toml /app/

WORKDIR /app
RUN uv sync --locked

COPY src/ ./src
EXPOSE 8000

CMD ["uv", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
