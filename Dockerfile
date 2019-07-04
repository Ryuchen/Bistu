FROM alpine:latest

LABEL maintainer="Ryuchen <chenhaom1993@hotmail.com>"

RUN mkdir -p /opt/web && mkdir -p /opt/simpleui

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories

RUN apk update && apk upgrade
RUN apk add py3-pip
RUN apk add --update sqlite sqlite-dev vim git python3 \
  python3-dev build-base zlib zlib-dev libxml2-dev libxslt-dev libffi-dev gcc \
  musl-dev libgcc openssl-dev curl libjpeg jpeg-dev tiff freetype lcms libwebp tcl openjpeg

COPY ./ /opt/web

RUN git clone https://github.com/Ryuchen/simpleui-modify.git /opt/simpleui

WORKDIR /opt/web

RUN pip3 install whitenoise gunicorn --no-cache-dir --trusted-host repo --index-url https://mirrors.aliyun.com/pypi/simple/

RUN pip3 install -r requirements.txt --no-cache-dir --trusted-host repo --index-url https://mirrors.aliyun.com/pypi/simple/

RUN rm -rf ls /usr/lib/python3.7/site-packages/simpleui
RUN ln -s /opt/simpleui/simpleui /usr/lib/python3.7/site-packages/simpleui

ENV DJANGO_SETTINGS_MODULE=web.settings

EXPOSE 8080

CMD exec gunicorn web.wsgi:application --bind 0.0.0.0:8080 --workers 2