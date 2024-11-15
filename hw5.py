import time
import csv
"""
  Homework#5

  Add your name here: Ethan Varner 

  You are free to create as many classes within the hw5.py file or across 
  multiple files as you need. However, ensure that the hw5.py file is the 
  only one that contains a __main__ method. This specific setup is crucial 
  because your instructor will run the hw5.py file to execute and evaluate 
  your work.

"""
"""
1- => Lambda was used in line/s: ............
2- => Filter or map was used in line/s: ...........
3- => yield was used in line/s: .........
"""

""""""""""""""""""""""""""""""""""""



"""_______________________________________________Gather all data______________________________________________________________"""


def parse_data(filename):
    """Store each line of zipcodes.txt in a dictionary with the first line (the headers) as keys for simplificaiton"""
    with open(filename, 'r') as file:
        """Split by tab"""
        reader = csv.DictReader(file, delimiter='\t')
        return [row for row in reader]
    

"""_______________________________________________Common Cities________________________________________________________________"""    


def get_common_cities(zip_filename, states_filename):
    """Parse data files and return all common cities"""
    # load states from states input file
    with open(states_filename, 'r') as file:
        target_states = set(file.read().strip().split())
    
    # use dictionary comprehension to gather data. ChatGPT assisted me in doing this
    zipcodes = parse_data(zip_filename)
    city_state_map = {
        # Picking each city in the zipcodes rows only if the corresponding states are equal
        state: {row['City'] for row in zipcodes if row['State'] == state}
        for state in target_states
    }
    
    # return the intersection of common cities
    return sorted(set.intersection(*city_state_map.values()))


def write_common_cities(cities, filename):
    """Write list of common cities to CommonCityNames.txt"""
    # open file and print in format
    with open(filename, 'w') as file:
        file.writelines(f"{city}\n" for city in cities)


"""_______________________________________________Lat Lon_______________________________________________________________________"""


def get_lat_lon(zip_filename, zips_filename):
    """Return a dictionary with zip codes as keys and lat and lon as values"""
    # read zip codes from zips.txt
    with open(zips_filename, 'r') as file:
        target_zips = set(file.read().strip().split())

    # use dictionary comprehension to gather relevant data for lat lon 
    # ChatGPT assisted me in making sure this was correct
    zip_data = parse_data(zip_filename)
    lat_lon_dictionary = {
        # make a new dictionary where the keys are zip codes and the 
        # values are strings containing the lat and long
        row['Zipcode']: f"{row['Lat']} {row['Long']}"
        for row in zip_data if row['Zipcode'] in target_zips
    }
    return lat_lon_dictionary

def write_lat_lon_data(lat_lon_map, filename):
    """Write lat lon data to LatLon.txt"""
    with open(filename, 'w') as file:
        # open file and print in format
        file.writelines(f"{lat_lon}\n" for lat_lon in lat_lon_map.values())


"""_______________________________________________Citystates____________________________________________________________________"""


def get_citystates(zipcodes, cities_file):
    """Parse cities.txt and create a dictionary of states that contain that city"""
    # Open and parse
    with open(cities_file, 'r') as file:
        cities = [line.strip().upper() for line in file]

    # Use list comprehension and dictionary comprehension to build city_states
    # ChatGPT assisted me in condensing this to this solution
    city_states_dictionary = {
        # it's just sql at this point
        # create new dictionary where the keys are cities and the 
        # values are sets of states where the city appears. 
        # sort out based on alphabetical order, removal of duplicates, etc
        city: sorted(set(entry['State'] for entry in zipcodes if entry['City'] == city))
        for city in cities if any(entry['City'] == city for entry in zipcodes)
    }
    # return city_states and cities both 
    return city_states_dictionary, cities


def write_citystates(city_states, output_file, cities):
    """Write states containing the city to CityStates.txt"""
    with open(output_file, 'w') as file:
        # ChatGPT assisted slightly with the formatting of this
        # write in format
        file.writelines(
            ' '.join(city_states.get(city, [])) + '\n'
            for city in cities
        )



if __name__ == "__main__": 
    start_time = time.perf_counter()  # Do not remove this line
    '''
    Inisde the __main__, do not add any codes before this line.
    -----------------------------------------------------------
    '''

    # write your code here

    # Common Cities
    common_cities = get_common_cities('zipcodes.txt', 'states.txt')
    write_common_cities(common_cities, 'CommonCityNames.txt')

    # LatLon
    lat_lon_map = get_lat_lon('zipcodes.txt', 'zips.txt')
    write_lat_lon_data(lat_lon_map, 'LatLon.txt')

    # CityStates
    city_states_map, cities = get_citystates(parse_data('zipcodes.txt'), 'cities.txt')
    write_citystates(city_states_map, 'CityStates.txt', cities)

    '''
    Inside the __main__, do not add any codes after this line.
    ----------------------------------------------------------
    '''
    end_time = time.perf_counter()
    # Calculate the runtime in milliseconds
    runtime_ms = (end_time - start_time) * 1000
    print(f"The runtime of the program is {runtime_ms} milliseconds.")  
    

