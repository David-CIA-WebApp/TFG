FROM node:14.16.0
WORKDIR /usr/src/app
COPY package*.json ./

RUN npm install
COPY . .
RUN node index.js