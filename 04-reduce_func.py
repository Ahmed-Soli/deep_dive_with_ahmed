"""
Reducing Function are functions that recombine an iterable recursively, ending up with a single return value
That are called accumulatars , aggregatars , folding functions 
from functools import reduce
reduce(fun,iterable,initializer=None)
initializer => if it's specified, it's essentially like adding it to the front of the iterable and it's often used to provide some kind of default in case the iterable is empty

Ex : find the maximum value in an iterable
a0,a1,a2,a3,.......,a(n-1)
we define a function that takes two paramters (a,b) -> and it returns the maximum of a and b
then we start by setting result = a0
then we iterate over the iterable finding the max and updating the result variable
result = max(result,a1)
result = max(result,a2)
result = max(result,a3)
result = max(result,a(n-1))
"""

# Normal way
lst = [0,1,5,6,7,51,65,98,12,56,24]
max_value = lambda a,b : a if a> b else b

def max_sequance(sequance):
    result = sequance[0]
    for num in sequance[1:] :
        result = max_value(num,result)
    return result

print(max_sequance(lst)) # 98
print(max(lst)) # 98 We can say that max_sequance is the implemenation of max

"""
instead of hardcoding the function max_value inside max_sequance we can pass it as an argument and extend the usage 
"""

def _reduce(fun,sequance:iter) -> int:
    result = sequance[0]
    for num in sequance[1:] :
        result = fun(num,result)
    return result

print(_reduce(fun=max_value,sequance=lst)) # finding Max value
print(_reduce(fun=lambda a,b:a+b,sequance=lst)) # finding sum value
print(_reduce(fun=lambda a,b:a if a < b else b,sequance=lst)) # finding min value

"""
Now let's import the built in reduce function
Important Notes:reduce works on any iterable like sets and strings(based on ASCI codes)
"""
from functools import reduce
print(reduce(max_value,lst)) # finding Max value 
print(reduce(lambda a,b:a+b,lst)) # finding sum value
print(reduce(lambda a,b:a if a < b else b,lst)) # finding min value
print(reduce(lambda a,b:a + ' ' + b ,('My','Name','Is','Ahmed'))) # concatenating the string and acting as ''.join()

"""
Popular built-in Reducing Functions
min min([1,2,3,4,5,6]) => 1
max min([1,2,3,4,5,6]) => 1
sum
any
all 
"""

print(reduce(lambda a,b:True if bool(a) or bool(b) else False,lst)) # any
print(any(lst)) # any
print(reduce(lambda a,b:True if bool(a) and bool(b) else False,lst)) # all
print(all(lst)) # any