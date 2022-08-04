
from bs4 import BeautifulSoup
import requests , openpyxl
import numpy as np

#excel handler
excel=openpyxl.Workbook()
sheet=excel.active
sheet.title="TOP 250 imdb"
sheet.append(["Movie Rank","Movie Name","Year of Release","Rating"])


#catching data from site
url="https://www.imdb.com/chart/top/"
source= requests.get(url)
soup = BeautifulSoup(source.text , "html.parser")

movies=soup.find("tbody", class_="lister-list").find_all("tr")

for movie in movies:
    name=movie.find("td" , class_="titleColumn").a.text
    rank=movie.find("td" , class_="titleColumn").get_text(strip=True).split(".")[0]
    year=movie.find("td" , class_="titleColumn").span.text.strip("()")
    rate= movie.find("td" , class_="ratingColumn imdbRating").strong.text
    print(rank , name , year , rate)
    sheet.append([rank , name , year , rate])


excel.save("imdbtop.xlsx")    

    





