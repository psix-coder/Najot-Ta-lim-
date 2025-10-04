datas = [{'a':'a', 'price':20}, {'a':'b', 'price':30}]

# datas.sort()
# datas.sort(reverse=True)


# def a(arg):
#     return len(arg)

def a(arg:dict):
    
    return arg['price']

datas.sort(key=a)

print(datas)