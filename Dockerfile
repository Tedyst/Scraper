FROM alpine
RUN echo \
  # replacing default repositories with edge ones
  && echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" > /etc/apk/repositories \
  && echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories \
  && echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories

WORKDIR /app

RUN apk update && apk add --no-cache wget ca-certificates libxslt-dev py-lxml libxml2 gcc libc6-compat libc-dev python3 \
  bash \
  ffmpeg \
  libsodium-dev \
  opus \
  python3 \
  libffi-dev \
  musl-dev

COPY requirements.txt ./
RUN python3 -m pip install -r requirements.txt

USER nobody

CMD ["python3","-u","scrape.py"]

COPY source.txt logger.py functii.py scrape.py ./