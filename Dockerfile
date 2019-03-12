FROM python:alpine

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

USER nobody

CMD ["pypy3","scrape.py"]

COPY source.txt logger.py functii.py scrape.py ./