import requests
import json

token = input('Your Token : ')
app_name = input('Application name : ')
description = input('Application description : ')
redirect_uri = input('Redirect URI : ')

headers = {'Authorization': token}
payload = {
    'name': app_name,
    'description': description,
    'redirect_uris': [redirect_uri]
}
req = requests.post(url='https://discordapp.com/api/oauth2/applications', \
                   headers=headers,
                   json=payload)
if req.status_code != 201:
    print('Error :/')
    exit(1)

print('Storing bot details in {}.json'.format('app_name'))
with open('{}.json'.format('app_name'), 'w+') as f:
    f.write(req.text)

req = requests.post('https://discordapp.com/api/oauth2/applications/{}/bot'.format(req.json()['id']),
                    headers=headers,
                    json=""
                    )

if req.status_code != 200:
    print('Error :/')
    exit(1)

print('Storing application details in {}-bot.json'.format('app_name'))
with open('{}-bot.json'.format('app_name'), 'w+') as f:
    f.write(req.text)

print('Bye ! o/')
