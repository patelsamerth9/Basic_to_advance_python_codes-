users = [
    {"name": "Alice", "score": 92},
    {"name": "Bob", "score": 75},
    {"name": "Charlie", "score": 88},
    {"name": "Daisy", "score": 60},
    {"name": "Ed", "score": 95}
]

# 1. List Comprehension: Filter users with score >= 80
winners = [u for u in users if u["score"] >= 80]
winners.sort(key=lambda x: x["score"], reverse=True)

print("--- Top Scorers ---")
for person in winners:
    print(f"{person['name']}: {person['score']}")