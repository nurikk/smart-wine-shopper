from parse import fetchData
from render import renderImage
# import requests

# URL = 'https://www.ishopchangi.com/WSHub/wsProduct.asmx/GetProductGroupByFilterEx'

# # -H 'cookie: ASP.NET_SessionId=itz2qqdh0sywgc4a4aoxw5qa; IPDetection=en-US; Language=en-US; _lastdetailRetrieval=Sun%20Sep%2002%202018%2011%3A45%3A05%20GMT%2B0800%20(Singapore%20Standard%20Time); productListSortOrder=popularity; productLoadPageSize=200; AWSALB=ic6YmXjA376SbrHZjVEQuX7SgnMFI9x2Sk0gvUA7On1e8lq5qjO+2D1V0lgcqePAaDBsjkjunCh1m0wXg+OlNkRewIhM0Fma+ju67tn+1fzwfisENJkoL2nCNgqX' 

# headers = {
#     "origin": "https://www.ishopchangi.com", 
#     "accept-encoding": "gzip, deflate, br", 
#     "accept-language": "ru,en-US;q=0.9,en;q=0.8", 
#     "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36", 
#     "content-type": "application/json", 
#     "accept": "application/json, text/javascript, */*; q=0.01", 
#     "referer": "https://www.ishopchangi.com/productlistings/wine-spirits-38/wine-204/red-wine-206?p=2", 
#     "authority": "www.ishopchangi.com", 
#     "x-requested-with": "XMLHttpRequest", 
#     "dnt": "1"
# }
# payload = {"categories":"206","brand":"","minPrice":0,"maxPrice":5000,"flightType":"departure|arrival|delivery|","filterBy":"","filterPageSize":"200","currentPageindex":"2","langType":"en-US","sortBy":"popularity","tagName":"","deliveryAvailable":""}


# req = requests.post(URL, data=payload)
# import pdb; pdb.set_trace()

if __name__ == '__main__':
    renderImage(fetchData(), '/tmp/img1.jpg')