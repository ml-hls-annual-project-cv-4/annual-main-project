FROM python

WORKDIR .

COPY . .

RUN  apt-get update \
&& pip install --upgrade pip \
&& pip install --no-cache-dir -r requirements.txt \
&& cat api/private.key

CMD python -m uvicorn api.main:app --host 0.0.0.0 --port 3000 --ssl-keyfile api/private.key --ssl-certfile api/cert.crt