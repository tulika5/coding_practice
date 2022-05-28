# list & tuple= both collection of heterogeneous elements
# but tuple is immutable; as a result more memory efficient:
#As lists are mutable, Python needs to allocate an extra memory block in case there is a need to extend the size of the list object after it is created. 
# In contrary, as tuples are immutable and fixed size, Python allocates just the minimum memory block required for the data.
my_list=[]
my_list=[3,4]
my_tuple=(1,) #single element tuple
#use tuple whenever collection is not supposed to be mutated

#set: distinct elemnents only; but no guarantee of order
my_set={3,2}

#FOR LOOP
for i in [1,2,3,4]:
    print(i)
    if i==3:
        #terminate the loop
        break;
    if i==4:
        #skip further process in this iteration; go to next iteration
        continue;

#function: stateless computation; ie return result acc. to input; no old state saved
#eg. function to count occurences of target element in given iterable data

def count(data, target,text_msg="hello"):
    print(text_msg)
    n=0
    for item in data:
        if item == target: # found a match
            n += 1
    return n
#calling function using positional arguments method
grades=['A','A','B']
prizes = count(grades, 'A' )
#using default parameter:
prizes = count(grades, 'A',"my_msg" )
# above case is called polymorphism; becoz same function can have diff. method signature

#keyword arguments:
prizes = count(data=grades,text_msg="new_msg",target='B')