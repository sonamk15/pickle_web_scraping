import requests
from bs4 import BeautifulSoup
URL= "https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
page = requests.get(URL)
soup = BeautifulSoup(page.text, "html.parser")
# div = soup.findAll('div',class_="_3RA-")
div = soup.findAll("div",class_="_1fje")
for i in div:
    poster = i.findAll('div' ,class_="_3nWP" )
    for url in poster:
        img_url =  url.find('img',src=True)['src']
    # print (i.prettify()
    name=i.findAll('div',class_="_2apC")
    for j in name:
        print (j.text)
        
    price = i.find('div',class_="_1kMS").text
    # print (price) 