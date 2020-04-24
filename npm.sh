#!/bin/sh
cd /tmp  
cp /workspace/oicjob/package.json /tmp/package.json
npm install
mv ./node_modules /workspace/oicjob/node_modules