import random
options = {
    "Pizza": 3,
    "Home-cooked Pasta": 5,
    "Salad (Be healthy!)": 1,
    "Tacos": 4
}
pool = [item for item, weight in options.items() for _ in range(weight)]

selection = random.choice(pool)
print(f"The universe has spoken: You are eating {selection}.")