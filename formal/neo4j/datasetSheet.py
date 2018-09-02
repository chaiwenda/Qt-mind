# date:2018/8/28 9:22
# -*- coding: utf-8 -*-
#author;cwd
import openpyxl
from py2neo import Graph, Node, Relationship
import random

"""
function: 读取excel表格并随机构建关系存入数据库
"""
j = 3  # start index
rootSrc_excel = "./simple.xlsx"

wb = openpyxl.load_workbook(rootSrc_excel, )
sheet = wb.get_sheet_by_name("Sheet1")
graph = Graph(password='da182681')
node_lists = []
re_lists = []
for item in range(3, 100, 1):
    node = "node_" + str(item)
    node_lists.append(node)
print(node_lists)

for item in range(3, 100, 1):
    node_lists[item - 3]= Node("company", name=sheet["A" + str(item)].value.strip().strip('/n'), corporate = sheet["B" + str(item)].value,
                website = sheet["C" + str(item)].value, Credit_url = sheet["D" + str(item)].value,
                direction = sheet["E" + str(item)].value, location = sheet["F" + str(item)].value)
    graph.create(node_lists[item-3])
print(len(node_lists))
print(type(node_lists))
    # graph.create(node)
queue = []

x_root = node_lists[0]
node_lists.pop(0)
# start
queue.append(x_root)
while len(queue) > 0:
    startNode = queue.pop(0)
    a = startNode
    b_lists = []  #候选词列表下标
    for item in range(0, 3, 1):
        try:
            index = random.randint(0, len(node_lists) - 1)
            print("index = " + str(index))
            b_lists.append(node_lists[index])
            queue.append(node_lists[index])
            node_lists.pop(index)
            print("queue = ", end="")
            print(queue)
        except ValueError:
            print("值不足3个")
            break
    print("候选词列表", end="")
    print(b_lists)
    for item in b_lists:
        rel = Relationship(a, 'call', item)
        print(rel)
        graph.create(rel)
# 删除数据库
# match(n)
# optional match(n)-[r]-()
# delete n,r


