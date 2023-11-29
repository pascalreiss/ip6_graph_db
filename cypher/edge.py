from dataclasses import dataclass
import cypher.node as node



@dataclass(unsafe_hash=True)
class Edge:
    From: node.Node
    To: node.Node
    Distance: float