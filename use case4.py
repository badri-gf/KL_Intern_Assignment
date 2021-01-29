import json
with open('python files.txt', 'r') as f:
    list1 = json.loads(f.read())
    print(list1)