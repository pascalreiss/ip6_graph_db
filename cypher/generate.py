from typing import List
import cypher.node as node
import cypher.edge as edge
import time


def generate_create_file(nodes: List[node.Node], edges: List[edge.Edge], name: str,) -> str:
    if not name:
        name = f"{time.time_ns()}_cypher"

    res: str
    res += 'MATCH (n) \n DETACH DELETE n; \n CREATE'
    for node in nodes:
        res += f"({node.id}_1:{node.type.name} {{id:'{node.id}', ECoS:'{node.ECoS_id}', coords:{node.coords}}}),\n"
        res += f"({node.id}_2:{node.type.name} {{id:'{node.id}', ECoS:'{node.ECoS_id}', coords:{node.coords}}}),\n\n"
        res += f"({node.id}_1)-[:DOUBLE_VERTEX]->({node.id}_2),\n"
        res += f"({node.id}_2)-[:DOUBLE_VERTEX]->({node.id}_1),\n\n"

    res += "\n"

    for edge in edges:
        res += f"({edge.From.id}_2)-[:LEADS_TO {{distance:{edge.Distance}}}]->({edge.To.id}_1),\n"
        res += f"({edge.To.id}_1)-[:LEADS_TO {{distance:{edge.Distance}}}]->({edge.From.id}_2),\n"

    fd = open(name, "x", encoding="utf-8")
    fd.write(res)
    fd.close()

    return res
