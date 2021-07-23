node = {"val": 0}
node["next"] = node
node["prev"] = node

zero = node
steps = 367

# for i in range(1, 50001):
#     for j in range(steps):
#         node = node["next"]
#     new_node = {"val": i}
#     new_node["next"] = node["next"]
#     node["next"]["prev"] = new_node
#     node["next"] = new_node
#     new_node["prev"] = node
#     node = new_node
#     if node["prev"]["val"] == 0:
#         print("az: " + str(i))
#     if i % 10000 == 0:
#         print(i)
# print(zero["next"]["val"])

p = 0
arr = [0]
for i in range(1, 50000001):
    p = (p + steps) % i
    # wstawiam i na poz p + 1
    p += 1
    if p == 1:
        print(i)
