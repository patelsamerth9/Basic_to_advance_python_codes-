n = int(input("Enter how many numbers: "))
print("Enter", n, "numbers:")
Max = int(input())   # first number as maximum
for i in range(1, n):
    num = int(input())
    if num > Max:
        Max = num
print("Maximum number is:", Max)