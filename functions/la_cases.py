

import requests
from bs4 import BeautifulSoup


from functions.web_scrape import search_start_end, remove_tabs_and_obs



url = 'http://publichealth.lacounty.gov/media/Coronavirus/locations.htm'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')




def return_cases(search_input):
    """
    Function scans the LA Public Health Care website and returns a list of the targetted data information
    Input: string variable
    Output: list
    """

    soup_strings = []
    for string in soup.strings:
        soup_strings.append(string)

    maxi = len(soup_strings)
    i = 0
    data_extract = []
    la_cases = []

    while (i <= maxi):
        if(soup_strings[i] == str(search_input)):
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

def return_cases_NonResidential(pattern1, pattern2, pattern3):
    """
    Function scans the LA Public Health Care website and returns a list of the targetted data information. It's
    particularly designed to capture the Non-Residential data since the title web-page is designed with several indentions
    Input: string variable
    Output: list
    """

    soup_strings = []
    for string in soup.strings:
        soup_strings.append(string)

    maxi = len(soup_strings)
    i = 0
    data_extract = []
    la_cases = []

    while (i <= maxi):
        if((soup_strings[i] == str(pattern1)) & (soup_strings[i+1] == str(pattern2)) & (soup_strings[i+2] == str(pattern3))):
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


def rcac_df(DF):
    """
    Function cleans up the column types for the Residential Congregate & Acute Care Settings dataframe
    Input: dataframe
    Output: dataframe
    """
    DF.columns = ['location_name', 'city_name', 'number_of_confirmed_staff', 'number_of_confirmed_residents', 
                  'total_deaths']
    DF['number_of_confirmed_staff'] = DF['number_of_confirmed_staff'].astype(int)
    DF['number_of_confirmed_residents'] = DF['number_of_confirmed_residents'].astype(int)
    DF['total_deaths'] = DF['total_deaths'].astype(int)

    return DF

def hss_df(DF):
    """
    Function cleans up the column types for the LA county Homeless Service Settings dataframe 
    Input: dataframe 
    Output: dataframe
    """
    DF.columns=['location_name', 'setting_type', 'number_of_confirmed_staff', 
                                         'number_of_confirmed_non_staff', 'total_deaths']
    DF['number_of_confirmed_staff'] = DF['number_of_confirmed_staff'].astype(int)
    DF['number_of_confirmed_non_staff'] = DF['number_of_confirmed_non_staff'].astype(int)
    DF['total_deaths'] = DF['total_deaths'].astype(int)

    return DF

def es_df(DF):
    """
    Function cleans up the column types for the LA county educational settings dataframe
    Input: dataframe
    Output: dataframe
    """
    DF.columns=['location_name','address','total_confirmed_staff','total_confirmed_students']
    DF['total_confirmed_staff'] = DF['total_confirmed_staff'].astype(int)
    DF['total_confirmed_students'] = DF['total_confirmed_students'].astype(int)

    return DF

def nr_df(DF):
    """
    Function cleans up the column types for the LA county Non-Residential settings dataframe
    Input: dataframe
    Output: dataframe
    """
    DF.columns=['location_name', 'address', 'total_confirmed_staff', 'total_non_confirmed_symptomatic_staff']
    DF['total_confirmed_staff'] = DF['total_confirmed_staff'].astype(int)
    DF['total_non_confirmed_symptomatic_staff'] = DF['total_non_confirmed_symptomatic_staff'].astype(int)

    return DF
