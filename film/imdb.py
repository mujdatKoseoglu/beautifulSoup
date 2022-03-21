import requests
from bs4 import BeautifulSoup

class Bea:

    list1=[]
    list2=[]

    def __init__(self):
        url="https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"
        html=requests.get(url).content
        soup=BeautifulSoup(html,"html.parser")
        self.list1=soup.find("tbody",{"class":"lister-list"}).find_all("tr")

    def find(self):
        
        for tr in self.list1:
            filmname=tr.find("td",{"class":"titleColumn"}).find("a").text
            year=tr.find("td",{"class":"titleColumn"}).find("span").text.strip("()")
            point=tr.find("td",{"class":"imdbRating"}).find("strong")
            point = str(point).split('<strong title=')[-1][1:5]
            
            self.list2.append((0, filmname, year, point))
        return self.list2



