from bs4 import BeautifulSoup
import requests
from data import Data
from bson.objectid import ObjectId
from datetime import date

today = date.today()




drive = requests.get("https://www.abcbourse.com/marches/cryptomonnaies")
print(drive)

if drive.ok:
    soup = BeautifulSoup(drive.text, "lxml")
    all_td = soup.find_all('tr', {"class": "alri"})
    for i in all_td:
        d = {}
        i_split = i.text.split("\n")
        d["_id"] = ObjectId()
        d["date"] = str(today)
        d["Nom"] = i_split[1]
        d["Dernier cours(USD)"] = float(i_split[2].replace(",","."))
        d["Dernier cours(EUR)"] = float(i_split[3].replace(",","."))
        d["Variation jour"] = float(i_split[4].replace(",",".").replace("%",""))
        d["Variation 1 an"] = float(i_split[5].replace(",",".").replace("%",""))

        print(d)
        Data.insert(d)


