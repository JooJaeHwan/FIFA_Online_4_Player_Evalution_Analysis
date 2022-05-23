import requests
import pandas as pd
# Nexon API Headers


season_url = "https://static.api.nexon.co.kr/fifaonline4/latest/seasonid.json"
data = requests.get(season_url)
season = data.json()
data = {}
id = []
name = []
for s in season:
    id.append(s["seasonId"])
    name.append(s["className"].split("(")[0])
data["id"] = id
data["name"] = name
result = pd.DataFrame(data)
result.loc[result["id"] == 212, "id"] = 203
result.loc[result["id"] == 234, "id"] = 224
result.to_csv("Season.csv")