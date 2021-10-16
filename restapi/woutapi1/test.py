import requests
 
start_url='http://127.0.0.1:8000/'
End_url='MixinCBV/'
respo = requests.get(start_url+End_url)
resp = requests.post(start_url+End_url) #this works only if we disable post method
res = requests.put(start_url+End_url) #put =update ,patch =patially update
re = requests.delete(start_url+End_url)


print(('-'*50))
print(respo.json())  #run this script in another terminal otherwise it wont work
print(resp.json())
print(res.json())
print(re.json())
#data=respo.json()
# print(data['ename'])
# print(data['esal'])

# for k,v in respo.items():
#     print(k,v)
