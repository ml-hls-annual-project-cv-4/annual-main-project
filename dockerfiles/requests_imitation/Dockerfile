FROM python

WORKDIR .

COPY . .

RUN apt-get update \
&& pip install --upgrade pip \
&& pip install --no-cache-dir -r requirements.txt

CMD python src/monitoring/requests_imitation.py
