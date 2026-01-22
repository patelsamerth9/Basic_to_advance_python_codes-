#this is used to remove unwanted characters from the beginning and end of a string.
#it is often used to clean up user input or data read from files.
s = '   hello world!!!   '
lstrip = s.lstrip()  # Remove leading whitespace
print(lstrip)  # Output: 'hello world!!!   '
print(type(lstrip))#<class 'str'>
print(id(lstrip))#id of the new string
print(id(s))#id of the original string
rstrip = s.rstrip(' !')  # Remove trailing spaces and exclamation marks
print(rstrip)  # Output: '   hello world'
strip = s.strip(' !')  # Remove leading and trailing spaces and exclamation marks
print(strip)  # Output: 'hello world'
# Demonstrating that original string remains unchanged
print(s)  # Output: '   hello world!!!   ' 
# This is useful for cleaning up strings, especially when dealing with user input or data from files. The original string remains unchanged, as strings in Python are immutable.  
# Strings in Python are immutable, so these methods return new strings with the specified characters removed, leaving the original string unchanged.
s1='***Welcome to Python Programming***.           '
strip=s1.strip(' *.          ')# Remove leading and trailing asterisks, spaces, and periods
print(strip)  # Output: 'Welcome to Python Programming'