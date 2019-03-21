FROM python:alpine

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

USER nobody

CMD ["python","main.py"]

COPY main.py utils ./