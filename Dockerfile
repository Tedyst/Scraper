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

RUN python3 -m pip install schedule &&\ 
  python3 -m pip install beautifulsoup4 &&\
  python3 -m pip install lxml &&\
  python3 -m pip install discord.py &&\
  python3 -m pip install asyncio &&\
  python3 -m pip install bs4
VOLUME ["/app/emag.txt", "/app/read.txt"]
CMD ["python3", "scrape.py"]

COPY scrape.py ./scrape.py