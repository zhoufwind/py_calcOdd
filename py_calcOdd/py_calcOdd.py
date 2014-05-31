# print('Hello World')

# Calculate the odd numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Option 1: using a new list to show the odd numbers
odd = numbers[0::2]
print odd

# Option 2: delete all the even numbers
del numbers[1::2]
print numbers

# NOTICE: I cannot using extended slice to delete even numbers
#numbers[1::2] = []
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#ValueError: attempt to assign sequence of size 0 to extended slice of size 5

