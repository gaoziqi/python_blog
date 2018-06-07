FROM postgres:10.4-alpine
WORKDIR /
ENV POSTGRES_PASSWORD postgres
ENV POSTGRES_USER postgres
COPY docker-entrypoint-initdb.d /docker-entrypoint-initdb.d 

ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 5432
CMD ["postgres"]