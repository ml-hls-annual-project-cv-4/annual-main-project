FROM python

LABEL maintainer="Maksim Kovalenko"

RUN groupadd kovalenko_ms
RUN useradd -ms /bin/bash -g kovalenko_ms kovalenko_ms

WORKDIR /home/kovalenko_ms

COPY . .

RUN pip install --upgrade pip \
&& pip install --no-cache-dir -r requirements.txt \
&& pip install opencv-python-headless \
&& pip install scikit-image 

