from abc import ABC, abstractmethod
from overrides import override
from threading import Thread
from typing import Dict, List


class PathSolver(ABC, Thread):
    def __init__(self, id: int, path: List[Dict[str, object]]) -> None:
        Thread.__init__(self)
        self._id = id
        self._path = path
        self._total_distance = 0
        self._nodes = []

    @property
    def id(self) -> int:
        return self._id

    @property
    def total_distance(self) -> float:
        return self._total_distance
    
    @property
    def nodes(self) -> List[object]:
        return self._nodes

    @abstractmethod
    def solve_path(self) -> None:
        ...

    @abstractmethod
    def to_dict(self) -> Dict[str, object]:
        return {
            'id': self.id,
            'total_distance': self.total_distance,
            'nodes': self.nodes
        }

class LinearPathSolver(PathSolver):
    def solve_path(self) -> None:
        for edge in self._path:
            self._total_distance += edge['distance']
            self._nodes.append(edge['node'])

    def to_dict(self) -> Dict[str, object]:
        return {
            'id': self.id,
            'total_distance': self.total_distance,
            'nodes': self.nodes
        }

    @override
    def run(self) -> None:
        self.solve_path()
