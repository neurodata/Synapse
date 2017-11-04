FROM ubuntu:16.04

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

COPY . /app
RUN pip install -r /app/requirements.txt
WORKDIR /app

ENTRYPOINT ["python"]
CMD ["NOMADS_driver.py"]
