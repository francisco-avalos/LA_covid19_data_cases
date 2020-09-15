import pandas as pd
import re



def suites_and_bldgs_in_address(address):
    """
    Fucntion checks to see if the address contains a Suite or Building #
    Input: list
    Output: True/False
    """
    for i in address.str.split(','):
        # if(re.search('^Ste.|^ Ste.|^Bldg.|^ Bldg.', i[1])):
        # if(re.search('^ Ste.|^ Bldg.', i[1])):
        if(len(i)==5):
            return True 
        return False


def parse_address(DF, address):
    """
    Function splits an address in the dataframe into street, city, state, and zip code as separate columns.
    It uses the suites_and_bldgs_in_address function to account for suites and buildings in the address parser.
    Input: dataframe, address list
    Output: dataframe
    """
    if suites_and_bldgs_in_address(address):
        streets1 = []
        streets2 = []

        for i in address.str.split(','):
            # if(re.search('^Ste.|^ Ste.|^Bldg.|^ Bldg.', i[1])):
            # if(re.search('^ Ste.|^ Bldg.', i[1])):
            if(len(i)==5):
                streets1.append([i[0], i[2], i[3], i[4]])
            else:
                streets2a.append(i)
        streets = streets1 + streets2

    if not suites_and_bldgs_in_address(address):
        streets = []

        for i in address.str.split(','):
            streets.append(i)

    streets = pd.DataFrame(streets)

    if(DF['empty']):
        del DF['empty']

    DF = pd.concat([DF, streets], axis=1)

    return DF