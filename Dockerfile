FROM python:3.12.1-alpine3.19

LABEL mantainer="freitas.dev@proton.me"

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

COPY . /app

WORKDIR /app

VOLUME /app

EXPOSE 1404

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt

RUN apk update && apk add git

RUN adduser --disabled-password --no-create-home anderson && \
    mkdir -p /data/web/static && \
    mkdir -p /data/web/media && \
    chown -R anderson:anderson /data/web/static && \
    chown -R anderson:anderson /data/web/media && \    
    chmod -R 755 /data/web/static && \
    chmod -R 755 /data/web/media && \
    chmod -R +x /app

ENV PATH="/app:/app/venv/bin:$PATH"

USER anderson

CMD ["sh","./build.sh"]