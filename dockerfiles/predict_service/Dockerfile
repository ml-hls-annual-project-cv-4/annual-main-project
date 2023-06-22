FROM python:3.8

WORKDIR .

COPY . .
RUN  apt-get update \
&& pip install virtualenv \
&& virtualenv env \
&& . env/bin/activate \
&& pip install --upgrade pip \
&& pip install -r requirements.txt \
&& apt-get install -y python3-opencv 

CMD . env/bin/activate && exec python -m uvicorn api.main:app --host 0.0.0.0 --port 3000 --ssl-keyfile api/private.key --ssl-certfile api/cert.crt
