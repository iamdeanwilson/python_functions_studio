# We want to COMPLETELY reverse a list by flipping the order of the entries AND flipping the order of characters in each element.

# a) Define a 'reverse_characters' function. Give it one parameter, which will be the string to reverse.

def reverse_characters(string):

# b) Within the function, use the 'list' function to split a string into a list of individual characters

  string_list = list(str(string))
  
# c) 'reverse' your new list.

  string_list.reverse()
  
# d) Use 'join' to create the reversed string and return that string from the function.
  
  reversed_string = ''.join(string_list)

  if reversed_string.isnumeric():
    reversed_string = int(reversed_string)
  
# e) Create a variable of type string to test your new function. # f) Use 'print(reverse_characters(my_variable_name))'; to call the function and verify that it correctly reverses the characters in the string.

  return reversed_string

# g) Use method chaining to reduce the lines of code within the function.

reverse_characters(651871774) 

# 2) The 'split' method does not work on numbers, but we want the function to return a number with all the digits reversed (e.g. 1234 converts to 4321 and NOT the string "4321")
# a) Add an if statement to your reverse_characters function to check the typeof the parameter.
# b - d) If type is ‘string’, return the reversed string as before. If type is ‘number’, convert the parameter to a string, reverse the characters, then convert it back into a number. Return the reversed number.
# e) Be sure to print the result returned by the function to verify that your code works for both strings and numbers. Do this before moving on to the next steps.

# 3) Create a new function with one parameter, which is the list we want to change. The function should:

def reverse_list(list):

# a) Define and initialize an empty list.

  empty_list = []

# b) Loop through the old list.

  for i in list:
  
# c) For each element in the old list, call reverse_characters to flip the characters or digits.

    reversed = reverse_characters(i)

# d) Add the reversed string (or number) to the list defined in part ‘a’.

    empty_list.append(reversed)

  

# e) Return the final, reversed list.

  empty_list.reverse()
  
  return empty_list
  
# f) Be sure to print the results from each test case in order to verify your code.

list_test1 = ['apple', 'potato', 'Capitalized Words']
list_test2 = [123, 8897, 42, 1168, 8675309]
list_test3 = ['hello', 'world', 123, 'orange']

print(reverse_list(list_test2))
