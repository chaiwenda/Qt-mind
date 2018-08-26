from py2neo import Graph, Node, Relationship
"""
function :连接数据库
"""

class database:
    # initialize parm
    def __init__(self, passmsg):
        self.passmsg = passmsg
        self.graph = Graph(password=self.passmsg)

    # Create a node
    def createNode(self, labe, nameNode):
        node = Node(labe, name=nameNode)
        self.graph.create(node)

    # Create relationships and their attributes
    def createRelationship(self, a, labe, b):
        re = Relationship(a, labe, b)
        self.graph.create(re)

    # Query the node and its attributes

    # Query the node and its subtree

    # Query the minimum path between two nodes


