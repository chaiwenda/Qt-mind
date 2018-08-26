from py2neo import Graph, Node, Relationship
"""
function :连接数据库
"""
x = "da182681"

graph = Graph(password=x)

a = Node("person","father", name="hank")
graph.create(a)
a.update_labels("aaa")
graph.create(a)