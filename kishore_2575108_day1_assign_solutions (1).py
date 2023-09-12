#!/usr/bin/env python
# coding: utf-8

# 

# # Manipulating using  a list

# In[1]:


lst = [22,'kishore']
lst


# In[14]:


lst.append(45)  #i)1.write a program to find the frist N prime numbers
lst


# In[12]:


lst.append(12) #ii)adding element of list
lst


# In[ ]:


ii)#To reverse elements in the list


# In[16]:


lst = [1, 2, 3, 4, 5]
lst.reverse()
print(lst)  # Output: [5, 4, 3, 2, 1]


# In[20]:


#iii) to display the same list of elements multiple times
lst = [22,44,55,66]
n=5
lst*n


# In[99]:


#iv)concatenated_list


a=['kish']
b=['ore']
c=a+b
print(c)




# In[100]:


lst1 = [1,2,3]
lst2 = [5,6]
lst3 = lst1 +lst2
lst3
print(lst3)


# In[127]:


#v)sorting
lst=[9,8,7,6]
lst.sort()
lst


# # 2.Write a python programme to do in a tuple 

# In[107]:


#i)Manipulate using tuples
my_tuple = [ 2,27,8,9]
my_tuple[1]



# In[106]:


a_tuple = [22,'kishore',52]
a_tuple[1]


# In[115]:


#ii)adding element of list
b_tuple =[1,'k','i','s']
b_tuple.append('h')
b_tuple



# In[117]:


#To reverse elements in the list
b_tuple =[1,'k','i','s']
b_tuple.reverse()
b_tuple


# In[130]:


tuple1=[1,'k','i','s']
tuple2=(9,8,6)
tuple=b_tuple1+b_tuple2
print([tuple])


# In[141]:


#v)sorting]
tuple1 =[9,8,7,6,]
tuple2 =[99.88]
tuple3= (tuple1,tuple2)
tuple1.sort()
tuple3


# # 3.write a python program to implement then following list

# In[142]:


#i)create a list with integers(min 10 numbers)
lst=[99,88,7,55,66,33,5,8,11,1222,3344,24]
lst


# In[34]:


#ii) 
my_list = [99,88,7,55,66,33,5,8,11,1222,3344,24]

# Using negative index -1 to get the last element
last_number = my_list[-1]

print(f"The last number in the list is: {last_number}")


# In[35]:


#iii)commanding for display the values from the list is [0:4]
my_list = [99,88,7,55,66,33,5,8,11,1222,3344,24]

# Display values from index 0 to 3 (inclusive of 0 and exclusive of 4)
values = my_list[0:4]

print("Values from the list:", values)


# In[37]:


#iv)commanding for display the values from the list is [2:]
my_list = [99,88,7,55,66,33,5,8,11,1222,3344,24]

# Display values from index 2 to the end of the list
values = my_list[2:]

print("Values from the list:", values)



# In[42]:


#v)commanding for display the values from the list is [:6]

my_list = [99,88,7,55,66,33,5,8,11,1222,3344,24]

# Display the first 6 values from the list
values = my_list[:6]

print("First 6 values from the list:", values)


# # 4.write a python program:tuple1=(10,50,20,40,30)
# 
# 

# In[45]:


#i) to display 
# Define the tuple
tuple1 = (10, 50, 20, 40, 30)

# Access and display the elements 10 and 50
element1 = tuple1[0]
element2 = tuple1[1]

print("Element 1:", element1)
print("Element 2:", element2)


# In[47]:


#ii)to display the length of tuple1
# Define the tuple
tuple1 = (10, 50, 20, 40, 30)

# Display the length of the tuple
length = len(tuple1)

print("Length of tuple1:", length)


# In[49]:


#iii)to find the minimum element from tuple1
# Define the tuple
tuple1 = (10, 50, 20, 40, 30)

# Find and display the minimum element from the tuple
min_element = min(tuple1)

print("Minimum element from tuple1:", min_element)


# In[51]:


#iv)to add all elements in the tuple1

# Define the tuple
tuple1 = (10, 50, 20, 40, 30)

# Add all elements in the tuple
total = sum(tuple1)

print("Sum of all elements in tuple1:", total)


# In[52]:


#v)to display the same tuple1 multiple times

# Define the tuple
tuple1 = (10, 50, 20, 40, 30)

# Display the tuple multiple times
n = 3  # Number of times to display
result = tuple1 * n

print("Tuple1 displayed", n, "times:", result)


# # 5.write a python program

# In[53]:


#i)to calculate length of string
# Input a string
user_input = input("Enter a string: ")

# Calculate and display the length of the string
length = len(user_input)
print("Length of the string:", length)


# In[54]:


#ii) to reverse words in a string
# Input a string
user_input = input("Enter a string: ")

# Split the string into words
words = user_input.split()

# Reverse the order of the words
reversed_words = words[::-1]

# Join the reversed words back into a string
reversed_string = ' '.join(reversed_words)

# Display the reversed string
print("Reversed string:", reversed_string)



# In[56]:


#iii) to display the same strings in multiple times
# Define the string
my_string = "Hello, World!"

# Display the string multiple times
n = 3  # Number of times to display
result = my_string * n

print("String displayed", n, "times:")
print(result)


# In[58]:


#iv) to concatenate two strings
# Define two strings
string1 = "Hello"
string2 = "World"

# Concatenate the two strings
concatenated_string = string1 + " " + string2

# Display the concatenated string
print("Concatenated string:", concatenated_string)


# In[60]:


#v)Str1="South India",using string slicing to display"India"
# Define the string
Str1 = "South India"

# Use string slicing to extract "India"
India_part = Str1[6:]

# Display the extracted part
print("Extracted part:", India_part)


# # 6.perform the following
# 

# In[61]:


#i)creating the dictionary
# Creating a dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Displaying the dictionary
print("Dictionary:", my_dict)


# In[62]:


#ii) accessing values and keys in the dictionary 
# Dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Accessing values using keys
name = my_dict["name"]
age = my_dict.get("age")

# Displaying values
print("Name:", name)
print("Age:", age)



# In[63]:


#iii)clear and delete  the dictonary values
# Dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Clearing all values from the dictionary
my_dict.clear()

# Displaying the empty dictionary
print("Empty Dictionary:", my_dict)



# In[39]:


#7.Program to insert a number at any position in a list 
def insert_number_to_position(input_list, number, position):
    if position < 0 or position > len(input_list):
        print("Invalid position. Position should be between 0 and the length of the list.")
    else:
        input_list.insert(position, number)
        print(f"{number} has been inserted at position {position}.")
        print("Updated list:", input_list)

if __name__ == "__main__":
    try:
        my_list = [1, 2, 3, 4, 5]
        print("Original list:", my_list)

        number = int(input("Enter the number you want to insert: "))
        position = int(input("Enter the position to insert the number: "))

        insert_number_to_position(my_list, number, position)
    except ValueError:
        print("Invalid input. Please enter valid numbers for the number and position.")


# In[4]:


#8.python programm to delete an element from a list by index 
def delete_element_by_index(input_list, index):
    if 0 <= index < len(input_list):
        deleted_element = input_list.pop(index)
        print(f"Deleted element: {deleted_element}")
    else:
        print("Invalid index. Index should be within the range of the list.")

if __name__ == "__main__":
    try:
        my_list = [1, 2, 3, 4, 5]
        print("Original list:", my_list)

        index = int(input("Enter the index of the element you want to delete: "))
        delete_element_by_index(my_list, index)
        
        print("Updated list:", my_list)
    except ValueError:
        print("Invalid input. Please enter a valid integer for the index.")


# In[5]:


#9.write a program to display a number from 1 to 100
for number in range(1, 101):
    print(number)


# In[7]:


#10 write a program to find the sum of all items in a tuple
def sum_of_tuple_items(t):
    total = 0
    for item in t:
        total += item
    return total

if __name__ == "__main__":
    try:
        # Example tuple
        my_tuple = (1, 2, 3, 4, 5)
        
        result = sum_of_tuple_items(my_tuple)
        
        print(f"The sum of items in the tuple is: {result}")
    except TypeError:
        print("Invalid input. Please provide a tuple of numbers.")


# In[28]:


#12.a list of words is given.find the words from the list that have theirsecond character in upper case is = ['hello','Dear','hOw','ARe',You']
# List of words
words = ['hello', 'Dear', 'hOw', 'ARe', 'You']

# Use a list comprehension to filter words with a uppercase second character
result = [word for word in words if len(word) > 1 and word[1].isupper()]

# Print the result
print("Words with an uppercase second character:", result)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # CONTROL STRUCTURES

# In[8]:


#1. first N prime number
def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def find_n_primes(n):
    primes = []
    number = 2  # Start with the first prime number
    while len(primes) < n:
        if is_prime(number):
            primes.append(number)
        number += 1
    return primes

if __name__ == "__main__":
    try:
        n = int(input("Enter the value of N: "))
        if n <= 0:
            print("N should be a positive integer.")
        else:
            prime_numbers = find_n_primes(n)
            print(f"The first {n} prime numbers are: {prime_numbers}")
    except ValueError:
        print("Invalid input. Please enter a valid positive integer for N.")



# In[9]:


#2.Salary
try:
    # Prompt the user to enter basic salary, HRA, TA, and DA
    basic_salary = float(input("Enter Basic Salary: "))
    hra = float(input("Enter HRA: "))
    ta = float(input("Enter TA: "))
    da = float(input("Enter DA: "))

    # Calculate the gross salary
    gross_salary = basic_salary + hra + ta + da

    # Deduct 10% as tax
    tax = 0.10 * gross_salary
    net_salary = gross_salary - tax

    # Display the gross and net salary
    print(f"Gross Salary: {gross_salary}")
    print(f"Tax (10% of Gross Salary): {tax}")
    print(f"Net Salary: {net_salary}")

except ValueError:
    print("Invalid input. Please enter valid numerical values for salary components.")


# In[13]:


#.search a string 
def search_string_in_list(search_list, target_string):
    found_indices = []
    for index, string in enumerate(search_list):
        if target_string in string:
            found_indices.append(index)
    return found_indices

if __name__ == "__main__":
    # Example list of strings
    my_list = ["apple", "banana", "cherry", "date", "elderberry", "fig"]

    target = input("Enter the string you want to search for: ")

    found_indices = search_string_in_list(my_list, target)

    if found_indices:
        print(f"The string '{target}' was found at indices: {found_indices}")
    else:
        print(f"The string '{target}' was not found in the list.")


# In[14]:


#4string 
def count_upper_lower_letters(input_string):
    upper_count = 0
    lower_count = 0

    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    upper_count, lower_count = count_upper_lower_letters(user_input)

    print(f"Number of uppercase letters: {upper_count}")
    print(f"Number of lowercase letters: {lower_count}")


# In[15]:


#5.odd and even numbers
# Initialize variables to store the sums
even_sum = 0
odd_sum = 0

# Iterate through numbers from 12 to 37 (inclusive)
for number in range(12, 38):
    if number % 2 == 0:  # Check if the number is even
        even_sum += number
    else:
        odd_sum += number

# Display the sums
print(f"Sum of even numbers between 12 and 37: {even_sum}")
print(f"Sum of odd numbers between 12 and 37: {odd_sum}")


# In[16]:


#6.Table of any city 
try:
    # Get the number for which you want to print the table
    num = int(input("Enter a number: "))

    # Print the multiplication table
    print(f"Multiplication Table for {num}:")
    for i in range(1, 11):
        result = num * i
        print(f"{num} x {i} = {result}")

except ValueError:
    print("Invalid input. Please enter a valid number.")


# In[17]:


#7.sum of first 10 prime numbers 
def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def sum_first_n_primes(n):
    primes = []
    number = 2  # Start with the first prime number
    while len(primes) < n:
        if is_prime(number):
            primes.append(number)
        number += 1
    return sum(primes)

if __name__ == "__main__":
    n = 10  # Sum the first 10 prime numbers
    prime_sum = sum_first_n_primes(n)
    print(f"The sum of the first {n} prime numbers is: {prime_sum}")


# In[20]:


#8.arthematic operayions
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    operation = input("Enter the operation (+, -, *, /): ")

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Division by zero is not allowed.")
            result = None
    else:
        print("Invalid operation.")

    if result is not None:
        print(f"Result: {result}")

except ValueError:
    print("Invalid input. Please enter valid numbers.")

    


# In[23]:


#9.Temperatue
try:
    # Get the temperature in Celsius from the user
    celsius = float(input("Enter the temperature in Celsius: "))

    # Convert Celsius to Fahrenheit
    fahrenheit = (celsius * 9/5) + 32

    # Display the converted temperature in Fahrenheit
    print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit")

except ValueError:
    print("Invalid input. Please enter a valid numerical temperature in Celsius.")



# In[24]:


#12. Number of seconds in a minute, hour, and day
seconds_per_minute = 60
seconds_per_hour = 60 * seconds_per_minute
seconds_per_day = 24 * seconds_per_hour

# Number of days in a year (assuming a non-leap year)
days_in_year = 365

# Calculate the number of seconds in a year
seconds_in_year = days_in_year * seconds_per_day

print(f"Number of seconds in a year: {seconds_in_year}")


# In[64]:


#13.a high  speed  train can travel at an average speed og 150mph,how long will ittake a traintravelling at this speed to travel from london to glassgow which is 414miles away
# Constants
distance_miles = 414  # Distance from London to Glasgow in miles
average_speed_mph = 150  # Average speed of the train in mph

# Calculate the time in hours
time_hours = distance_miles / average_speed_mph

# Display the time in hours and minutes
hours = int(time_hours)
minutes = (time_hours - hours) * 60

print(f"It will take approximately {hours} hours and {minutes:.2f} minutes to travel from London to Glasgow.")


# In[65]:


#14.write a python program that defines a variable called days_in_each_school_year and assign 192to the variable.the program should then printout out the totalhours that you spend in school fromyear 7 to year11,if each day spend 6 hours indays_in_each_school_year=192
# Define the variable
days_in_each_school_year = 192

# Calculate the total hours spent in school from year 7 to year 11
total_years = 11 - 7 + 1  # Years 7, 8, 9, 10, 11
total_hours = total_years * days_in_each_school_year * 6

# Display the total hours
print(f"Total hours spent in school from year 7 to year 11: {total_hours} hours")


# In[ ]:


#15.if the age of ram,sam and khan are input through the keyword,write a pythonprogram to determine the eldest and youngest of the tree
# Input ages of Ram, Sam, and Khan
ram_age = int(input("Enter Ram's age: "))
sam_age = int(input("Enter Sam's age: "))
khan_age = int(input("Enter Khan's age: "))

# Find the eldest and youngest
if ram_age >= sam_age and ram_age >= khan_age:
    eldest = "Ram"
    if sam_age <= khan_age:
        youngest = "Sam"
    else:
        youngest = "Khan"
elif sam_age >= ram_age and sam_age >= khan_age:
    eldest = "Sam"
    if ram_age <= khan_age:
        youngest = "Ram"
    else:
        youngest = "Khan"
else:
    eldest = "Khan"
    if ram_age <= sam_age:
        youngest = "Ram"
    else:
        youngest = "Sam"

# Display the results
print(f"The eldest person is {eldest} with age {max(ram_age, sam_age, khan_age)} years.")
print(f"The youngest person is {youngest} with age {min(ram_age, sam_age, khan_age)} years.")


# In[26]:


#16.right n times with and without slicing 
def rotate_right_with_slicing(arr, n):
    n = n % len(arr)
    rotated_list = arr[-n:] + arr[:-n]
    return rotated_list

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    n = 2  # Number of times to rotate to the right

    rotated_list = rotate_right_with_slicing(my_list, n)
    print(f"Rotated list with slicing: {rotated_list}")


# In[ ]:




