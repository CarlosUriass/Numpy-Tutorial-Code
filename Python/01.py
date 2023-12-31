# 1.1 List

## Data structure in Python: List

fruits = ["🍌","🍒","🍓","🍏","🍐"] # Declare a list

# 1.2 Accessing elements

print(fruits[0]) # Output = "🍌"
print(fruits[1]) # Output = "🍒"


## 1.2.1 Negative indexing

print(fruits[-3]) # Output = "🍓"
print(fruits[-2])  # Output = "🍏"

# 1.3 Data types
print(type(fruits[-2])) # Output = <class 'str'>

## 1.3.1 List with different data types

my_list = [1,"1","Hello!", 2.4, False]

# 1.3.2 Print data types

for i in my_list:
    print(type(i))

'''
Output:

<class 'int'>
<class 'str'>
<class 'str'>
<class 'float'>
<class 'bool'>
'''