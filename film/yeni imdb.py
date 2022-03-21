import requests 
from bs4 import BeautifulSoup 
print("FİLMLER".ljust(50),"YILI","PUANI".ljust(4),"SAYISI") 
url="https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"
html=requests.get(url).content 
soup=BeautifulSoup(html,"html.parser")  
list=soup.find("tbody",{"class":"lister-list"}).find_all("tr") 
i=1
for tr in list: 
    title=tr.find("td",{"class":"titleColumn"}).find("a").text 
    year=tr.find("td",{"class":"titleColumn"}).find("span").text.strip("()") 
    point=tr.find("td",{"class":"imdbRating"}).find("strong") 
    point = str(point).split('<strong title=')[-1][1:5] 
    print(title.ljust(50),year,point.ljust(7),i)
    i=i+1
