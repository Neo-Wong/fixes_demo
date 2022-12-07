FROM python:3.9-slim-buster

RUN apt-get update \
    && apt-get install nginx vim -y --no-install-recommends

# COPY deploy/nginx.default /etc/nginx/sites-available/default

WORKDIR /fixes_web

RUN chown -R www-data:www-data /fixes_web

EXPOSE 8000
STOPSIGNAL SIGTERM