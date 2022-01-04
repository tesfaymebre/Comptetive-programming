from collections import OrderedDict
N = int(input())
items = OrderedDict()
for i in range(N):
    item_pri = input().split()
    itemType = ' '.join(item_pri[:len(item_pri)-1])
    if itemType not in items:
        items[itemType] = int(item_pri[len(item_pri)-1])
    else:
        items[itemType]+= int(item_pri[len(item_pri)-1])
for x in items:
    print(x,items[x])
