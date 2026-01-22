n = int(input("Enter a number: "))
i = 0
while n > 0:
    i+=1
    n= n // 10
print("Total Digits:", i)
#with the help of while loop we can count the digits of a number by continuously dividing the number by 10 until it becomes 0, incrementing a counter at each step. 