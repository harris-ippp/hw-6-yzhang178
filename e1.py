import requests
from bs4 import BeautifulSoup


election_ad = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General"
resp = requests.get(election_ad)
soup = BeautifulSoup(resp.text, "html5lib")
election_item = soup.find_all('tr', "election_item")
ids = []
years = []
for row in election_item:
    year_td = row.find("td", "year")
    year = year_td.contents[0]
    election_id = row["id"]
    print(year, election_id.split("-")[-1])
