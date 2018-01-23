DROP TABLE IF EXISTS {table};
CREATE TABLE {table} (
as_of_date varchar,
agency_code varchar,
resp_id varchar,
resp_name varchar,
resp_address varchar,
resp_city varchar,
resp_state varchar,
resp_zip varchar,
parent_name varchar,
parent_address varchar,
parent_city varchar,
parent_state varchar,
parent_zip varchar,
edit_status varchar,
id_tax varchar)

WITH (
  OIDS=TRUE
);
ALTER TABLE {table}
  OWNER TO roellk; COMMIT;

  CREATE TEMPORARY TABLE ts_load 
  (TS varchar) ; -- TS contains an entire TS record per row

  COPY ts_load 
    FROM '{data_file}' ENCODING 'latin1';
    COMMIT;

INSERT INTO {table} (
as_of_date,
agency_code,
resp_id,
resp_name,
resp_address,
resp_city,
resp_state,
resp_zip,
parent_name,
parent_address,
parent_city,
parent_state,
parent_zip,
edit_status,
id_tax)

SELECT 
SUBSTRING(TS, 1, 4),
SUBSTRING(TS, 5, 1),
SUBSTRING(TS, 6, 10),
SUBSTRING(TS, 16, 30),
SUBSTRING(TS, 46, 40),
SUBSTRING(TS, 86,25),
SUBSTRING(TS, 111,2),
SUBSTRING(TS, 113, 10),
SUBSTRING(TS, 123, 30),
SUBSTRING(TS, 153, 40),
SUBSTRING(TS, 193, 25),
SUBSTRING(TS, 218, 2),
SUBSTRING(TS, 220, 10),
SUBSTRING(TS, 230, 1),
SUBSTRING(TS, 231, 10)


FROM ts_load
;COMMIT;
DROP TABLE IF EXISTS ts_load; COMMIT;