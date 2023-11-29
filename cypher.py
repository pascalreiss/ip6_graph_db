from typing import List
import time
from enum import StrEnum
import numpy as np
from dataclasses import dataclass

class Element(StrEnum):
    weiche = 'Weiche'

class Bhf(StrEnum):
    dab = 'Dachsburg'
    ens = 'Ensikon'
    cha = 'Charrat'
    ger = 'Gerau'
    fus = 'Fusio'
    blo = 'Bloney'

@dataclass(unsafe_hash=True)
class Node:
    id: str
    ecos_id: str
    element: Element
    name: str
    bhf: Bhf
    coords: np.ndarray

@dataclass(unsafe_hash=True)
class Edge:
    node1: Node
    node2: Node
    distance: float

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
        name = f"{time.time_ns()}_cypher"

    res: str
    res += 'MATCH (n) \n DETACH DELETE n; \n CREATE'

    for node in nodes:
        res += string_double_vertex(node)

    res += "\n"

    for edge in edges:
        res += string_edge(edge)

    fd = open(name, "x", encoding="utf-8")
    fd.write(res)
    fd.close()

    return res
