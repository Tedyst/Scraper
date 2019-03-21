FROM python:alpine

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app
USER nobody

ENV PYTHONPATH /

CMD ["python","/main.py"]

COPY utils/__init__.py /
COPY utils /utils/
COPY main.py /