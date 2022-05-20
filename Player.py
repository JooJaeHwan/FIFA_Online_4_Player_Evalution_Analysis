import requests
import pandas as pd
# Nexon API Headers
headers = {'Authorization' : 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50X2lkIjoiMTg0OTE3MjMxIiwiYXV0aF9pZCI6IjIiLCJ0b2tlbl90eXBlIjoiQWNjZXNzVG9rZW4iLCJzZXJ2aWNlX2lkIjoiNDMwMDExNDgxIiwiWC1BcHAtUmF0ZS1MaW1pdCI6IjUwMDoxMCIsIm5iZiI6MTY0OTg1NDI3MiwiZXhwIjoxNjY1NDA2MjcyLCJpYXQiOjE2NDk4NTQyNzJ9.qE--Kwy2lznUUHyGgZxkR2oZLdHN73VWmzqNbFstDI4'} 
player_url = "https://static.api.nexon.co.kr/fifaonline4/latest/spid.json"
data = requests.get(player_url, headers=headers)
player = data.json()
data = {}
id = []
name = []
class_id = []
for p in player:
   id.append(p["id"])
   name.append(p["name"])
   class_id.append(p["id"]//1000000)
data["id"] = id
data["이름"] = name
data["class_id"] = class_id
df = pd.DataFrame(data)
df = df.loc[(df["class_id"] != 300) | (df["class_id"] != 317) | (df["class_id"] != 318) | (df["class_id"] != 319) | (df["class_id"] != 320) | (df["class_id"] != 500) | (df["class_id"] != 501) | (df["class_id"] != 502) | (df["class_id"] != 503) | (df["class_id"] != 506) | (df["class_id"] != 508)]
df.loc[df["class_id"]==212, "class_id"] = 203
df.loc[df["class_id"]==234, "class_id"] = 224
df.reset_index(drop=True, inplace=True)
df.to_csv("Player.csv")