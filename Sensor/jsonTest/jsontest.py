import json
#JSONファイル読込
f = open('Temp-humi-data_2020060922.json', 'r')
json_dict = json.load(f)
print('json_dict:{}'.format(type(json_dict)))

#JSON データの変換
print('------ 辞書型から JSON形式の文字列へ変換 ------')
json_str = json.dumps(json_dict)
print('json_str:{}'.format(type(json_str)))
print('------ JSON形式の文字列から辞書型へ変換 ------')
json_dict2 = json.loads(json_str)
print('json_dict2:{}',format(type(json_dict2)))

#JSON データの書き込み
f2 = open('testWrite.json', 'w')
json.dump(json_dict2, f2)
