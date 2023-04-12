import random
import sys

if len(sys.argv) < 3 or sys.argv[1] == "" or sys.argv[2] == "":
    print("Not enough input arguments provided. Exiting the program...")
    sys.exit()
else:
    try:
        item_cnt = int(sys.argv[1])
    except ValueError:
        print("Argument 1 is not an integer. Exiting the program...")
        sys.exit()
    try:
        item_max_wt = int(sys.argv[2])
    except ValueError:
        print("Argument 2 is not an integer. Exiting the program...")
        sys.exit()

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

def sort_val(items):
    return sorted(items, key=lambda x: x.value, reverse=True)

def desc_value_items(items, max_wt):
    desc_val_items = []
    total_value = 0
    sorted_items = sort_val(items)
    for item in sorted_items:
        if item.weight <= max_wt:
            desc_val_items.append(item)
            max_wt -= item.weight
            total_value += item.value
    return desc_val_items, total_value

nIn = item_cnt
maxWtIn = item_max_wt
maxValIn = 50
items = gen_items(nIn, maxWtIn, maxValIn)
print(f"No. of Items: {len(items)}")
for item in items:
    print(f"Value: {item.value}, Weight: {item.weight}")


desc_val_items, total_value = desc_value_items(items, maxWtIn)
print(f"\nSolution 1: Take as many items as possible with highest value first\nTotal value: {total_value}")
for item in desc_val_items:
    print(f"Value: {item.value}, Weight: {item.weight}")
