import requests

res = requests.post("http://127.0.0.1:3000/api/library/3",json={"name":"The Gadfly","id":456})
res = requests.post("http://127.0.0.1:3000/api/library/4",json={"name":"One Hundred Years of Solitude","id":100})
res = requests.delete("http://127.0.0.1:3000/api/library/2")
res = requests.put("http://127.0.0.1:3000/api/library/1",json={"name":"Little Women","id":143})
print(res.json())


