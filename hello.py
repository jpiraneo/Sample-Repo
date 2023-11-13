import requests


name = input("Your name? ")
print("Hello,", name)

r = requests.get("https://google.com")

print(r.status_code)
