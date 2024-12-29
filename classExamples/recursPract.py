import random
import math

    # 1. map(str, my_list):
        ## map(dataType, list) == Convert each item in list to passed data parameter.
    # 2. "[delimiter]".join(someStr):
        ## join() == joins the items in list using the specified delimiter .

random_number = random.randint(1, 12)
print ("Starting Number: " + str(random_number))
print ("_______________________")
num_list =[]

def factorial(n):
    if n == 0:
        return 1
    else:
        if num_list == []:
            
            print("Let's begin! First up..." + str(n))
            num_list.append(n)
            currVal=  math.prod(num_list) 
            
            print(" * ".join(map(str, num_list)) + " = " + str(currVal))
            print("_________________")
            return n * factorial(n - 1)
        
        else:
            print("Next is... " + str(n))
            num_list.append(n)
            currVal=  math.prod(num_list) 

            print(" * ".join(map(str, num_list)) + " = " + str(currVal))
            print("_________________")
            return n * factorial(n - 1)

#Test function
result = factorial(random_number)
print("========================")
print("The Final result is: " + str(result))