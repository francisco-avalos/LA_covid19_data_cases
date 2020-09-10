
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
        if ((entry_list[i]=='\n') & (entry_list[i+1]=='Total')):
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




