FROM alpine:edge

COPY scrape.py ./scrape.py

RUN apk add wget python py-beautifulsoup4
RUN python3 -m pip install mysql-connector schedule

ENTRYPOINT ["python3", "scrape.py"]