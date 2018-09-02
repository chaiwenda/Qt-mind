from py2neo import Graph, Node, Relationship
"""
function :连接数据库
"""
# match(n)
# optional match(n)-[r]-()
# delete n,r

graph = Graph(
    "http://localhost:7474",
    username="neo4j",
    password="da182681"
)
a = Node(label = "company",name = "华为公司demo1")
a1 = Node(label = "company",name = "华为公司demo2")
a2 = Node(label = "company",name = "华为公司demo3")
a3 = Node(label = "company",name = "华为公司demo4")
b = Node(label = "Person",name = "任正非")
graph.create(a)
graph.create(a3)
graph.create(a1)
graph.create(a2)
graph.create(b)

re1 = Relationship(a,'CALL',a1)
re1['count'] = 1
re2 = Relationship(a,'CALL',a2)
re2['count'] = 2
re2 = Relationship(a2,'CALL',a3)
re2['count'] = 2
re3 = Relationship(a3,'CALL',b)
re3['count'] = 3
graph.create(re1)
graph.create(re2)
graph.create(re3)



