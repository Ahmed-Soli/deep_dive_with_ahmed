"""
filter(fuction,iterable)
Filter() is a built-in function in Python. The filter function can be applied to an iterable such as a list or a dictionary and create a new iterator. This new iterator can filter out certain specific elements based on the condition that you provide very efficiently

filter function take a single function ( that takes only one argument) and a single iterable
returns an iterable
it removes the element that doesn't match with our function condition and returns an iterable with the newly filtered elements
"""

lst = [0,1,2,3,4]

print(list(filter(None,lst))) # [1, 2, 3, 4]

def is_even(num:int) -> bool:
    """this function takes a number and checks if it's even or odd and returns boolan value"""
    return num % 2 == 0 

print(list(filter(is_even,lst))) # [0, 2, 4]

print(list(filter(lambda n : n % 2 == 0 ,lst))) # [0, 2, 4]

# Normal way
filtered_lst = []
for num in lst:
    if num % 2 == 0 :
        filtered_lst.append(num)
print(filtered_lst) # [0, 2, 4]
