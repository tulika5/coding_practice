#merge 2 dictionaries x & y without modifying original dicts; 
#last-one-wins conflict-handling of dict.update() as well.
# so that ans={'a': 1, 'b': 10, 'c': 11}
x = {'a': 1, 'b': 2}
y = {'b': 10, 'c': 11}
print(x|y)

#PROBLEM 2:
#GIVEN input:
given_ip=[{'id_1': 5}, {'id_2': 10}, {'id_2': 4}]
#Expected output:
# [
#  [5],
#  [10,4]
# ]
processing_Dict={}
for dict_elem in given_ip:
    #iterating key,value in dictionary
    for dict_key,dict_value in dict_elem.items():
        #checking key in dictionary
        if dict_key in processing_Dict:
            processing_Dict[dict_key].append(dict_value)
        else:            
            processing_Dict[dict_key]=[dict_value]
print(list(processing_Dict.values()))