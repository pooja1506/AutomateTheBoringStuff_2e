import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(type(res))

res.status_code == requests.codes.ok
print(len(res.text))

print(res.text[:250])