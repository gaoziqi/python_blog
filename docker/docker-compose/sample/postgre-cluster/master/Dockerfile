FROM postgres:10.1
WORKDIR /
ENV POSTGRES_PASSWORD postgres
ENV POSTGRES_USER postgres

RUN docker-entrypoint.sh postgres

WORKDIR /var/lib/postgresql/data

RUN echo "wal_level = hot_standby\n\
max_wal_senders = 1    #有几个备库就设置为几\n\
wal_keep_segments = 256    #设置一个足够大的值，以防主库生成WAL日志太快，日志还没有来得及传送到standby，就会循环覆盖\n\
hot_standby = on\n\
logging_collector = on\n\
log_directory = 'pg_log'\n\
log_filename = 'postgresql-%Y-%m-%d_%H%M%S.log'" >> postgresql.conf && \
echo "host    replication     replica     slave1/32                 md5\n\
host    replication     replica     slave2/32                 md5" >> pg_hba.conf && \


CMD ["pg_ctl", "restart"]