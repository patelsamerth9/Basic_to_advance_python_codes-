# Loop through numbers 1 to 10
for i in range(1, 11):
    print(f"Table of {i}:")
    for j in range(1, 11):
        result = i * j
        print(f"{i} x {j} = {result}")
    print("-" * 15)