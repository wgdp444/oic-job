FROM node:alpine

RUN apk add --no-cache bash && \
    apk add --no-cache git python3 && \
    npm install -g npm @vue/cli

# プロンプトの左のやつの表示
ENV PS1 "\s:\w# "

WORKDIR /workspace