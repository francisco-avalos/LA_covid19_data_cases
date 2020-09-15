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
        return false


def parse_address(DF, address):
	"""
	Function splits addresses 
	"""


	streets = []

	for i in address.str.split(','):
		streets.append(i)

	streets = pd.DataFrame(streets)

	DF = pd.concat([DF, streets], axis=1)

	return DF