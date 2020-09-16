
import requests
import re

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


def extract_communities_and_zipcodes():
    """
    Function web scrapes data from www.laalmanac.com and produces 2 lists - for communities and zip codes
    Input: None
    Ouput: 2 lists
    """
    url = 'http://www.laalmanac.com/communications/cm02_communities.php'
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    td_data = soup.find_all('td')

    # Extract comminity and zip code data
    communities = {}
    zipcodes = {}
    
    c = 1
    
    for index in range(len(td_data)):

        if (c % 2) != 0:
            community = td_data[index].text.strip()
            idx = int(index/2)
            communities[idx] = community
        
        if (c % 2) != 0:
            zip_code = td_data[index+1].text.strip()
            idx = int(index/2)
            zipcodes[idx] = zip_code
        
        c+=1

    return communities, zipcodes


def community_string_parser(communities, zipcodes):
    """
    Function cleans out and refines the string names of web sraped data
    Input: 2 lists 
    Output: 2 lists
    """
    communities_and_zips = []
    cities = []
    zips = []

    for i in zipcodes:
        communities_and_zips.append(communities[i] + '---' + zipcodes[i])

    for i in communities_and_zips:
        city = i.split('---')[0]

        item = re.sub(r"(^Los.Angeles.|\(Los Angeles\)|PO Boxes|\/.*)", "", city.strip())
    
        item = re.sub(r"(^Pasadena.*)", "Pasadena", item)
        item = re.sub(r"(^Alhambra.*)", "Alhambra", item)
        item = re.sub(r"(^Downtown.*)", "Downtown", item)
        item = re.sub(r"(.*Long Beach.*)", "Long Beach", item)
        item = re.sub(r"(Santa Clarita )", "", item)

        item = re.sub(r"(Rancho Dominguez.*)", "West Rancho Dominguez", item) # Officially 'West Rancho Dominguez'
        item = re.sub(r"(Los Angeles International Airport.*)", "Los Angeles", item) # ME: get's 'Los Angeles' 
        item = re.sub(r"(\(|\))", "", item.strip())
        item = re.sub(r" $","", item)

        cities.append(item)

        zipcode = i.split('---')[1]
        zips.append(zipcode)

    return cities, zips


def get_LA_cities_and_zipcodes_from_LAAlmanac():
    """
    Function webscrapes the cities and their zipcodes from www.laalmanac.com
    Input: None
    Ouutput: Dataframe 
    """
    communities, zipcodes = extract_communities_and_zipcodes()
    Community_DF, ZipCodes_DF = community_string_parser(communities, zipcodes)

    LA_DF = pd.Dataframe(columns=('city', 'postal_code'))
    Z1 = []
    
    for i in range(len(ZipCodes_DF)):
        Z1.append(ZipCodes_DF[i].split(', ')[0]) # going with the first zip code in each community
    
    LA_DF['city'] = Community_DF
    LA_DF['postal_code'] = Z1

    return LA_DF


def add_ZipCode(DF):
    """
    Function adds zip-codes to the given dataframe - intended for Residential Congregaste Settings
    Input: dataframe
    Output: Dataframe
    """
    la_community_df = get_LA_cities_and_zipcodes_from_LAAlmanac()

    DF = pd.merge(DF, la_community_df, on=['city'], how='left')

    return DF

