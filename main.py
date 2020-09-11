import re
import requests
from bs4 import BeautifulSoup


from functions.web_scrape import convert_scrapped_data_to_dataframe
from functions.la_cases import return_cases, return_cases_NonResidential, rcac_df, hss_df, es_df, nr_df
from functions.web_scrape import rcac_section, LAC_NR_section, lac_hss_section, lac_es_section






rcac_string, No_columns = rcac_section()
cases = return_cases(rcac_string)

RCAC_DF = convert_scrapped_data_to_dataframe(cases, data_length=No_columns)
RCAC_DF = rcac_df(RCAC_DF)

RCAC_DF.to_csv(r'~/Desktop/Residual_Congregate_and_Acute_Care_Settings.csv', index=False)


lac_hss_string, No_columns = lac_hss_section()
cases = return_cases(lac_hss_string)
HSS_DF = convert_scrapped_data_to_dataframe(cases, data_length=No_columns)
HSS_DF = hss_df(HSS_DF)

HSS_DF.to_csv(r'~/Desktop/LA_County_Homeless_Service_Settings.csv', index=False)


lac_es_string, No_columns = lac_es_section()
cases = return_cases(lac_es_string)
ES_DF = convert_scrapped_data_to_dataframe(cases, data_length=No_columns)
ES_DF = es_df(ES_DF)

ES_DF.to_csv(r'~/Desktop/LA_County_Educational_Settings.csv', index=False)



p1, p2, p3, No_columns = LAC_NR_section()
cases  = return_cases_NonResidential(p1, p2, p3)
NR_DF = convert_scrapped_data_to_dataframe(cases, data_length=No_columns)
NR_DF = nr_df(NR_DF)

NR_DF.to_csv(r'~/Desktop/LA_County_Non-Residential_Settings.csv', index=False)


# LAC_NR_DF = convert_scrapped_data_to_dataframe(cases, data_length=No_columns)

# LAC_NR_DF.columns=['location_name', 'address', 'total_confirmed_staff', 'total_non_confirmed_symptomatic_staff']
# LAC_NR_DF['total_confirmed_staff'] = LAC_NR_DF['total_confirmed_staff'].astype(int)
# LAC_NR_DF['total_non_confirmed_symptomatic_staff'] = LAC_NR_DF['total_non_confirmed_symptomatic_staff'].astype(int)


# LAC_NR_DF.to_csv(r'/Users/franciscoavalosjr/Desktop/LA_County_Non-Residential_Settings.csv', index=False)









