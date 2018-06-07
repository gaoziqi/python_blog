FROM postgres:10.1
WORKDIR /var/lib/postgresql/data


RUN echo "wal_level = hot_standby
max_wal_senders = 1    #有几个备库就设置为几
wal_keep_segments = 256    #设置一个足够大的值，以防主库生成WAL日志太快，日志还没有来得及传送到standby，就会循环覆盖
hot_standby = on
logging_collector = on
log_directory = 'pg_log'
log_filename = 'postgresql-%Y-%m-%d_%H%M%S.log'" >> postgresql.conf && \
echo "host    replication     replica     slave1/32                 md5
host    replication     replica     slave2/32                 md5" >> pg_hba.conf && \


WORKDIR /

CMD ["docker-entrypoint.sh", "postgres"]