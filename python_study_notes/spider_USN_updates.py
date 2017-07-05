import requests
from bs4 import BeautifulSoup

##To spider the USN update summary from page 1 to page max which is set in the code as max_page

def usn_spider(max_page):
        page = 1
        while page <= max_page:
                url = 'https://www.ubuntu.com/usn/xenial/?page=' + str(page)
                source_code = requests.get(url)
                plain_text = source_code.text
                soup = BeautifulSoup(plain_text,"lxml")
                for item in soup.find_all("h3"):
                        text = item.get_text()
                        #href ="https://www.ubuntu.com/" + item.get('href')
                        #print(href)
                        print(text)
                page += 1

usn_spider(1) ##Can change the max page here
