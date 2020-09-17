## Outline
This repository web scrapes point of interest (POI) cases data from the [Los Angeles Public Health website](http://publichealth.lacounty.gov/media/Coronavirus/locations.htm)

## Uses 
This is a great way for individuals to obtain and study Covid-19 cases data at the POI level across the Los Angeles County. This is also helpful since the website currently has no built in API. 

Specifically, it pulls cases by POI in the following 4 sections:
* Residential Congregate and Acute Care Settings
* Los Angeles County Non-Residential Settings
* Los Angeles County Homeless Service Settings
* Los Angeles County Educational Settings

## Instructions
* Install module requirements for Python files using 'pip install -r requirements.txt'. 
* Run the main.py file

## Output
Two files for each section is exported into csv files. The first file is exactly the same as the website and the second also includes the address parsed out into street, city, state, and zip-code. 

***For location purposes, the Residential Congregate Settings file also has a third file that adds zip code to the POI. Zip codes here were web scraped and matched using the [LA Almanac](http://www.laalmanac.com/communications/cm02_communities.php)**

—

