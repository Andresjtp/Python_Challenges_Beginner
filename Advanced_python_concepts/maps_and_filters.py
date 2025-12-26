from functools import reduce #to use the recude function, we need to import it from functools module

# example of reduce function

numbers = [1, 2, 3, 4, 5, 6] #below is how the reduce function works step by step based on the sum function defined below
#         [3, 3, 4, 5, 6] -> after first step (1+2)
#         [6, 4, 5, 6] -> after second step (3+3)
#         [10, 5, 6] -> after third step (6+4)
#         [15, 6] -> after fourth step (10+5)
#         [21] -> after fifth step (15+6)

def sum(a, b):
    return a + b

c = reduce(sum, numbers)
print(c) # this will output the sum of all numbers in the list (21)

# Examples of Maps and Filters in Python

# Example of map function
number = [1, 2, 3, 4, 5] # a simple list of numbers

def square(x): #a simple function that squares a number
    return x * x

new = list(map(square, number))  # map applies the function to each item in the iterable (number)
print(new)

#we can also use lambda functions with map to make it more concise
new = list(map(lambda x: x * x, number))
print(new)


#example of filter function
a = [2, 3, 5, 67, 45, 2, 1, 4, 78, 79 , 6655 ,6775, 546 ,75 ,45 , 23]

def is_greater_than_9(x):
    if x > 9:
        return True
    else:
        return False

new = list(filter(is_greater_than_9, a)) # filter applies the function to each item in the iterable (a) and only keeps the items that return True
print(new)

#we can also use lambda functions with filter to make it more concise
new = list(filter(lambda x: x > 9, a))
print(new)


