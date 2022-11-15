# defaultdict for Gnosis

import json
from collections import defaultdict

> save SAFE__addressBook from local storage into safe_v1.json
f = open('safe_v1.json')
safe_v1 = json.load(f)
v2 = defaultdict(dict)

for i in safe_v1:
  v2[str(i['chainId'])][str(i['address'])] = i['name']

> Copy to SAFE_v2__addressBook in local storage
print(json.dumps(v2))