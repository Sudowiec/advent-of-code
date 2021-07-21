inp = list(map(int, input().split(" ")))
sum = 0
indx = 0

def rec():
    global indx
    global inp
    global sum
    sub_nodes = inp[indx]
    indx += 1
    metadata_entries = inp[indx]
    indx += 1
    for i in range(sub_nodes):
        rec()
    for i in range(metadata_entries):
        sum += inp[indx]
        indx += 1

indx = 0
def rectwo():
    global indx
    global inp
    nodes_list = []
    node_sum = 0
    sub_nodes = inp[indx]
    indx += 1
    metadata_entries = inp[indx]
    indx += 1
    if sub_nodes != 0:
        for i in range(sub_nodes):
            nodes_list.append(rectwo())
        for i in range(metadata_entries):
            m = inp[indx]
            indx += 1
            if m > 0 and m <= len(nodes_list):
                node_sum += nodes_list[m - 1]
    else:
        for i in range(metadata_entries):
            node_sum += inp[indx]
            indx += 1
    return(node_sum)
print(rectwo())