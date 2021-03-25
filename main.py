
import re
import requests
from bs4 import BeautifulSoup

from functions.web_scrape import convert_scrapped_data_to_dataframe
from functions.la_cases import return_cases, return_cases_NonResidential, rcac_df, hss_df, es_df, nr_df, return_cases_ResCong, return_cases_home
from functions.web_scrape import rcac_section, LAC_NR_section, lac_hss_section, lac_es_section

from parse_address.parse_functions import parse_address

from functions.la_cases import add_ZipCode




# Residential Congragate Settings

# r1, r2, r3, r4, r5, No_columns = rcac_section()
# cases = return_cases_ResCong(r1, r2, r3, r4, r5)

# RCAC_DF = convert_scrapped_data_to_dataframe(cases, data_length=No_columns)
# RCAC_DF = rcac_df(RCAC_DF)

# RCAC_DF.to_csv(r'~/Desktop/Residual_Congregate_and_Acute_Care_Settings.csv', index=False)


# RCAC_DF = parse_address(RCAC_DF, RCAC_DF['city_name'])
# RCAC_DF.columns = ['location_name','city_name','number_of_confirmed_staff','number_of_confirmed_residents','total_deaths','city',
#                 'state']

# RCAC_DF.to_csv(r'~/Desktop/Residual_Congregate_and_Acute_Care_Settings(Parsed).csv', index=False)

# RCAC_DF = add_ZipCode(RCAC_DF)

# RCAC_DF.to_csv(r'~/Desktop/Residual_Congregate_and_Acute_Care_Settings(Parsed_and_ZipCode).csv', index=False)


# Non-Residential Settings

# p1, p2, p3, p4, p5, p6, p7, No_columns = LAC_NR_section()
# cases  = return_cases_NonResidential(p1, p2, p3, p4, p5, p6, p7)
# NR_DF = convert_scrapped_data_to_dataframe(cases, data_length=No_columns)
# NR_DF = nr_df(NR_DF)

# NR_DF.to_csv(r'~/Desktop/LA_County_Non-Residential_Settings.csv', index=False)

# NR_DF = parse_address(NR_DF, NR_DF['address'])

# NR_DF.columns = ['location_name','address','total_confirmed_staff','total_confirmed_non_staff','street_address','city',
#                  'state','zipcode']
# # NR_DF.columns = ['location_name','address','total_confirmed_staff','street_address','city','state','zipcode']
# # NR_DF.columns = ['location_name','address','total_confirmed_staff','total_non_confirmed_symptomatic_staff','street_address','city',
# #                  'state','zipcode']

# NR_DF.to_csv(r'~/Desktop/LA_County_Non-Residential_Settings(Parsed).csv', index=False)



# # ## Homeless Service Settings

pat1, pat2, pat3, pat4, pat5, No_columns = lac_hss_section()
cases = return_cases_home(pat1, pat2, pat3, pat4, pat5)
# HSS_DF = convert_scrapped_data_to_dataframe(cases, data_length=No_columns)
# HSS_DF = hss_df(HSS_DF)

# HSS_DF.to_csv(r'~/Desktop/LA_County_Homeless_Service_Settings.csv', index=False)



# # Educational Settings

# lac_es_string, No_columns = lac_es_section()
# cases = return_cases(lac_es_string)
# ES_DF = convert_scrapped_data_to_dataframe(cases, data_length=No_columns)
# ES_DF = es_df(ES_DF)

# ES_DF.to_csv(r'~/Desktop/LA_County_Educational_Settings.csv', index=False)

# # print(ES_DF)
# ES_DF = parse_address(ES_DF, ES_DF['address'])
# # print(ES_DF.head(60))
# ES_DF.columns = ['location_name','address','total_confirmed_staff','total_confirmed_students','street_address','city','state',
#                  'zipcode']

# ES_DF.to_csv(r'~/Desktop/LA_County_Educational_Settings(Parsed).csv', index=False)

