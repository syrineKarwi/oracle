


from urllib.request import urlopen as uRep
from bs4 import BeautifulSoup as soup
start_url='https://www.mytek.tn/3-informatique'
links=[]
max_page=1
current_page=0


def Article(url):
    global links
    uClient = uRep(url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html,"html.parser")
    containers = page_soup.findAll("li",{"class":"ajax_block_product"})
    for container in containers:
        title_container = container.find("a",{"class" : "product_img_link"})
        href=title_container.get('href')
        if ('search' not in href and 'page' not in href):
            links.append(href)
            print("saved",href)
    if (current_page < max_page):
        newlink = page_soup.find('ul',{'class':'pagination'}).find('a').get('href')
        if (newlink):
            current_page=current_page+1
            Article(start_url+newlink)

Article(start_url)
