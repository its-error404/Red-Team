import requests
from random import randrange
from collections import namedtuple

http_proxies = ["http://90.114.27.196:3128", "http://72.169.66.253:87", "http://197.234.13.27:4145"]
user_agnets = ["Mozilla/5.0 (Linux; Android 12; POCO X2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Mobile Safari/537.36","Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 6.0; .NET CLR 2.1.14270)","Mozilla/5.0 (Linux; Android 11; ONEPLUS A6010) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.40 Mobile Safari/537.36"]

def random_agent():
    
    agent_index = randrange(0, len(user_agnets))
    headers = {"user-agent":"{}".format(user_agnets[agent_index])}
    return headers
    
def random_proxy():
    
    proxy_index = randrange(0,len(http_proxies))
    proxy = {"http": "{}".format(http_proxies[proxy_index])}
    return proxy
    
def therequest():
    
    r = requests.get("http://testing-ground.webscraping.pro/whoami",proxies=random_proxy(), headers=random_agent())
    return r.text, r.cookies

if __name__ == "__main__":
    
    results = therequest()
    
    Scraper = namedtuple("Scraper", ["html","cookies"])
    scrape = Scraper(results[0],results[1])
    
    print(scrape.html)
    print(scrape.cookies)
    
    