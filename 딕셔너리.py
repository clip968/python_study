dic = {'apple':'사과', 'peach':'복숭아', 'banana':'바나나'}

print(dic)

for key in dic:
    print("%s => %s" % (key, dic[key]))
    
dic['grape'] = '포도'

print(dic)
dic.update({'orange':'오렌지', 'mandarin':'귤'})
print(dic)

print(dic.keys())
print(dic.values())