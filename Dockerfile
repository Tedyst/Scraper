FROM alpine:edge

RUN echo \
  # replacing default repositories with edge ones
  && echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" > /etc/apk/repositories \
  && echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories \
  && echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories


COPY scrape.py ./scrape.py

RUN apk add wget python
RUN python -m pip install mysql-connector && \
  python -m pip install schedule &&\ 
  python -m pip install beautifulsoap4

ENTRYPOINT ["python3", "scrape.py"]