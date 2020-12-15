FROM python:3.9.0-alpine3.12 as base
RUN apk add --no-cache --virtual .build-deps gcc musl-dev
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
ENTRYPOINT ["./entrypoint.sh"]

FROM base as prod
COPY entrypoint.sh .
COPY logging_config.json .
COPY ping_pong/src ping_pong/src

FROM base as dev
COPY requirements-dev.txt ./
RUN pip install -r requirements-dev.txt
COPY . .
