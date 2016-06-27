fields_12_14 = ('year', 'rid', 'agency', 'loan_type', 'property_type', 'loan_purpose', 'occupancy', 'preapproval', 'amount', 'action', 'msa', 'state', 'county',
    'tract', 'ethnicity', 'co_ethnicity', 'race1', 'race2', 'race3', 'race4', 'race5', 'co_race1', 'co_race2', 'co_race3', 'co_race4', 'co_race5',
    'sex', 'co_sex', 'income', 'purchaser', 'denial1', 'denial2', 'denial3', 'rate_spread', 'hoepa', 'lien', 'edit_status', 'sequence', 'population',
    'min_population_pct', 'median_income', 'tract_to_msa_income_pct', 'num_owner_occ_units', 'num_single_fam_units', 'app_date_ind')

values =('2013', '0000000151', '5', '1', '2', '1', '3', '4', '11260', '02', '020', '0028.12', '1', '5', '0124', '0', ' ', ' ', ' ', '6', '1', '00070', '3', '5', '6', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', 'NA   ', '2', '3', '0001165');
fields_04_11 = ('year', 'rid', 'agency', 'loan_type', 'loan_purpose', 'occupancy', 'amount', 'action', 'msa', 'state', 'county',
    'tract', 'sex', 'co_sex', 'income', 'purchaser', 'denial1', 'denial2', 'denial3', 'edit_status', 'property_type', 'preapproval',
    'ethnicity', 'co_ethnicity', 'race1', 'race2', 'race3', 'race4', 'race5', 'co_race1', 'co_race2', 'co_race3', 'co_race4', 'co_race5',
    'rate_spread', 'hoepa', 'lien', 'sequence')
{
    "load_years": ["1990", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999",
            "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009",
            "2010", "2010", "2011", "2012", "2013", "2014"]
}
derp = ['As of Year',
'Respondent ID',
'Agency Code',
 'Loan Type',
 'Property Type',
 'Loan Purpose',
 'Occupancy',
 'Loan Amount (000s)',
 'Preapproval',
 'Action Type',
 'MSA/MD',
  'State Code',
  'County Code',
  'Census Tract Number',
  'Applicant Ethnicity',
  'Co Applicant Ethnicity',
  'Applicant Race 1',
  'Applicant Race 2',
  'Applicant Race 3',
  'Applicant Race 4',
  'Applicant Race 5',
  'Co Applicant Race 1',
  'Co Applicant Race 2',
  'Co Applicant Race 3',
  'Co Applicant Race 4',
  'Co Applicant Race 5',
  'Applicant Sex',
  'Co Applicant Sex',
  'Applicant Income (000s)',
  'Purchaser Type',
  'Denial Reason1',
'Denial Reason 2',
'Denial Reason 3',
'Rate Spread',
 'HOEPA Status',
 'Lien Status',
 'Edit Status',
'Sequence Number',
'Population',
'Minority Population %',
'FFIEC Median Family Income',
'Tract to MSA/MD Income %',
'Number of Owner-occupied units',
'Number of 1-to 4-Family units',
'Application Date Indicator']

print len(derp)


