# date:2018/9/2 12:21
# -*- coding: utf-8 -*-
#author;cwd
"""
function:
"""
#coding:gbk
from py2neo import Graph, Node, Relationship, data


class Select(object):
    def __init__(self, pd, path):
        self.pd = pd
        self.NodeLists = []
        self.path = path
        self.db = Graph("http://localhost:7474/", username="neo4j", password=self.pd)
    def Select(self, str_in):  # 模糊搜索
        data1 = self.db.run("MATCH (n)where n.name=~'.*" + str_in + ".*'  RETURN n.name LIMIT 25").data()
        for i in data1:
            str1 = i['n.name']
            # print(str1)
            self.NodeLists.append(str1)
        return self.NodeLists
    def Select_one(self, str_in):  # 精确
        data_node = self.db.run("match(n{name:'"+str_in+"'})  RETURN n.name, n.Credit_url, n.corporate, n.direction, n.location, n.website LIMIT 25").data()
        return data_node
    def Select_one_name(self, str_in):  # 精确
        data_node = self.db.run("match(n{name:'"+str_in+"'})  RETURN n.name LIMIT 25").data()
        return data_node
    def Select_Father_Node(self, str1):  # 搜索父亲节点
        data2 = self.db.run("MATCH (n{name:'"+str1+"'})<-[]-(a) return a").data()
        return data2
    def Select_Children_Node(self, str1):  # 搜索孩子节点
        data3 = self.db.run("MATCH (n{name:'" + str1 + "'})-[]->(b) return b.name, b.Credit_url, b.corporate, b.direction, b.location, b.website").data()
        return data3
    def Select_Children_Node_Name(self, str1):  # 搜索孩子节点名字
        data4 = self.db.run("MATCH (n{name:'" + str1 + "'})-[]->(b) return b.name").data()
        return data4
    def json_file_done(self):
        line = ''
        with open(self.path, 'r') as f:
            line = f.read()
            line = line.replace('n.', '').replace('b.', '')
            f.close()
        with open(self.path, 'w') as f:
            f.write(line)
            f.close()
    def subgraph(self, root_node_name):
        queue = []  # 节点队列
        queue_names = []  # 节点名字队列
        queue.append(self.Select_one(search_node_name))
        queue_names.append(root_node_name)
        if len(queue_names) > 0:
            children_Lists = []  # 孩子节点列表
            start = queue[0]
            node_Lists = self.Select_Children_Node(queue_names[0])
            node_Lists_names = self.Select_Children_Node_Name(queue_names[0])
            startNode = queue[0][0]
            startNode['children'] = []
            queue_names.pop(0)
            if len(node_Lists) > 0:
                for item1 in node_Lists_names:
                    queue_names.append(item1)
                for item2 in node_Lists:  # 孩子节点列表
                    queue.append(item2)
                    children_Lists.append(item2)
                    endNode = item2
                    endNode['children'] = []
                    startNode['children'].append(endNode)
        print("str=")
        print(startNode)
        with open(self.path, 'w') as f:
            f.write(str(startNode))
            f.close()
        self.json_file_done()
        return startNode




if __name__ == '__main__':
    search_node_name = "华为技术有限公司"
    pd = "da182681"
    path = './neo4j/data1.json'
    node_Search = Select(pd, path)
    node3 = node_Search.subgraph(search_node_name)


