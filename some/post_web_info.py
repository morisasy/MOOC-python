
import requests
pload = {'username':'olivia','password':'123'}
r = requests.post('https://httpbin.org/post',data = pload)
print(r.json())
r_dictionary= r.json()
print(r_dictionary['form'])
