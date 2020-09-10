import re
import requests
from bs4 import BeautifulSoup


from functions.web_scrape import search_start_end, remove_tabs_and_obs, convert_scrapped_data_to_dataframe




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


## testing trial
RCAC_string = 'Residential Congregate and Acute Care Settings Meeting the Criteria of (1) At Least One Laboratory-confirmed Resident or (2) Two or More Laboratory-confirmed Staff in Long-Term Care Facilities that are not Skilled Nursing Facilities, or (3) Three or More Laboratory-Confirmed Staff in Shared Housing'



while (i <= maxi): 
    if(soup_strings[i]==RCAC_string):
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


RESID_AND_ACUTE_DF = convert_scrapped_data_to_dataframe(cases, data_length=5)


RESID_AND_ACUTE_DF.columns=['location_name', 'city_name', 'number_of_confirmed_staff', 'number_of_confirmed_residents', 
                  'total_deaths']
RESID_AND_ACUTE_DF['number_of_confirmed_staff'] = RESID_AND_ACUTE_DF['number_of_confirmed_staff'].astype(int)
RESID_AND_ACUTE_DF['number_of_confirmed_residents'] = RESID_AND_ACUTE_DF['number_of_confirmed_residents'].astype(int)
RESID_AND_ACUTE_DF['total_deaths'] = RESID_AND_ACUTE_DF['total_deaths'].astype(int)



RESID_AND_ACUTE_DF.to_csv(r'/Users/franciscoavalosjr/Desktop/section_data.csv', index=False)






