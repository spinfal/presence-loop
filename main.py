import requests as r
#import random
import time as t
import sys, os

print('lets get shwifty')
token = input('your token: ')
check = r.get('https://discordapp.com/api/v8/users/@me/settings', headers={'Authorization': token})
if check.status_code != 200:
  print('there was an error with that token\n' + str(check.content))
  sys.exit()
delay = input('interval (leave blank for default): ')
if delay == "":
  delay = 2
elif int(delay) < 1:
  print('you cannot enter anything less than 1') # i mean u can lol, just be careful /shrug
  t.sleep(3)
  os.system('python3 main.py')
limit = input('include invisible (yes or no): ')
if limit == 'yes':
  limit = 4
elif limit == 'no':
  limit = 3
else:
  print('invalid choice')
  t.sleep(3)
  os.system('python3 main.py')
print('\nstarting...')
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
    print('\nan error has occured, please try again.\n' + str(res.content) + '\n')
    sys.exit()
  os.system('cls')
  print('status: ' + str(res.status_code) + '\nstatus set to: ' + setstatus[choice])
  choice = choice + 1
  t.sleep(int(delay))
