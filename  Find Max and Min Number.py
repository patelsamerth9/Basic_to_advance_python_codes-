n = 5
print("Enter 5 numbers:")
Max = int(input())   # take first number as maximum
for i in range(1, n):
    num = int(input())
    if num > Max:
        Max = num
print(Max)