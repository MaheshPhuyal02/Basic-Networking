import requests

print("Welcome to basic request and get program")
print("****************************************")
link = input("Paste your link here: ")
r = requests.get(link)
print(r.status_code)
print(r.headers)
print(r.content)
