num = 1234
total = 0
while num > 0:
    total += num % 10
    num //= 10
print("Sum of digits:", total)