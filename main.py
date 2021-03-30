import requests
import json
try:
    while True:
      print("=========本機資訊=========")
      local = requests.get("http://ip-api.com/json/")
      info = json.loads(local.text)
      print("主機IP：\t"+info["query"])
      print("所在城市：\t"+info["city"])
      print("所在國家：\t"+info["country"]+","+info["regionName"]+","+info["city"])
      print("當前時區\t"+info["timezone"])
      print("電信提供商ISP\t"+info["isp"])
      print("AS編號\t"+info["as"])
except EOFError:
    pass
