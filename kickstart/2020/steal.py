import requests

# https://postb.in/1595107388509-5068783329334

postbin = input("Postbin: ")

i = 0

while True:
    i += 1
    payload = {"pingseq":i}
    requests.get(url = postbin, params = payload)