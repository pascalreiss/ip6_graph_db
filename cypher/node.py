from dataclasses import dataclass
import numpy as np

import cypher.weiche_typ as weiche

@dataclass(unsafe_hash=True)
class Node:
    id: str
    ECoS_id: str
    coords: np.ndarray
    type: weiche.Weiche
