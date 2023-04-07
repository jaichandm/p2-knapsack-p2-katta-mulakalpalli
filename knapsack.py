import random

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def gen_items(n, max_wt, max_val):
    items = []
    for i in range(n):
        value = random.randint(1, max_val)
        weight = random.randint(1, max_wt)
        item = Item(value, weight)
        items.append(item)
    return items

nIn = 10
maxWtIn = 100
maxValIn = 50
items = gen_items(nIn, maxWtIn, maxValIn)
for item in items:
    print(f"Value: {item.value}, Weight: {item.weight}")
