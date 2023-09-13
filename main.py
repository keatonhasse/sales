import requests

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0'
}
url = 'https://redsky.target.com/redsky_aggregations/v1/web/pdp_client_v1?key=9f36aeafbe60771e321a7cc95a78140772ab3e96&tcin=14151826&pricing_store_id=61'
response = requests.get(url, headers=headers)
print(response)
data = response.json()
print(data['data']['product']['price'])
