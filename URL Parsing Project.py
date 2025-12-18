url = "https://www.example.com/index.html"
parts = url.split("/")
print("Protocol:", parts[0][:-1])
print("Domain:", parts[2])
print("Page:", parts[-1])