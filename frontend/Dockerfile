FROM node:latest
WORKDIR /app
COPY package*.json ./
COPY babel.config.js ./
COPY .eslintrc.js ./
RUN npm install
COPY ./ .
