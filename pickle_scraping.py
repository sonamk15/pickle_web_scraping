import requests
from bs4 import BeautifulSoup
from pprint import pprint

URL= "https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
page = requests.get(URL)
soup = BeautifulSoup(page.text, "html.parser")
# div = soup.findAll('div',class_="_3RA-")
div = soup.findAll("div",class_="_1fje")
def picle_detial(div):
    picle_list = []
    for j in div:
        picle_detials = j.findAll('div',class_="_3WhJ")
        for i in picle_detials:
            poster = i.findAll('div' ,class_="_3nWP" )
            for url in poster:
                img_url =  url.find('img',src=True)['src']
            pickle_name=i.findAll('div',class_="_2apC")
            for j in pickle_name:
                name = (j.text)
            price = i.find('div',class_="_1kMS").text
                    
            picle_dic = {}

            picle_dic["name"]=name
            picle_dic["rupees"]=price
            picle_dic["img_url"]=img_url

            picle_list.append(picle_dic)
    return picle_list
pprint (picle_detial(div))
        