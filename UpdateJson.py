import json

def JsonOpen(path):
    with open(path, 'r', encoding='UTF-8') as fr:
        data = json.loads(fr.read())
    return data

def JsonUpdate(data,newdata):
    data.append(newdata)
    return data

def JsonStore(data):
    data= json.dumps(data, ensure_ascii=False)
    with open('repurchases.json', 'w', encoding='UTF-8') as f:
        f.write(data)
