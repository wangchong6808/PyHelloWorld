#! /usr/bin/python3
# -*-coding:UTF-8-*-

import json

data = {'k1': 'v1', 'k2': 'v2'}
str = '{"key1":"value1", "key2":"value2"}'
jsonStr = json.dumps(data)

dic = json.loads(str)

print(jsonStr)

for k,v in dic.items():
    print(k, v)
