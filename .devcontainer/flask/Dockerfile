FROM python:3.7.4

RUN git clone https://github.com/wgdp444/oicjob-rest-api.git && \
    cd oicjob-rest-api && \
    pip install -r requirements.txt

WORKDIR /oicjob-rest-api/src

CMD ["python3 app.py"]


