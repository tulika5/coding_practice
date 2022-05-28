#instead of checking everytime=> that will be expensive; it is better to handle when exception occurs
try:
    my_list=[1,2,3,4]
    for i in my_list:
        print(i)
        #raising custom exceptions
        if i==3:
            raise ValueError("ERORR: VALUE of i is 3")

#catching Exception; Exception is the base class of all errors; u can limit to specific error codes      
except Exception:
    print("Got an exception")
finally:
    print('This block will be executed in all cases whether or not expection occured;use eg to close files')