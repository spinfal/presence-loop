import requests as r
#import random
import time as t
from termcolor import colored as cl
import sys, os

print(cl('lets get shwifty', 'green'))
token = input(cl('your token: ', 'white'))
check = r.get('https://discordapp.com/api/v8/users/@me/settings', headers={'Authorization': token})
if check.status_code != 200:
  print(cl('there was an error with that token\n', 'red') + str(check.content))
  sys.exit()
delay = input(cl('interval (leave blank for default): ', 'white'))
if delay == "":
  delay = 4
elif int(delay) < 1:
  print(cl('you cannot enter anything less than 1', 'red')) # i mean u can lol, just be careful /shrug
  t.sleep(3)
  os.system('python3 main.py')
limit = input(cl('include invisible (yes or no): ', 'white'))
if limit == 'yes':
  limit = 4
elif limit == 'no':
  limit = 3
else:
  print(cl('invalid choice', 'red'))
  t.sleep(3)
  os.system('python3 main.py')
print(cl('\nstarting...', 'cyan'))
t.sleep(2)

headers = {
  'Authorization': token,
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}

setstatus = ['online', 'idle', 'dnd', 'invisible']
choice = 0

while True:
  if choice == int(limit):
    choice = 0
  res = r.patch('https://discordapp.com/api/v8/users/@me/settings', json={"status": setstatus[choice]}, headers=headers)
  if res.status_code != 200:
    print(cl('\nan error has occured, please try again.\n', 'red') + str(res.content) + '\n')
    sys.exit()
  print('\033[H\033[J')
  print('status: ' + str(res.status_code) + cl('\nstatus set to: ' + setstatus[choice], 'green'))
  choice = choice + 1
  t.sleep(int(delay))