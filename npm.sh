#!/bin/sh
cd /tmp  
cp /workspace/oicjob/package.json /tmp/package.json
npm install --no-bin-links
npm audit fix
mv ./node_modules /workspace/oicjob/node_modules