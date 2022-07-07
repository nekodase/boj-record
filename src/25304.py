total = int(input())
n_inputs = int(input())
shoplist = []
for n in range(n_inputs):
    price, count = map(int, input().split())
    shoplist.append((price, count))

table = ('No', 'Yes')
for item_price, item_count in shoplist:
    total = total - item_price*item_count

print(table[total == 0])