import requests
import hashlib

url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'
res = requests.get(url)


print(hashlib.sha1('123'.encode('utf-8')).hexdigest())

class CheckPassword():
  pass