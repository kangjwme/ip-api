import requests
import json

key = input("請輸入ipinfo.io中所提供的金鑰")

print("=========本機資訊=========")

local = requests.get("https://ipinfo.io/?token=%s" % (key))
info = json.loads(local.text)

print("主機位置：\t"+info["ip"])
print("主機名稱：\t"+info["hostname"])
print("所在城市：\t"+info["city"])
print("所在國家：\t"+info["region"]+","+info["country"])
print("電信組織\t"+info["org"])
print("當前時區\t"+info["timezone"])
