import requests


name = input("Your name? ")
print("Hello,", name)
print("Goodbye,", name)

r = requests.get("https://google.com")

print(r.status_code)
