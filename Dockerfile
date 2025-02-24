FROM python:3.13-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:0.6.2 /uv /uvx /bin/

COPY . /app
WORKDIR /app
RUN uv sync --frozen --compile-bytecode

ENTRYPOINT ["/app/.venv/bin/fastapi", "dev", "app/main.py", "--port", "80", "--host", "0.0.0.0"]
