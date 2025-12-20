# this is used to add two comditon without using there names 
#for example 
a=int(input('enter a number:'))
b=int(input('enter a number:'))
c=int(input('enter a number:'))
if a>b and b>c:
   print('true')
else:
   print('false')
#instead of this we can just write like this only
a=int(input('enter a number:'))
b=int(input('enter a number:'))
c=int(input('enter a number:'))
if a>b>c:
      print('true')
else:
   print('false')
#the output for both will be the same for both the program 
#we can only use this with and only we cannot use it with or operator
   