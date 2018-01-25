
drop table if exists public.{table};
create table public.{table}
(  year varchar,
    rid varchar,
    agency varchar,
    loan_type varchar,
    property_type varchar,
    purpose varchar,
    occupancy varchar,
    amount varchar,
    preapproval varchar,
    action varchar,
    msa varchar,
    state varchar,
    county varchar,
    tract varchar,
    app_eth varchar,
    co_eth varchar,
    race_1 varchar,
    race_2 varchar,
    race_3 varchar,
    race_4 varchar,
    race_5 varchar,
    co_race_1 varchar,
    co_race_2 varchar,
    co_race_3 varchar,
    co_race_4 varchar,
    co_race_5 varchar,
    app_sex varchar,
    co_app_sex varchar,
    income varchar,
    purchaser varchar,
    denial_1 varchar,
    denial_2 varchar,
    denial_3 varchar,
    rate_spread varchar,
    hoepa varchar,
    lien varchar,
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
  OWNER TO postgres;

  copy public.{table}
    from '{data_file}'
    DELIMITER ',' ENCODING 'latin1';