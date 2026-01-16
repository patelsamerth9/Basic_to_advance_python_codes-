#it is same as the range function
#the syntax is string[start:stop:step]
#start is inclusive, stop is exclusive
#step is optional, default is 1
#we can omit start, stop or both
#omitting start means starting from index 0
s="Hello, World!"
print(s[0:3])      # Hel
print(s[7:12])     # World
print(s[:5])       # Hello character has index -1, the second last -2, and so on.
#if we dont provide start index it starts from 0
#if we dont provide stop index it goes till the end of the string it will give entire string
s1="Python Programming"
print(s1[1::2])
s2=s1[::-1]#reversing the string
print(s2)#this can reverse any string and then it is used to check palindrome       