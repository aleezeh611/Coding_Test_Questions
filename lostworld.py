import requests
import sys

def operations_code(code,val):
    if len(val) == 1:
        return val[0]

    if code == 'BAR':
        res = 999999
        for i in range(len(val)):
            if val[i] < res:
                res = val[i]

    if code == 'FOO':
        res = 0
        for i in range(len(val)):
            res += val[i]
        
    if code == 'FOX':
        res = -999999
        for i in range(len(val)):
            if val[i] > res:
                res = val[i]

    return res


def lostword():
    #Read url from file 
    inFile = sys.argv[1]
    with open(inFile,'r') as i:
        lines = i.readlines()

    link = 'https://jsonkeeper.com/' + lines[0]

    response_API = requests.get(link)
    #print(response_API.status_code)


    tempdata = response_API.json()
    data = tempdata['data']

    #STEP 1: GROUP MASK VALUES
    group_mask_values = {}
    for i in range(len(data['masks'])):
        if data['masks'][i] not in group_mask_values:
            group_mask_values[data['masks'][i]] = []
        group_mask_values[data['masks'][i]].append(data['timelines'][i])

    #STEP 2 PERFORM SUB OPERATIONS ACCORDING TO TRANSLATION TABLE AND MASK VALUES KEY-VALUE PAIRS
    store_temp_results = []
    for mask in group_mask_values:    
        if mask not in data['action_plan']['sub_operations']:
            store_temp_results.append(0)
        else:
            store_temp_results.append(operations_code(data['action_plan']['sub_operations'][mask], group_mask_values[mask]))
    
    #PERFORM ACTION ACCORDING TO GIVEN OPERATION IN ACTION PLAN
    result = operations_code(data['action_plan']['operation'], store_temp_results)

    return result


print(lostword())
