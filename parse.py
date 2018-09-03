import json
from pydash import pick, map_
from operator import itemgetter, attrgetter

import re


def fetchData():
    file_name = './data.json'
    data = json.loads(json.loads(open(file_name).read())['d'])
    items = data['Items']
    
    count = data['Count']
    
    keys = [
        'ProductGroupTitle',
        'Org_Disc_Price',
        'Org_Price'
    ]
    # import pdb; pdb.set_trace()
    return sorted(map_(items, lambda item:  pick(item, keys)), key = itemgetter('Org_Disc_Price'))


if __name__ == '__main__':
    data = fetchData()    
    print(data[:3])
    # import pdb; pdb.set_trace()
