# Aurora PostgreSQL Operations

SELECT version();
SELECT now();
SELECT current_database();
SELECT current_user;

SELECT * FROM pg_stat_activity LIMIT 50;
SELECT * FROM pg_stat_replication;
SELECT * FROM pg_replication_slots;

SELECT datname,count(*) FROM pg_stat_activity GROUP BY datname;

SELECT pid,usename,now()-xact_start age,query
FROM pg_stat_activity
WHERE xact_start IS NOT NULL
ORDER BY age DESC;

SELECT schemaname,relname,
pg_size_pretty(pg_total_relation_size(relid))
FROM pg_statio_user_tables
ORDER BY pg_total_relation_size(relid) DESC
LIMIT 50;

SELECT query,calls,total_exec_time
FROM pg_stat_statements
ORDER BY total_exec_time DESC
LIMIT 20;

SELECT relname,last_vacuum,last_autovacuum
FROM pg_stat_user_tables;

SELECT relname,n_live_tup,n_dead_tup
FROM pg_stat_user_tables
ORDER BY n_dead_tup DESC;

SELECT * FROM pg_stat_bgwriter;

SELECT pg_current_wal_lsn();

SELECT pid,wait_event_type,wait_event
FROM pg_stat_activity
WHERE wait_event IS NOT NULL;
