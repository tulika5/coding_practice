#python: interpreted language; dynamically typed
#java: compiled language; statically typed

#PROGRAM: Calculate GPA based on input grades
#allow user to input as many grades they want; keep waiting for input unless newline entered
#keep a lookup dictionary to represent grade-marks relation
#compute GPA=total marks/num of grades

#dictionary
gpa_lookup={'A':10,'B':9,'C':8,'D':7,'E':6}

done_flag=False
num_subjects=0
total_marks=0
while not done_flag:
    grade=input()
    if grade=='':
        done_flag=True
    elif grade not in gpa_lookup:
        print(f"Invalid grade ={grade} has been entered.")
    else:
        total_marks+=gpa_lookup[grade]
        num_subjects+=1
if num_subjects>0:
    print(f"computed GPA={(total_marks/num_subjects)}")

#a=10; here a is identifier; 10 is object; a refers to the memory address of object
#b=a; so both a & b are referring to same object; if there is some way the object can transform the state,
# then the change will be reflected in both variables

#everything in python is class;
#class: blueprint; its instantiation is called object
