import requests

url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20140222'

payload = {
    'applicationId': '1068276949878974132',
    'keyword': 'プロテイン',
    'hits': 10,
    'sort': '+itemPrice',
}

r = requests.get(url, params=payload)

resp = r.json()
print("検索結果 =", resp['count'])
print('-'*40)

for i in resp['Items']:
    item = i['Item']
    print(item['itemName'])
    print(item['itemPrice'], 'yen')
