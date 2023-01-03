FROM node:latest

WORKDIR /app
ADD package.json /app/package.json
RUN npm install 
COPY . /app
CMD npm start
EXPOSE 8002