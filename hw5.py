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
        state: {row['City'] for row in zipcodes if row['State'] == state}
        for state in target_states
    }
    
    # return the intersection of common cities
    return sorted(set.intersection(*city_state_map.values()))



if __name__ == "__main__": 
    start_time = time.perf_counter()  # Do not remove this line
    '''
    Inisde the __main__, do not add any codes before this line.
    -----------------------------------------------------------
    '''

    

    # write your code here
    


    '''
    Inside the __main__, do not add any codes after this line.
    ----------------------------------------------------------
    '''
    end_time = time.perf_counter()
    # Calculate the runtime in milliseconds
    runtime_ms = (end_time - start_time) * 1000
    print(f"The runtime of the program is {runtime_ms} milliseconds.")  
    

