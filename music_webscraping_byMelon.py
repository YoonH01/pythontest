import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/index.htm"
headers = {"User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

day = soup.find("span", attrs={"class":"yyyymmdd"}).get_text().replace("\n","")
ranks = soup.find_all("tr", attrs={"class":"lst50"})

if __name__ == "__main__":
    print("="*10,f"{day} Melon Top 50","="*10)

    for index, rank in enumerate(ranks):
        top = rank.find("div", attrs={"class":"ellipsis rank01"}).get_text().strip()
        print(f"{index + 1} : {top}")