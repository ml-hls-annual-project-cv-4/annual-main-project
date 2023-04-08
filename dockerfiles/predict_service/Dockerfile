FROM python

ARG BRANCH=develop

RUN cd home/ \
&& git clone -b $BRANCH https://github.com/ml-hls-annual-project-cv-4/annual-main-project.git

WORKDIR /home/annual-main-project

COPY . .

RUN  apt-get update \
&& pip install --upgrade pip \
&& pip install --no-cache-dir -r requirements.txt

CMD python -m uvicorn api.main:app --host 0.0.0.0 --port 80
