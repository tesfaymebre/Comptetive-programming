"""
Task
You are the manager of a supermarket.
You have a list of  items together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence.

item_name = Name of the item.
net_price = Quantity of the item sold multiplied by the price of each item.
"""
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
