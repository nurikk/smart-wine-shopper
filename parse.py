import json

import requests


def fetchData():
    file_name = './data.json'
    data = json.loads(json.loads(open(file_name).read())['d'])
    return data


def fetchData2():
    headers = {
        "origin": "https://www.ishopchangi.com",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "ru,en-US;q=0.9,en;q=0.8",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        "content-type": "application/json",
        "accept": "application/json, text/javascript, */*; q=0.01",
        "referer": "https://www.ishopchangi.com/productlistings/wine-spirits-38/wine-204/red-wine-206?p=2",
        "authority": "www.ishopchangi.com",
        "x-requested-with": "XMLHttpRequest",
        "dnt": "1"
    }
    payload = {
        "categories": '|'.join(["206"]),
        "brand": "",
        "minPrice": 0,
        "maxPrice": 200,
        "flightType": '|'.join(["departure"]), # departure arrival delivery
        "filterBy": "",
        "filterPageSize": "200",
        "currentPageindex": "1",
        "langType": "en-US",
        "sortBy": "popularity",
        "tagName": "",
        "deliveryAvailable": ""
    }

    URL = 'https://www.ishopchangi.com/WSHub/wsProduct.asmx/GetProductGroupByFilterEx'
    req = requests.post(URL, data=json.dumps(payload), headers=headers)
    data = json.loads(req.json()['d'])
    print('Items: {0}'.format(data.get('Count', 0)))
    return data.get('Items', [])


if __name__ == '__main__':
    data = fetchData2()
    print(data[:3])
