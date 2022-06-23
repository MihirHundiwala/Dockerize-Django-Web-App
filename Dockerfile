FROM python:3.9-buster

RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default

RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

RUN mkdir -p /home/app
RUN mkdir -p /home/app/src

COPY requirements.txt start-server.sh /home/app/
COPY src /home/app/src/

WORKDIR /home/app

RUN pip install -r requirements.txt
RUN chown -R www-data:www-data /home/app

# start server
EXPOSE 8020
STOPSIGNAL SIGTERM
CMD ["./home/app/start-server.sh"]