"""
a higher order functoin => is a function that takes a function as a parameter and/or returns a function as it's return value
ex: sorted,map,filter
map(func,*iterables) -> iterator
*iterables  => a variable number of iterable objects
func        => some function that takes as many arguments as there are iterable objects passed to the iterables
map func    => returns an iterator 

example1 :
lst = [1,2,3]
def calculate_square(num:int) -> int:
    '''this function takes a number and returns the square root'''
    return num **2 #**2 means num to the power of 2

print(list(map(calculate_square,lst)))

example2 :
lst_1 = [1,2,3]
lst_2 = [10,20,30]
def add_two_numbers(num_1:int,num_2:int) -> int:
    '''this function takes two numbers and returns the addition'''
    return num_1 + num_2

print(list(map(add_two_numbers,lst_1,lst_2)))

"""

lst = [1,2,3]
def calculate_square(num:int) -> int:
    '''this function takes a number and returns the square root'''
    return num **2 #**2 means num to the power of 2

print(list(map(calculate_square,lst))) # [1, 4, 9]
print(list(map(lambda num:num **2,lst))) # [1, 4, 9]

lst_1 = [1,2,3]
lst_2 = [10,20,30]
def add_two_numbers(num_1:int,num_2:int) -> int:
    '''this function takes two numbers and returns the addition'''
    return num_1 + num_2

print(list(map(add_two_numbers,lst_1,lst_2)))  #[11, 22, 33]


# Normal way
addition_lst = []
for i in range(0,len(lst_1)):
    new_num = lst_1[i] + lst_2[i]
    addition_lst.append(new_num)
print(addition_lst)




