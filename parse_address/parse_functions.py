
import pandas as pd
import re



def suites_and_bldgs_in_address(address):
    """
    Fucntion checks to see if the address contains a Suite or Building #
    Input: list
    Output: True/False
    """
    trigger = False

    for i in address.str.split(','):
        if(re.search('^Ste.|^ Ste.|^Bldg.|^ Bldg.|^Suite.|^ Suite.|^#2.|#^ #2.|^#A$|^# A$|^ #A$|^ # A$|^E$|^ E$|^ #420$', i[1])):
        # if(re.search('^ Ste.|^ Bldg.', i[1])):
        # if(len(i)==5):
            trigger = True
            break
    return trigger


def parse_address(DF, address):
    """
    Function splits an address in the dataframe into street, city, state, and zip code as separate columns.
    It uses the suites_and_bldgs_in_address function to account for suites and buildings in the address parser.
    Input: dataframe, address list
    Output: dataframe
    """
    streets = []

    if suites_and_bldgs_in_address(address):
        for i in address.str.split(','):
            if(len(i)==5):
                streets.append([i[0], i[2], i[3], i[4]])
            if(len(i)==4):
                streets.append(i)
            if(len(i)==2):
                streets.append(i)

    if not suites_and_bldgs_in_address(address):
        for i in address.str.split(','):
            streets.append(i)

    streets = pd.DataFrame(streets)

    DF = pd.concat([DF, streets], axis=1)

    return DF