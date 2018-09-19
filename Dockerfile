FROM frolvlad/alpine-python2
RUN echo \
  # replacing default repositories with edge ones
  && echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" > /etc/apk/repositories \
  && echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories \
  && echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories

WORKDIR /app

COPY scrape.py ./scrape.py

RUN apk update && apk add wget ca-certificates libxslt-dev py-lxml
RUN python -m pip install schedule &&\ 
  python -m pip install beautifulsoup4 &&\
  python -m pip install lxml &&\
  python -m pip install bs4
VOLUME ["/app/emag.txt", "/app/read.txt"]
CMD ["python", "scrape.py"]