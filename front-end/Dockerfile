# syntax=docker/dockerfile:1
FROM node:14.16.0
WORKDIR /app
ADD src .
ADD public .
ADD babel.config.js .
ADD package-lock.json .
ADD package.json .
RUN npm i
CMD ["npm", "run", "serve"]