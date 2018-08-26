from py2neo import Graph, Node, Relationship
graph = Graph("http://localhost:7474/", username="neo4j", password="da182681")
node1 = Node("Person", name="Kang")
node2 = Node(label="Person", name="Ko")

graph.create(node1)
graph.create(node2)

node1_to_node2 = Relationship(node1, "Call", node2)
node1_to_node2["count"] = 100
graph.create(node1_to_node2)
