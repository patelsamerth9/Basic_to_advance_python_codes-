i=int(input('enter a number: '))
while i>0:# infinite loop
    i+=1
    if i%3==0:# condition to skip even numbers
        continue# continue to the next iteration
    print(i)# print odd numbers only
   