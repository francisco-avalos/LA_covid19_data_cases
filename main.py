import re
import requests
from bs4 import BeautifulSoup


from functions.web_scrape import search_start_end, remove_tabs_and_obs, convert_scrapped_data_to_dataframe
from functions.web_scrape import rcac_section, LAC_NR_section




url = 'http://publichealth.lacounty.gov/media/Coronavirus/locations.htm'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')


soup_strings = []

for string in soup.strings:
    soup_strings.append(string)



maxi = len(soup_strings)
i = 0
data_extract = []
cases = []


# rcac_string, No_columns = rcac_section()
p1, p2, p3, No_columns = LAC_NR_section()

while (i <= maxi): 
    # if(soup_strings[i] in rcac_string):
    if((soup_strings[i] in p1) & (soup_strings[i+1] in p2) & (soup_strings[i+2] in p3)):
        length = len(soup_strings[i:])
        start = len(soup_strings) - length
        end = start + length
        stop = 'Total'
        placeholder=str()
        while ((start <= end) & (placeholder != stop)):
            placeholder = soup_strings[start]
            data_extract.append(soup_strings[start])
            start+=1
        
        data_start,data_end = search_start_end(data_extract)
        
        for i in range(len(data_extract)):
            if ((i >= data_start) & (i <= data_end)):
                cases.append(data_extract[i])
        break
    i+=1

del data_extract, i, maxi, data_start, data_end, length

cases = remove_tabs_and_obs(cases)


LAC_NR_DF = convert_scrapped_data_to_dataframe(cases, data_length=No_columns)

LAC_NR_DF.columns=['location_name', 'address', 'total_confirmed_staff', 'total_non_confirmed_symptomatic_staff']
LAC_NR_DF['total_confirmed_staff'] = LAC_NR_DF['total_confirmed_staff'].astype(int)
LAC_NR_DF['total_non_confirmed_symptomatic_staff'] = LAC_NR_DF['total_non_confirmed_symptomatic_staff'].astype(int)


LAC_NR_DF.to_csv(r'/Users/franciscoavalosjr/Desktop/LA_County_Non-Residential_Settings.csv', index=False)


# RESID_AND_ACUTE_DF = convert_scrapped_data_to_dataframe(cases, data_length=No_columns)


# RESID_AND_ACUTE_DF.columns=['location_name', 'city_name', 'number_of_confirmed_staff', 'number_of_confirmed_residents', 
#                   'total_deaths']
# RESID_AND_ACUTE_DF['number_of_confirmed_staff'] = RESID_AND_ACUTE_DF['number_of_confirmed_staff'].astype(int)
# RESID_AND_ACUTE_DF['number_of_confirmed_residents'] = RESID_AND_ACUTE_DF['number_of_confirmed_residents'].astype(int)
# RESID_AND_ACUTE_DF['total_deaths'] = RESID_AND_ACUTE_DF['total_deaths'].astype(int)



# RESID_AND_ACUTE_DF.to_csv(r'/Users/franciscoavalosjr/Desktop/Residual_Congregate_and_Acute_Care_Settings.csv', index=False)






