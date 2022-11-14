# syntax=docker/dockerfile:1
FROM mysql:8.0.21
MAINTAINER delphi
ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=delphi

ADD ./init/dump.sql /docker-entrypoint-initdb.d/
