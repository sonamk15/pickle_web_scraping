import requests
from bs4 import BeautifulSoup
URL= "https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
page = requests.get(URL)
soup = BeautifulSoup(page.text, "html.parser")
# div = soup.findAll('div',class_="_3RA-")
div = soup.findAll("div",class_="_1fje")
for i in div:
    name=i.findAll('div',class_="_2apC")
    # name=i.findAll('div',class_="_1fje")
    for j in name:
        print (j.text)
        # k = j.findAll('div',class_="_2apC")
        # for x in k:
        #     print (x.text)
    # print (i.prettify())
# for i in div:
