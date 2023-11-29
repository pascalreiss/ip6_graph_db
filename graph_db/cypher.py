from typing import List
from uuid import uuid4

from graph_db.data_elements.edge_dc import Edge
from graph_db.data_elements.node_dc import Node


def string_double_vertex(node: Node) -> str:
    res = f"({node.id}_1:{node.element.name} {{name:'{node.name}', ecos_id: '{node.ecos_id}', bhf: '{node.bhf.name}', x:{node.coords[0]}, y:{node.coords[1]}, z:{node.coords[2]}}}),\n"
    res += f"({node.id}_2:{node.element.name} {{name:'{node.name}', ecos_id: '{node.ecos_id}', bhf: '{node.bhf.name}', x:{node.coords[0]}, y:{node.coords[1]}, z:{node.coords[2]}}}),\n"
    res += f"({node.id}_1)-[:DOUBLE_VERTEX]->({node.id}_2),\n"
    res += f"({node.id}_2)-[:DOUBLE_VERTEX]->({node.id}_1),\n\n"
    return res


def string_edge(edge: Edge) -> str:
    res = f"({edge.node1.id}_2)-[:LEADS_TO {{distance:{edge.Distance}}}]->({edge.node2.id}_1),\n"
    res += f"({edge.node2.id}_1)-[:LEADS_TO {{distance:{edge.Distance}}}]->({edge.node1.id}_2),\n"


def create_cypher(nodes: List[Node], edges: List[Edge], name: str) -> str:
    if not name:
        name = f"{str(uuid4())}.cypher"

    res: str
    res += "MATCH (n) \n DETACH DELETE n; \n CREATE"

    for node in nodes:
        res += string_double_vertex(node)

    res += "\n"

    for edge in edges:
        res += string_edge(edge)

    fd = open(name, "x", encoding="utf-8")
    fd.write(res)
    fd.close()

    return res
