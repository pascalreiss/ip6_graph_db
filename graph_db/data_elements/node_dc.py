from dataclasses import dataclass

import numpy as np

from graph_db.data_elements.bahnhof_enum import Bhf
from graph_db.data_elements.element_enum import Element


@dataclass(unsafe_hash=True)
class Node:
    id: str
    ecos_id: str
    element: Element
    name: str
    bhf: Bhf
    coords: np.ndarray
