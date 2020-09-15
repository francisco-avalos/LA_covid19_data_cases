This repository web scrapes point of interest (POI) cases data from the Los Angeles Public Health website - http://publichealth.lacounty.gov/media/Coronavirus/locations.htm

This is a great way for individuals to obtain and study Covid-19 cases data at the POI level across the Los Angeles County. This is also helpful since the website currently has no built in API. 

Specifically, it pulls cases by POI in the following 4 sections:
* Residential Congregate and Acute Care Settings
* Los Angeles County Non-Residential Settings
* Los Angeles County Homeless Service Settings
* Los Angeles County Educational Settings

Two files for each section is exported into csv files: (1) as the 'as-seen' format and (2) as 'as-seen' with the addition of the address parsed out into street, city, state, and zip-code

Installation requirements for Python files:  use 'pip install -r requirements.txt'
