FROM python

WORKDIR .

COPY . .

RUN  apt-get update \
&& pip install --upgrade pip \
&& pip install --no-cache-dir -r requirements.txt

CMD python -m uvicorn api.main:app --host 0.0.0.0 --port 3000
