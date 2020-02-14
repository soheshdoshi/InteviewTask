import random


class Node:
    def __init__(self, value):
        self.key = value
        self.right = self.left = None


def insertnode(rootnode, data):
    q = []
    q.append(rootnode)
    while len(q):
        temp = q[0]
        q.pop(0)
        if temp.left == None:
            temp.left = Node(data)
            break
        else:
            q.append(temp.left)
        if temp.right == None:
            temp.right = Node(data)
            break
        else:
            q.append(temp.right)


def createTree(levelarr, n):
    root = Node(levelarr[0])
    for i in range(1, n):
        insertnode(root, levelarr[i])
    return root

def checksum(tree_node, sum_value, st, path_list):
    if tree_node is None:
        return path_list
    st.append(tree_node.key)
    if tree_node.left == None and tree_node.right == None:
        if sum(st) == sum_value:
            path_list.append([i for i in st])
    checksum(tree_node.left, sum_value, st, path_list)
    checksum(tree_node.right, sum_value, st, path_list)
    st.pop()
    return path_list


depth = int(input("Enter depth of tree:-"))
sumation_value = int(input("Enter Summation value for that:"))
arr_lenth = (2 ** depth) - 1
node_arr = random.sample(range(1, 100), arr_lenth)#[1,2,3,2,2,1,7]
print(node_arr)
tree = createTree(node_arr, arr_lenth)
path = checksum(tree, sumation_value, [], [])
if len(path) > 0:
    print(path)
else:
    print("No Possible Path.")







