import pandas as pd
import re



def suites_and_bldgs_in_address(address):
	"""
	Fucntion checks to see if the address contains a Suite or Building #
	Input: list
	Output: True/False
	"""
	for i in addresses.str.split(','):
        if(re.search('^Ste.|^ Ste.|^Bldg.|^ Bldg.', i[1])):
            return True 
        return False


def parse_address(DF, address):
	"""
	Function splits addresses 
	"""
	if suites_and_bldgs_in_address(address):
		streets1 = []
		streets2 = []

		for i in address.str.split(','):
            if(re.search('^Ste.|^ Ste.|^Bldg.|^ Bldg.', i[1])):
            	streets1.append([i[0], i[2], i[3], i[4]])
            else:
            	streets2a.append(i)
        streets = streets1 + streets2

    if !(suites_and_bldgs_in_address(address)):
        streets = []

        for i in address.str.split(','):
            streets.append(i)

	streets = pd.DataFrame(streets)

	DF = pd.concat([DF, streets], axis=1)

	return DF