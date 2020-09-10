import re
import requests
from bs4 import BeautifulSoup


from functions.web_scrape import convert_scrapped_data_to_dataframe
from functions.la_cases import return_cases
from functions.web_scrape import rcac_section, LAC_NR_section






rcac_string, No_columns = rcac_section()
cases = return_cases(rcac_string)
# p1, p2, p3, No_columns = LAC_NR_section()



# LAC_NR_DF = convert_scrapped_data_to_dataframe(cases, data_length=No_columns)

# LAC_NR_DF.columns=['location_name', 'address', 'total_confirmed_staff', 'total_non_confirmed_symptomatic_staff']
# LAC_NR_DF['total_confirmed_staff'] = LAC_NR_DF['total_confirmed_staff'].astype(int)
# LAC_NR_DF['total_non_confirmed_symptomatic_staff'] = LAC_NR_DF['total_non_confirmed_symptomatic_staff'].astype(int)


# LAC_NR_DF.to_csv(r'/Users/franciscoavalosjr/Desktop/LA_County_Non-Residential_Settings.csv', index=False)


RESID_AND_ACUTE_DF = convert_scrapped_data_to_dataframe(cases, data_length=No_columns)

RESID_AND_ACUTE_DF.columns=['location_name', 'city_name', 'number_of_confirmed_staff', 'number_of_confirmed_residents', 
                  'total_deaths']
RESID_AND_ACUTE_DF['number_of_confirmed_staff'] = RESID_AND_ACUTE_DF['number_of_confirmed_staff'].astype(int)
RESID_AND_ACUTE_DF['number_of_confirmed_residents'] = RESID_AND_ACUTE_DF['number_of_confirmed_residents'].astype(int)
RESID_AND_ACUTE_DF['total_deaths'] = RESID_AND_ACUTE_DF['total_deaths'].astype(int)



RESID_AND_ACUTE_DF.to_csv(r'/Users/franciscoavalosjr/Desktop/Residual_Congregate_and_Acute_Care_Settings.csv', index=False)






