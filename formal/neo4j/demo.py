# date:2018/9/2 15:39
# -*- coding: utf-8 -*-
#author;cwd
"""
function:
"""
from py2neo import Graph, Node, Relationship
import random
x1 = [1,2,3,4,5,6,7]
queue = []
x_root = "root"
# re1 = Relationship(a = ,'CALL',a1)
# start
queue.append(x_root)
while len(queue) > 0:
    startNode = queue.pop(0)
    a = Node("company", name = startNode)
    b_lists = []  #候选词列表下标
    for item in range(0, 3, 1):
        try:
            index = random.randint(0, len(x1) - 1)
            print("index = " + str(index))
            b_lists.append(x1[index])
            queue.append(x1[index])
            x1.pop(index)
            print("queue = ", end="")
            print(queue)
        except ValueError:
            print("值不足3个")
            break
    print("候选词列表", end="")
    print(b_lists)
    for item in b_lists:
        item = Node("company", name=item)
        rel = Relationship(a, 'CALL', item)
        print(rel)



