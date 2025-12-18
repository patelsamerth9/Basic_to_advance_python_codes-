num = 9876
count = 0
while num > 0:
    num //= 10
    count += 1
print("Total Digits:", count)