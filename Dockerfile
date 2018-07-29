FROM frolvlad/alpine-python2
RUN echo \
  # replacing default repositories with edge ones
  && echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" > /etc/apk/repositories \
  && echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories \
  && echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories


COPY scrape.py ./scrape.py

RUN apk update && apk add wget ca-certificates
RUN python -m pip install mysql-connector && \
  python -m pip install schedule &&\ 
  python -m pip install beautifulsoup4

ENTRYPOINT ["python", "scrape.py"]