DROP TABLE IF EXISTS {table};
CREATE TABLE {table} (
	resp_id varchar,
	msa varchar,
	agency varchar,
	agency_group_code varchar,
	resp_name varchar,
	resp_city varchar,
	resp_state varchar,
	resp_state_fips varchar,
	assets varchar,
	olc varchar,
	parent_id varchar,
	parent_name varchar,
	parent_city varchar,
	parent_state varchar,
	as_of_year varchar,
	resp_rssd varchar)


WITH (
  OIDS=TRUE
);
ALTER TABLE {table}
  OWNER TO postgres; COMMIT;

  CREATE TEMPORARY TABLE panel_load
  (PANEL varchar); -- LAR contains an entire LAR record

  COPY panel_load
    FROM '{data_file}' ENCODING 'latin1';;
    COMMIT;

INSERT INTO {table} (
resp_id,
msa,
agency,
agency_group_code,
resp_name,
resp_city,
resp_state,
resp_state_fips,
assets,
olc,
parent_id,
parent_name,
parent_city,
parent_state,
as_of_year,
resp_rssd)

SELECT 
SUBSTRING(PANEL, 1, 10),
SUBSTRING(PANEL, 11, 5),
SUBSTRING(PANEL, 16, 1),
SUBSTRING(PANEL, 17, 2),
SUBSTRING(PANEL, 19, 30),
SUBSTRING(PANEL, 49, 25),
SUBSTRING(PANEL, 74, 2),
SUBSTRING(PANEL, 76, 2),
SUBSTRING(PANEL, 78, 10),
SUBSTRING(PANEL, 88, 1),
SUBSTRING(PANEL, 89, 10),
SUBSTRING(PANEL, 99, 30),
SUBSTRING(PANEL, 129, 25),
SUBSTRING(PANEL, 154, 2),
SUBSTRING(PANEL, 156, 4),
SUBSTRING(PANEL, 160, 10)
FROM panel_load
;COMMIT;
DROP TABLE IF EXISTS panel_load; COMMIT;

