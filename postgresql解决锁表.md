# postgresql解决锁表
    --查询是否锁表了
    select oid from pg_class where relname='可能锁表了的表'
    select pid from pg_locks where relation='上面查出的oid'
    --如果查询到了结果，表示该表被锁 则需要释放锁定
    select pg_cancel_backend(上面查到的pid)