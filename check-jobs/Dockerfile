FROM node:14.16.0
COPY index.js /app
COPY package.json /app
COPY package-lock.json /app
WORKDIR /app
RUN npm install
CMD ["npm", "start"]