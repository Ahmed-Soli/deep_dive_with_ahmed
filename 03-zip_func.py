"""
zip function is not a highr order function
zip(*iterables) -> new iterable consists of a tuple combination of each element in the iterables
lst_1 = [1,2,3,4]
lst_2 = [10,20,30,40]
print(zip(lst_1,lst_2)) # [(1, 10), (2, 20), (3, 30), (4, 40)]

it iterate over the iterables till it exausted the shortest iterable
"""

lst_1 = [1,2,3,4]
lst_2 = [10,20,30,40]
print(list(zip(lst_1,lst_2))) # [(1, 10), (2, 20), (3, 30), (4, 40)]