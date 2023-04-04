import requests

proxies = {"http" : "45.250.163.170:8081"}
headers = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/109.0.5414.83 Mobile/15E148 Safari/604.1"}

r = requests.get("http://testing-ground.webscraping.pro/whoami",proxies = proxies, headers = headers)

print ( r.text )

for cookie in r.cookies:
    print(cookie)
    
print(r.cookies["TestingGround"])