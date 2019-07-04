FROM alpine:latest

LABEL maintainer="Ryuchen <chenhaom1993@hotmail.com>"

RUN mkdir -p /opt/bistu && mkdir -p /opt/simpleui

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories

RUN apk add --update sqlite sqlite-dev vim git python3 \
  python3-dev build-base zlib zlib-dev libxml2-dev libxslt-dev libffi-dev gcc \
  musl-dev libgcc openssl-dev curl libjpeg jpeg-dev tiff freetype lcms libwebp tcl openjpeg

COPY ./ /opt/bistu

RUN git clone https://github.com/Ryuchen/simpleui-modify.git /opt/simpleui

WORKDIR /opt/bistu

RUN pip3 install gunicorn --trusted-host repo --index-url https://mirrors.aliyun.com/pypi/simple/

RUN pip3 install -r requirements.txt --trusted-host repo --index-url https://mirrors.aliyun.com/pypi/simple/

# RUN rm -rf /opt/bistu/.venv/lib/python3.7/site-packages/simpleui
# RUN ln -s /opt/simpleui/simpleui /opt/bistu/.venv/lib/python3.7/site-packages/simpleui

ENV DJANGO_SETTINGS_MODULE=web.settings

RUN gunicorn --bind 0.0.0.0:8080 web.wsgi

EXPOSE -P 8554:8080
