FROM node:12.18-alpine3.11

ENV PROJECT_NAME "oicjob"

RUN apk add --no-cache bash && \
    apk add --no-cache git python3 curl && \
    npm install -g npm && \
    yarn global add @vue/cli

# プロンプトの左のやつの表示
ENV PS1 "\s:\w# "

WORKDIR /workspace