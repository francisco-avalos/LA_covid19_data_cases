

import requests
from bs4 import BeautifulSoup


from functions.web_scrape import search_start_end, remove_tabs_and_obs



url = 'http://publichealth.lacounty.gov/media/Coronavirus/locations.htm'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')




def return_cases(soup):
    soup_strings = []
    
    for string in soup.strings:
        soup_strings.append(string)

    maxi = len(soup_strings)
    i = 0
    data_extract = []
    la_cases = []

    while (i <= maxi): 
        if(soup_strings[i] in soup_strings):
            
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
                    la_cases.append(data_extract[i])
            break
        i+=1

    del data_extract, i, maxi, data_start, data_end, length

    la_cases = remove_tabs_and_obs(la_cases)

    return la_cases
