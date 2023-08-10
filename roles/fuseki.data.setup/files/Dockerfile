FROM docker.io/python:3.11-alpine

RUN apk add --no-cache \
        bash \
        curl \
        git

RUN pip install \
        https://github.com/Kurrawong/kurrawong-python/archive/refs/tags/0.3.2.zip \
        httpx \
        rich \
        rdflib

WORKDIR /app