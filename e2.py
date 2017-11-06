import requests
from bs4 import BeautifulSoup


url = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General"
rest = requests.get(url)
soup = BeautifulSoup(rest.text, "html5lib")
election_item = soup.find_all('tr', "election_item")
election_ids = []
years = []
for row in election_item:
    year_td = row.find("td", "year")
    year = year_td.contents[0]
    years.append(year)
    election_id = row["id"]
    election_ids.append(election_id.split("-")[-1])


for i in range(len(years)):
    fp = open("president_general_%s.csv" % years[i], "w")
    rest = requests.get("http://historical.elections.virginia.gov/elections/download/%s/precincts_include:0/" % election_ids[i])
    fp.write(rest.text)
    fp.close()
