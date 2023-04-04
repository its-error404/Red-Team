from bs4 import BeautifulSoup
from html.parser import HTMLParser

if __name__ == "__main__":
    
    with open("simple.html") as html_file:
        soup = BeautifulSoup(html_file, "html")
        
    print(soup.title)
    print('*'*8)
    print(soup.title.string)
    print('*'*8)
    
    for cell in soup.find_all("td"):
        print(cell)
        
    print('*'*8)
    print(soup.prettify())
    print('*'*8)
    print(soup.get_text())