from dataclasses import dataclass

from graph_db.data_elements.node_dc import Node


@dataclass(unsafe_hash=True)
class Edge:
    node1: Node
    node2: Node
    distance: float
