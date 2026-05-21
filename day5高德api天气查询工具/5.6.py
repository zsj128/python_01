import json
u={'name':'李','age':30,'skills':["Python","Java"]}
j=json.dumps(u,ensure_ascii=True,indent=0,sort_keys=True)
print(j)
print(json.loads(j))