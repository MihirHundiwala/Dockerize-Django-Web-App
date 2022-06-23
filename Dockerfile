FROM python:3.9-buster

RUN apt-get update
RUN apt-get install nginx vim -y --no-install-recommends

COPY nginx.default /etc/nginx/sites-available/default

RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/src

COPY requirements.txt start-server.sh /opt/app/
COPY src /opt/app/src/

RUN ls -r

WORKDIR /opt/app

RUN pip install -r requirements.txt

RUN chmod +x start-server.sh
RUN chown -R www-data:www-data /opt/app

RUN ls -r

WORKDIR /opt/app/src
RUN ls -r

#start server
EXPOSE 8020
STOPSIGNAL SIGTERM
CMD ["/opt/app/start-server.sh"]