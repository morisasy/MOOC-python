import requests
receive = requests.get('https://imgs.xkcd.com/comics/making_progress.png')
ploads = {'things':2,'total':25}
r = requests.get('https://httpbin.org/get',params=ploads)
print(r.text)
print(r.url)

print(r.headers)
print(r.headers['Content-Type'])
print(r.text)
