FROM node:alpine

ENV PROJECT_NAME "oicjob"

RUN apk add --no-cache bash && \
    apk add --no-cache git python3 && \
    pip install flask && \
    npm install -g npm && \
    cd oicjob && npm install

# プロンプトの左のやつの表示
ENV PS1 "\s:\w# "

WORKDIR /workspace