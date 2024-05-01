
from pprint import pprint
from queue import Queue
from typing import List
class GraphList:

    def __init__(self) -> None:
        self.n = 0
        self.L: List[List[int]] = []

    def add_vertex(self) -> None:
        self.L.append([])
        self.n += 1

    def add_edge(self, vi: int, vf: int) -> bool:
        if not ((0 <= vi < self.n) and (0 <= vf < self.n)):
            return False
        self.L[vi].append(vf)
        self.L[vi].sort()
        self.L[vf].append(vi)
        self.L[vf].sort()
        return True