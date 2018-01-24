DROP TABLE IF EXISTS {table};
CREATE TABLE {table} (
	activity_year varchar,
	resp_id varchar,
	agency_code varchar,
	parent_resp_id varchar,
	parent_name varchar,
	filler varchar,
	parent_city varchar,
	parent_state varchar,
	region varchar,
	assets varchar,
	olc varchar,
	resp_name varchar,
	resp_city varchar,
	resp_state varchar,
	filler2 varchar,
	filler3 varchar,
	top_holder_rssd varchar,
	top_holder_name varchar,
	top_holder_city varchar,
	top_holder_state varchar,
	top_holder_country varchar,
	resp_rssd varchar,
	parent_rssd varchar,
	resp_state_fips varchar)

WITH (
  OIDS=TRUE
);
ALTER TABLE {table}
  OWNER TO roellk; COMMIT;

  CREATE TEMPORARY TABLE panel_load
  (PANEL varchar); -- LAR contains an entire LAR record

  COPY panel_load
    FROM '{data_file}' ENCODING 'latin1';;
    COMMIT;

INSERT INTO {table} (
	activity_year,
	resp_id,
	agency_code,
	parent_resp_id,
	parent_name,
	parent_city,
	parent_state,
	region,
	assets,
	olc,
	resp_name,
	filler,
	resp_city,
	resp_state,
	filler2,
	filler3,
	top_holder_rssd,
	top_holder_name,
	top_holder_city,
	top_holder_state,
	top_holder_country,
	resp_rssd,
	parent_rssd,
	resp_state_fips
)

SELECT 
SUBSTRING(PANEL, 1, 4),
SUBSTRING(PANEL, 5, 10),
SUBSTRING(PANEL, 15, 1),
SUBSTRING(PANEL, 16, 10),
SUBSTRING(PANEL, 26, 30),
SUBSTRING(PANEL, 56, 80),
SUBSTRING(PANEL, 81, 2),
SUBSTRING(PANEL, 83, 2),
SUBSTRING(PANEL, 85, 10),
SUBSTRING(PANEL, 95, 1),
SUBSTRING(PANEL, 96, 30),
SUBSTRING(PANEL, 126, 40),
SUBSTRING(PANEL, 166, 25),
SUBSTRING(PANEL, 191, 2),
SUBSTRING(PANEL, 193, 10),
SUBSTRING(PANEL, 203, 10),
SUBSTRING(PANEL, 213, 10),
SUBSTRING(PANEL, 223, 30),
SUBSTRING(PANEL, 253, 25),
SUBSTRING(PANEL, 278, 2),
SUBSTRING(PANEL, 280, 40),
SUBSTRING(PANEL, 320, 10),
SUBSTRING(PANEL, 330, 10),
SUBSTRING(PANEL, 340, 2)



FROM panel_load
;COMMIT;
DROP TABLE IF EXISTS panel_load; COMMIT;






















