import requests

request_bbc = requests.get("https://www.bbc.co.uk")
request_google = requests.get("https://www.google.co.uk")


print("-------------------The Status Code-------------------")
print(request_bbc.status_code)
input()

print("-------------------The Content-------------------")
print(request_bbc.content)
input()

print("-------------------The Status Code-------------------")
print(request_google.status_code)
input()

print("-------------------The Content-------------------")
print(request_google.content)
