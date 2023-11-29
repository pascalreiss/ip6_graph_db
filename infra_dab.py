"""Neo4j Dachsburg-Ring example."""
from typing import Dict, List, Tuple

import numpy as np
from neo4j import GraphDatabase

from graph_db.data_elements.bahnhof_enum import Bhf
from graph_db.data_elements.edge_dc import Edge
from graph_db.data_elements.edge_relation_enum import EdgeRelation
from graph_db.data_elements.node_dc import Node
from graph_db.data_elements.switch_item_enum import SwitchItem
from graph_db.db_api import bidirectional_edge, double_node, reset_db

w3_tp = Node(
    id="w3_id",
    ecos_id="3",
    switch_item=SwitchItem.WEICHE,
    name="w3",
    bhf=Bhf.DAB,
    coords=np.array([3, 3, 3]),
)


w_tps: List[Node] = [w3_tp]
double_nodes: Dict[str, Tuple[Node, Node]] = {}
query: List[str] = []

for w_tp in w_tps:
    cmd, nodes = double_node(w_tp)
    double_nodes[w_tp.name] = nodes
    query.append(cmd)

URI = "bolt://neo4j:7687"
USR = "neo4j"
PASSWD = "password"

driver = GraphDatabase.driver(URI, auth=(USR, PASSWD))

session = driver.session()

session.run(reset_db())

for cmd in query:
    session.run(cmd)

edge_w0_w1 = Edge(
    double_nodes["w0"][1], double_nodes["w1"][0], EdgeRelation.TRAIN_RAIL, 5
)

cmd = bidirectional_edge(edge_w0_w1)
session.run(cmd)
