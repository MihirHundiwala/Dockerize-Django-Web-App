FROM python:3.9-buster

RUN apt-get update
RUN apt-get install nginx vim -y --no-install-recommends

COPY nginx.default /etc/nginx/sites-available/default

RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

RUN mkdir -p /django-app/src

COPY src /django-app/src
COPY requirements.txt start-server.sh /django-app/

WORKDIR /django-app

RUN pip install -r requirements.txt

RUN chown -R www-data:www-data /django-app/src

#start server
EXPOSE 8020
STOPSIGNAL SIGTERM
CMD ["ls -r"]