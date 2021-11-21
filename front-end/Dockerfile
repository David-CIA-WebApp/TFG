# syntax=docker/dockerfile:1
FROM node:14.16.0

# instalar un simple servidor http para servir nuestro contenido estático
RUN npm install -g http-server

# hacer la carpeta 'app' el directorio de trabajo actual
WORKDIR /app

# copiar 'package.json' y 'package-lock.json' (si están disponibles)
COPY package*.json ./

# instalar dependencias del proyecto
RUN npm install

# copiar los archivos y carpetas del proyecto al directorio de trabajo actual (es decir, la carpeta 'app')
COPY . .

ENV VUE_APP_BACK_URL "http://141.94.203.217:8001"
# construir aplicación para producción minificada
RUN npm run build

CMD [ "http-server", "-P", "http://localhost:8080?", "dist" ]