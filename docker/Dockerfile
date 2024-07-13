FROM python:3.12-slim

ENV MAIN_DIR /opt/services/eventic-backend

WORKDIR ${MAIN_DIR}

COPY .. ${MAIN_DIR}

RUN apt-get update \
    && pip install uv \
    && uv pip install --no-cache-dir -r src/requirements/dev.txt --system
