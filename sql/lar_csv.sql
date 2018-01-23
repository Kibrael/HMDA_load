
drop table if exists public.{table};
create table public.{table}
(  year varchar,
    rid varchar,
    agency varchar,
    loan_type varchar,
    property_type varchar,
    loan_purpose varchar,
    occupancy varchar,
    loan_amount varchar,
    preapproval varchar,
    action_type varchar,
    msa varchar,
    state_code varchar,
    county_code varchar,
    census_tract varchar,
    app_ethnicity varchar,
    co_app_ethnicity varchar,
    app_race_1 varchar,
    app_race_2 varchar,
    app_race_3 varchar,
    app_race_4 varchar,
    app_race_5 varchar,
    co_app_race_1 varchar,
    co_app_race_2 varchar,
    co_app_race_3 varchar,
    co_app_race_4 varchar,
    co_app_race_5 varchar,
    app_sex varchar,
    co_app_sex varchar,
    income varchar,
    purchaser_type varchar,
    denial_1 varchar,
    denial_2 varchar,
    denial_3 varchar,
    rate_spread varchar,
    hoepa varchar,
    lien_status varchar,
    edit_status varchar,
    sequence_num varchar,
    population varchar,
    min_pop_pct varchar,
    ffiec_mfi varchar,
    tract_to_msa_mfi_pct varchar,
    count_owner_occ_units varchar,
    count_1_4_fam_units varchar,
    app_date_indicator varchar
)

WITH (
  OIDS=TRUE
);commit;
ALTER TABLE public.{table}
  OWNER TO roellk;

  copy public.{table}
    from '{data_file}'
    DELIMITER ',' ENCODING 'latin1';