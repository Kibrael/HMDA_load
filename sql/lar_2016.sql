
drop table if exists hmda.lar_2016;
create table hmda.lar_2016
(  year integer,
    rid varchar,
    agency integer,
    loan_type integer,
    property_type varchar,
    loan_purpose integer,
    occupancy integer,
    loan_amount integer,
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
    app_sex integer,
    co_app_sex integer,
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
    app_date_indicator integer
)

WITH (
  OIDS=TRUE
);commit;
ALTER TABLE hmda.lar_2016
  OWNER TO roellk;

  copy hmda.lar_2016
    from '/Users/roellk/Desktop/HMDA/hmda_data_public/lar/2016HMDALAR-National.csv'
    DELIMITER ',';