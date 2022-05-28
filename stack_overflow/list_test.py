#I want to ask the user which list they would like to access, then retrieve that list.
list1=[1, 2, 3, 4, 5]
list2=[6, 7, 8, 9, 10]
list3=['s', 'r', 't', 'd']

user_input=input('which list do you want to access')
#CAUTION: DON'T USE EVAL for unsanitized user input
#it just executes anything which user has entered; so it can be threat to security
#x=eval(user_input)

#GOOD SOLUTION
lists = {
    'list1': list1,
    'list2': list2,
    'list3': list3
}

user_input=input('which list do you want to access: ')
if user_input in lists:
    print('selected list:', lists[user_input])
else:
    print('no list matched')