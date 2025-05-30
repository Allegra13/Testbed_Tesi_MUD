FROM debian:bullseye

RUN apt-get update && apt-get install -y \
    apache2 \
    curl \
    iputils-ping \
    iproute2 \
    && apt-get clean

# Copia i file MUD nella directory pubblica del server HTTP
COPY /osmud/mudfiles/ /var/www/html/mudfiles/
COPY /osmud/start.sh /start.sh

RUN chmod +x /start.sh

EXPOSE 80

CMD ["/start.sh"]
