FROM python:3.13-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:0.6.2 /uv /uvx /bin/

ADD . /app
WORKDIR /app
RUN uv sync --frozen --compile-bytecode

ENTRYPOINT ["uv", "run", "python"]
