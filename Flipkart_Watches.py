from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
#url
url="https://www.flipkart.com/mens-watches-store?otracker=nmenu_sub_Men_0_Watches"
html=urlopen(url)
Soup=BeautifulSoup(html,'lxml') #lxml is technique of parsing
#access the whole block
li=Soup.find_all('div',class_="_3liAhj _2Vsm67")
l=[]
for i in range(li.__len__()):
    e=list()
    #access Heading
    e.append(li[i].find('a',class_="_2cLu-l").text)
    #access Price
    e.append(li[i].find('div',class_="_1vC4OE").text)
    #access rating
    if li[i].find('div',class_="hGSR34"):
        e.append(li[i].find('div',class_="hGSR34").text)
    else:
        e.append("NAN")
    l.append(e)
df=pd.DataFrame(l,columns=['ITEM','PRICE','RATING'])
df.to_csv('Flipkart.csv',index=False)#write to csv