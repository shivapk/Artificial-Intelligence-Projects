#!/usr/bin/python

import sys

def min_value(tree_list):
    if isinstance(tree_list, list):
        temp = sys.maxsize
        for sub_list in tree_list:
            temp = min(temp, max_value(sub_list))
        return temp
    else:
        return tree_list

def max_value(tree_list):
    if isinstance(tree_list, list):
        temp = (-1)*sys.maxsize
        for sub_list in tree_list:
            temp = max(temp, min_value(sub_list))
        return temp
    else:
        return tree_list

def min_value_ab(tree_list, alpha, beta):
    if isinstance(tree_list, list):
        temp = sys.maxsize
        for sub_list in tree_list:
            temp = min(temp, max_value_ab(sub_list, alpha, beta))
            if temp <= alpha:
                print("min cut")
                return temp
            else:
                beta = min(beta, temp)
        return temp
    else:
        return tree_list

def max_value_ab(tree_list, alpha, beta):
    if isinstance(tree_list, list):
        temp = (-1)*sys.maxsize
        for sub_list in tree_list:
            temp = max(temp, min_value_ab(sub_list, alpha, beta))
            if temp >= beta:
                print("max cut")
                return temp
            else:
                alpha = max(alpha, temp)
        return temp
    else:
        return tree_list

def alpha_beta(tree_list):
    print(max_value_ab(tree_list, (-1)*sys.maxsize , sys.maxsize))

def minimax(tree_list):
    print(max_value(tree_list))

if __name__ == '__main__':
    tree_list = [[4, [7, 9, 8], 8], [[[3, 6, 4], 2, 6], [[9, 2, 9], 4, 7, [6, 4, 5]]]]
    minimax(tree_list)
    alpha_beta(tree_list)
