DROP TABLE IF EXISTS public.{table};
CREATE TABLE public.{table} (
as_of_date varchar,
resp_id varchar,
agency varchar,
id_tax varchar,
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
resp_name_panel varchar,
resp_city_panel varchar,
resp_state_panel varchar,
assets_panel varchar,
olc_panel varchar,
region_code_panel varchar,
lar_count varchar,
edit_status varchar

)
WITH (
  OIDS=TRUE
);
ALTER TABLE {table}
  OWNER TO postgres; COMMIT;

COPY public.{table}
    from '{data_file}'
    DELIMITER E'\t' ENCODING 'latin1';