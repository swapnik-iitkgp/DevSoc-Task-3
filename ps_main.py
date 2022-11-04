#Print result after every function to check 
#Read the info in every functions to get the proper understanding of desired output

import json
from multiprocessing.sharedctypes import Value
filepaths='data.json'

def read_data(filepaths):
    with open(filepaths) as json_file:
      return json.load(json_file)
    # Read data from filepaths

data = read_data(filepaths)

def get_oldest(data):
    max = 0
    c = 0
    oldest = []
    for i in data["AVENGERS"]:
        if (data["AVENGERS"][i]['age'] > max):
            max = data["AVENGERS"][i]['age']
    for i in data["AVENGERS"]:
        if data["AVENGERS"][i]['age'] == max:
            oldest.append(data["AVENGERS"][i])

    for i in data["DC"]:
        if (data["DC"][i]['age'] > max):
            max = data["DC"][i]['age']
    for i in data["DC"]:
        if data["DC"][i]['age'] == max:
            oldest.append(data["DC"][i])
    # Return all info of the oldest superheroes
    # Return all info of the oldest superheroes
    return oldest

# returns info: Thor and Wonder Woman

def get_oldest_avenger(data):
   max=0
   oldest_avenger=[]
   for i in data["AVENGERS"]:
        if (data["AVENGERS"][i]['age'] >max):
            max=data["AVENGERS"][i]['age']
   for i in data["AVENGERS"]:
        if (data["AVENGERS"][i]['age'] == max):
            oldest_avenger.append(data["AVENGERS"][i])
    # Return all info of the oldest avenger
   return oldest_avenger

# returns info: Thor

def get_total_points(data):
    total_points={}
    k = 0
    for i in data["AVENGERS"]:
        key = str([m for m in data["AVENGERS"] if True][k])
        k+=1
        total_points[key] = 0
        for j in data["AVENGERS"][i]['points']:
            total_points[key]+=data["AVENGERS"][i]['points'][j]
    k = 0
    for i in data["DC"]:
        key = str([h for h in data["DC"] if True][k])
        k += 1
        total_points[key] = 0
        for j in data["DC"][i]['points']:
            total_points[key]+=data["DC"][i]['points'][j]
    # Return a dictionary
    # Key: superhero name
    # Value: total points
    return total_points

# returns info: Dict of superhero name and total points

def get_more_than_average(data):
    more_than_average=[]
    avg_mcu=0
    avg_dc=0
    for i in data["AVENGERS"]:
        avg_mcu+=data["AVENGERS"][i]["points"]["stealth"]
    avg_mcu=avg_mcu/len(data["AVENGERS"])
    c=0
    for i in data["AVENGERS"]:
        if(data["AVENGERS"][i]['points']['stealth']>avg_mcu):
            more_than_average.append(str([n for n in data["AVENGERS"] if True][c]))
        c+=1
    for i in data["DC"]:
      avg_dc+=data["DC"][i]['points']['strength']
    avg_dc=avg_dc/len(data["DC"])
    c = 0
    for i in data["DC"]:
        if(data["DC"][i]['points']['strength']>avg_dc):
            more_than_average.append(str([q for q in data["DC"] if True][c]))
        c+=1
    '''
    Return list of superheroes with stealth more than average in MCU
    and list of superheroes with strength more than average in DCEU
    '''
    return more_than_average

  #returns info: Steve Rogers and Superman

def get_names(data):
    names = []
    for i in data:
        value = {j for j in data[i] if True}
        names += list(value)
    # Return a list of superhero names
    return names

#returns a list 

