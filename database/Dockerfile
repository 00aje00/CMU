# syntax=docker/dockerfile:1
FROM mysql:8.0.21
MAINTAINER delphi

# definding appropriate variables to access MySQL
ENV MYSQL_ROOT_PASSWORD=root
#ENV MYSQL_DATABASE=delphi

# dumping our dump.sql database into MySQL
ADD ./init/dump.sql /docker-entrypoint-initdb.d/
