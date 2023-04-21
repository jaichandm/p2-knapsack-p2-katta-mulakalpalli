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
    total_weight = 0
    sorted_items = sort_val(items)
    for item in sorted_items:
        if item.weight <= max_wt:
            desc_val_items.append(item)
            max_wt -= item.weight
            total_weight += item.weight
            total_value += item.value
    return desc_val_items, total_value, total_weight


def asc_wt_items(items, max_wt):
    asc_wt_items = []
    total_val = 0
    total_wt = 0
    sorted_items = sorted(items, key=lambda x: x.weight)
    for item in sorted_items:
        if item.weight <= max_wt:
            asc_wt_items.append(item)
            max_wt -= item.weight
            total_wt += item.weight
            total_val += item.value
    return asc_wt_items, total_val, total_wt

def sort_ratio_items(items):
    return sorted(items, key=lambda item: item.value/item.weight, reverse=True)

nIn = item_cnt
maxWtIn = item_max_wt
maxValIn = 50
items = gen_items(nIn, maxWtIn, maxValIn)
print(f"No. of Items: {len(items)}")
for item in items:
    print(f"Value: {item.value}, Weight: {item.weight}")


def desc_ratio_items(items, max_weight):
    sorted_items = sort_ratio_items(items)
    sorted_ratio_items = []
    total_value = 0
    total_weight = 0
    for item in sorted_items:
        if total_weight + item.weight <= max_weight:
            sorted_ratio_items.append(item)
            total_value += item.value
            total_weight += item.weight
    return sorted_ratio_items, total_value, total_weight

def knapsack(items, W):
    n = len(items)
    K = [[0 for x in range(W+1)] for x in range(n+1)]

    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif items[i-1].weight <= w:
                K[i][w] = max(items[i-1].value + K[i-1][w-items[i-1].weight], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]


desc_val_items, total_value, total_weight = desc_value_items(items, maxWtIn)
print(f"\nSolution 1: Using decreasing Value\nTotal value: {total_value}\nTotal weight: {total_weight}")
for item in desc_val_items:
    print(f"Value: {item.value}, Weight: {item.weight}")


asc_weight_items, total_value, total_weight = asc_wt_items(items, maxWtIn)
print(f"\nSolution 2: Using increasing Weight\nTotal value: {total_value}\nTotal weight: {total_weight}")
for item in asc_weight_items:
    print(f"Value: {item.value}, Weight: {item.weight}")

dec_ratio_items, total_value, total_weight = desc_ratio_items(items, maxWtIn)
print(f"\nSolution 3: Using decreasing Ratio(Value/Weight)\nTotal value: {total_value}\nTotal weight: {total_weight}")
for item in dec_ratio_items:
    print(f"Value: {item.value}, Weight: {item.weight}")
