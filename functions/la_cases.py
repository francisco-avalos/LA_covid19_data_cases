

import requests
from bs4 import BeautifulSoup


from functions.web_scrape import search_start_end, remove_tabs_and_obs



url = 'http://publichealth.lacounty.gov/media/Coronavirus/locations.htm'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')




def return_cases(search_string) -> list:
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
		if(soup_strings[i] in search_string):
			
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




