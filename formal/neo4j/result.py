#coding:gbk
from py2neo import Graph, Node, Relationship, data
def Select(str_in):
    db = Graph("http://localhost:7474/", username="neo4j", password="da182681")
    data1 = db.run("MATCH (n)where n.name=~'.*"+str_in+".*'  RETURN n.name LIMIT 25").data()
    print(data1)
    for i in data1:
        str1 = i['n.name']
        print(str1)
        data2 = db.run("MATCH (n{name:'"+str1+"'})<-[]-(a) return a.name,a.time,a.address").data()
        #print(data2)
        for i1 in data2:
            print(i1)
        data3 = db.run("MATCH (n{name:'" + str1 + "'})-[]->(b) return b.name,b.id,b.address").data()
        #print(data3)
        for i2 in data3:
            print(i2)

Select("华为公司")








