# syntax=docker/dockerfile:1
FROM nginx:latest
ADD dist /user/share/nginx/html/
CMD ["nginx", "-g", "daemon off;"]