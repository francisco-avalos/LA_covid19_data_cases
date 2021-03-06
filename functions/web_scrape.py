
import pandas as pd




def search_start_end(entry_list):
    """
    Function returns index of targetted web scrapped data
    Input: A list
    Output: Two index values marking the start and end of the targetted data
    """
    length = len(entry_list)
    start = end = 0
    i = 0
    while (i < length):
        if ((entry_list[i]=='\n') & (entry_list[i+1]=='1')):
            start = i+2
        if ((entry_list[i]=='\n') & ((entry_list[i+1]=='Total') | (entry_list[i+1]=='Totals'))):
            end = i-1
        if ((start != 0) & (end != 0)):
            break
        i+=1
    return start,end



def remove_tabs_and_obs(entry_list) -> list:
    """
    Function removes tabs (\n) and numerical index (Obs) from scraped data
    Input: A list
    Output: A list
    """
    delete_ints = []
    
    for i in range(len(entry_list)):
#         if(entry_list[i]=='\n'): # had web formattitng inconsistencies 
        if((entry_list[i]=='\n') | (entry_list[i]=='\r\n"') | (entry_list[i]=='"\r\n')):
            if(entry_list[i+1]):
                delete_ints.append(i)
                delete_ints.append(i)
    iterations = len(delete_ints)-1
    while(iterations != -1):
        del entry_list[delete_ints[iterations]]
        iterations-=1
    return entry_list






def convert_scrapped_data_to_dataframe(entry_list, data_length):
    """
    Function converts the scrapped data into a dataframe
    Input: A list and integer 
    Output: A dataframe
    """
    new_cases = []
    
    for i in range(0, len(entry_list), data_length):
        new_cases.append(entry_list[i:i+data_length])
    
    df = pd.DataFrame(new_cases)
    
    return df



def rcac_section():
    """
    Function returns string to search for in the 'Residential Congregate and Acute
    Care Settings' section of the LA Public Care setting and the number of columns to look for 
    Input: None
    Output: a string and integer
    """
    # RCAC_string = 'Residential Congregate and Acute Care Settings Meeting the Criteria of (1) At Least One Laboratory-confirmed Resident or (2) Two or More Laboratory-confirmed Staff in Long-Term Care Facilities that are not Skilled Nursing Facilities, or (3) Three or More Laboratory-Confirmed Staff in Shared Housing'
    rcac_string1 = 'Active Outbreaks at Residential Congregate and Acute Care Settings with (1) At Least One '
    rcac_string2 = 'Laboratory-Confirmed'
    rcac_string3 = ' Resident, or (2) Two or More Laboratory-Confirmed Staff in Long-Term Care Facilities that are not Skilled Nursing Facilities, or (3) Three or More '
    rcac_string4 = 'Laboratory-Confirmed'
    rcac_string5 = ' Staff in Shared Housing'
    column_size = 5

    # return RCAC_string, column_size
    return rcac_string1, rcac_string2, rcac_string3, rcac_string4, rcac_string5, column_size

def LAC_NR_section():
    """
    Function returns string to search for in the 'Los Angeles County Non-Residential Settings' section of the LA Public Care Setting
    and the number of columns to look for
    ** Note: Due to the spacing in this section's web design, 3 pattern match strings are needed to confirm**

    Input: None
    Output: a stringa and integer
    """
    # pattern_1 = 'Los Angeles County '
    # pattern_2 = 'Non-Residential'
    # pattern_3 = ' Settings Meeting the Criteria of Three or More '
    pat1 = 'Active Outbreaks at '
    pat2 = 'Non-Residential'
    pat3 = ' Settings with Three or More '
    pat4 = 'Laboratory-Confirmed'
    pat5 = ' '
    pat6 = 'COVID-19'
    pat7 = ' Cases'
    column_size = 4

    return pat1, pat2, pat3, pat4, pat5, pat6, pat7, column_size


def lac_hss_section():
    """
    Function returns string to search for in the 'Los Angeles County Homeless Service Settings' and the number of columns to look for
    Input: None
    Output: a string and integer
    """
    # HSS_string = 'Los Angeles County Homeless Service Settings Meeting the Criteria of At Least One '
    pat1 = 'Active Outbreaks at Homeless Service Settings with at Least One '
    pat2 = 'Laboratory-Confirmed'
    pat3 = ' '
    pat4 = 'COVID-19'
    pat5 = ' Case'
    column_size = 5

    return pat1, pat2, pat3, pat4, pat5, column_size

def lac_es_section():
    """
    Function returns string to search for in the 'Los Angeles County Educational Settings' and the number of columns to look for
    Input: None
    Output: a string and integer
    """
    # education_string = 'Los Angeles County Educational Settings Meeting the Criteria of Three or More '
    pat1 = 'Active Outbreaks at Educational Settings with Three or More '
    pat2 = 'Laboratory-Confirmed'
    pat3 = ' COVID-19 Cases'
    column_size = 4

    return pat1, pat2, pat3, column_size





