import requests

payload = {'username':'myusername', 'ip':'myip'}
url = 'http://challenges.enigmagroup.org/programming/1/index.php'

r = requests.get(url, auth=('myusername', 'enigmagrouppassword'))

r.cookies['mission'] = 'yes'
r.cookies['PHPSESSID'] = 'myphpsessid'
r.cookies['__cfduid'] = 'my__cfduid'

print r.text

r = requests.post(url, data=payload, cookies=r.cookies)

print r.text