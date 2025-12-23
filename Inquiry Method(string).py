#this is used to find the method of inquiry based on a given string input
#this is the function which define us about string is in upper,lower,title or capitalized case
s="hello world"
s1="HELLO WORLD"
s3=s.isalpha()
s4=s1.isupper()
s5=s.istitle()
s6=s.capitalize()
print(s3)  #False because of space
print(s4)  #True because all letters are in upper case
print(s5)  #False because first letter of each word is not in upper case
print(s6)  #Hello world because only first letter of first word is in upper case  
s7='HELLO World welcome'
s8=s7.islower()
s9=s7.isupper()
s10=s7.istitle()
print(s8)  #False because of upper case letters
print(s9)  #False because of lower case letters
print(s10) #False because first letter of each word is not in upper case  