from ast import List
from collections import Counter
from inspect import signature


integer_list = [5,4,5,4,5,4,4,5,3,3,3,2,2,1,5]

def nth_most_rate_signature(list:List, n:int):
    list = Counter(list).items()
    
    # This loop outlines the item and the value as the number of times the item occurred 
    for (item, occurrance) in list:
        if n == occurrance:
            nth_rarest = str(item) + ' is the number '+ str(n) +' rarest in the listed items'
            return print(nth_rarest)
        

# The signature function is assigned to a variable and
#  returns the arguments passed into the functions parameter
func_signature = signature(nth_most_rate_signature)

y = func_signature.parameters['list'].annotation
x = func_signature.parameters['n'].annotation

# calling the function
nth_most_rate_signature(integer_list,2)


# reveals the properties of the arguments of the function wrapped inside the signature function 
print('Signature of parameter "n" passed into the function: ' + x)
print('Signature of parameter "list" passed into the function: ' + y)