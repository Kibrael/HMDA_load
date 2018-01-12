
drop table if exists hmda.lar_2016;
create table hmda.lar_2016
(  year integer,
    rid varchar,
    agency integer,
    loan_type varchar,
    loan_purpose varchar,
    occupancy varchar,
    loan_amount varchar,
    action_type varchar,
    msa varchar,
    state_code varchar,
    county_code varchar,
    census_tract varchar,
    app_sex varchar,
    co_app_sex varchar,
    income varchar,
    purchaser_type varchar,
    denial_1 varchar,
    denial_2 varchar,
    denial_3 varchar,
    edit_status varchar,
    property_type varchar,
    preapproval varchar,
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
    rate_spread varchar,
    hoepa varchar,
    lien_status varchar,
    sequence_num varchar
)

WITH (
  OIDS=TRUE
);
ALTER TABLE hmda.platform_panel
  OWNER TO roellk;

  copy hmda.platform_panel
    from '/Users/roellk/Desktop/HMDA/hmda_data_public/'
    delimiter ',' csv;
    