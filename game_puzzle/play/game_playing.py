import sys

class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children

#to pop elements from tree_string and form a parent node
def build_node(tree_string):
    nodes_list = []
    ch = tree_string.pop()
    while (ch != '('):
        nodes_list.append(ch)
        ch = tree_string.pop()
    nodes_list.reverse()
    return Node(0, nodes_list)

# To parse tree into a list.
def parse_tree_to_list(root, list):
    if root.children == None:
        list.append(str(root.value))
        return
    list.append('(')
    for child in root.children:
        parse_tree_to_list(child, list)
    list.append(')')

# To parse list into a tree.
def parse_list_to_tree(list):
    tree_string = []
    nums = "0123456789"
    i = 0
    while i < len(list):
        # print tree_string
        char = list[i]
        if char == '(':
            tree_string.append(char)
        if char == ')':
            tree_string.append(build_node(tree_string))
        if char == '-':
            sign = char
            j = i + 1
            number = ""
            while list[j] in nums:
                number += list[j]
                j += 1
            i = j - 1
            number = sign + number
            node = Node(int(number))
            tree_string.append(node)
        if char in nums:
            number = char
            j = i + 1
            while list[j] in nums:
                number += list[j]
                j += 1
            i = j - 1
            node = Node(int(number))
            tree_string.append(node)
        i += 1
    return tree_string.pop()

# To classify a cut properly
def format_cut(node):
    list = []
    parse_tree_to_list(node,list)
    list1 = " ".join(list)
    return list1

# Helper to Minimax - returns min among children
def min_value(root, alpha = None, beta = None):
    if root.children == None:
        return root.value
    value = sys.maxsize
    for node in root.children:
        value = min(value, max_value(node, alpha, beta))
        if alpha != None:
            if value <= alpha:
                list1 = format_cut(node)
                list2 = format_cut(root)
                print("cut after ", list1, " in subtree ", list2)
                return value
            beta = min(beta, value)
    root.value = value
    return value


# Helper to Minimax - returns max among children
def max_value(root, alpha = None, beta = None):
    if root.children == None:
        return root.value
    value = (-1)*sys.maxsize
    for node in root.children:
        value = max(value, min_value(node, alpha, beta))
        if alpha != None:
            if value >= beta:
                list1 = format_cut(node)
                list2 = format_cut(root)
                print("cut after ", list1, " in subtree ", list2)
                return value
            alpha = max(alpha, value)
    root.value = value
    return value


# MINI-MAX algorithm
def minimax(root):
    return max_value(root)

# ALPHA-BETA algorithm
def alpha_beta(root):
    return max_value(root, (-1) * sys.maxsize, sys.maxsize)

# print the path in case of MiniMax Algorithm
def print_minimax(root, list):
    if root.children == None:
        return
    count = 0;
    for node in root.children:
        count += 1
        if node.value == root.value:
            list.append(count)
            print_minimax(node, list)

if __name__ == '__main__':
#MINIMAX 
    tree = parse_list_to_tree("((4 (7 9 8) 8) (((3 6 4) 2 6) ((9 2 9) 4 7 (6 4 5))))")
    print("\n~~~~~~~~~~~~~~~  mini - max  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    minimax_value = minimax(tree)
    print("maximum value : ", minimax_value)
    list = []
    print_minimax(tree, list)
    print("path : ", list)
#ALPHA-BETA
    tree = parse_list_to_tree("((4 (7 9 8) 8) (((3 6 4) 2 6) ((9 2 9) 4 7 (6 4 5))))")
    print("\n~~~~~~~~~~~~~~~  alpha - beta  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("\nmaximum value : ", alpha_beta(tree))

#    tree = parse_list_to_tree("(((1 4) (3 (5 2 8 0) 7 (5 7 1)) (8 3)) (((3 6 4) 2 (9 3 0)) ((8 1 9) 8 (3 4 ))))")
#    print("\n~~~~~~~~~~~~~~~  mini - max  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
#    minimax_value = minimax(tree)
#    print("maximum value : ", minimax_value)
#    list = []
#    print_minimax(tree, list)
#    print("path : ", list)
#    tree = parse_list_to_tree("(((1 4) (3 (5 2 8 0) 7 (5 7 1)) (8 3)) (((3 6 4) 2 (9 3 0)) ((8 1 9) 8 (3 4 ))))")
#    print("\n~~~~~~~~~~~~~~~  alpha - beta  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
#    print("\nmaximum value : ", alpha_beta(tree))
#
#
#    tree = parse_list_to_tree("(5 (((4 7 -2) 7) 6))")
#    print("\n~~~~~~~~~~~~~~~  mini - max  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
#    minimax_value = minimax(tree)
#    print("maximum value : ", minimax_value)
#    list = []
#    print_minimax(tree, list)
#    print("path : ", list)
#    tree = parse_list_to_tree("(5 (((4 7 -2) 7) 6))")
#    print("\n~~~~~~~~~~~~~~~  alpha - beta  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
#    print("\nmaximum value : ", alpha_beta(tree))
#
#    tree = parse_list_to_tree("((8 (7 9 8) 4) (((3 6 4) 2 1) ((6 2 9) 4 7 (6 4 5))))")
#    print("\n~~~~~~~~~~~~~~~  mini - max  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
#    minimax_value = minimax(tree)
#    print("maximum value : ", minimax_value)
#    list = []
#    print_minimax(tree, list)
#    print("path : ", list)
#    tree = parse_list_to_tree("((8 (7 9 8) 4) (((3 6 4) 2 1) ((6 2 9) 4 7 (6 4 5))))")
#    print("\n~~~~~~~~~~~~~~~  alpha - beta  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
#    print("\nmaximum value : ", alpha_beta(tree))
#
#    tree = parse_list_to_tree("(((1(4 7)) (3 ((5 2) (2 8 9) 0 -2) 7 (5 7 1)) (8 3)) (((8 (9 3 2) 5) 2 (9 (3 2) 0)) ((3 1 9) 8 (3 4))))")
#    print("\n~~~~~~~~~~~~~~~  mini - max  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
#    minimax_value = minimax(tree)
#    print("maximum value : ", minimax_value)
#    list = []
#    print_minimax(tree, list)
#    print("path : ", list)
#    tree = parse_list_to_tree("(((1(4 7)) (3 ((5 2) (2 8 9) 0 -2) 7 (5 7 1)) (8 3)) (((8 (9 3 2) 5) 2 (9 (3 2) 0)) ((3 1 9) 8 (3 4))))")
#    print("\n~~~~~~~~~~~~~~~  alpha - beta  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
#    print("\nmaximum value : ", alpha_beta(tree))


