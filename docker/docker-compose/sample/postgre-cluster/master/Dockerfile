FROM postgres:10.4-apline
WORKDIR /
ENV POSTGRES_PASSWORD postgres
ENV POSTGRES_USER postgres
COPY ./docker-entrypoint-initdb.d /

ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 5432
CMD ["postgres"]