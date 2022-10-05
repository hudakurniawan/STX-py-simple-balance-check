#simple STX balance check
import requests
import json
import datetime

server = 'https://stacks-node-api.mainnet.stacks.co/v2/accounts/'
ts = datetime.datetime.now()

user = input('STX Wallet Address: ')

#GET data
data = requests.get(server+user)
load = json.loads(data.content)
balance = load['balance']
balance = int(balance, base=16)/1000000

print(ts)
print(balance,' STX')
