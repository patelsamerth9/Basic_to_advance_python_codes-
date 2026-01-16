#This is used to seperate or join the strings based on the given separator
s = 'hello how are you samarth'#this is the string that we created
s1=s.replace(' ','-')#this will replace all the spaces with hyphens
print(s1)#hello-how-are-you-samarth
s2=s.replace(' ',',',3)#this will replace all the spaces with commas but only first 3 occurrences
print(s2)#hello,how,are,you samarth
s3=s.replace('k','m',2)#this will try to replace k with m but as k is not present in the string it will return the original string
print(s3)#hello how are you samarth
# The original string remains unchanged, as strings in Python are immutable.
print(s3)#hello how are you samarth