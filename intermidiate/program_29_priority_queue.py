"""Demonstrate a simple priority queue with heapq."""

import heapq
from dataclasses import dataclass, field
from typing import Any


@dataclass(order=True)
class Task:
    priority: int
    description: str = field(compare=False)


class PriorityQueue:
    """Store tasks ordered by priority."""

    def __init__(self) -> None:
        self._heap: list[Task] = []

    def push(self, task: Task) -> None:
        heapq.heappush(self._heap, task)

    def pop(self) -> Task:
        if not self._heap:
            raise IndexError("pop from an empty priority queue")
        return heapq.heappop(self._heap)

    def __len__(self) -> int:
        return len(self._heap)


if __name__ == "__main__":
    queue = PriorityQueue()
    queue.push(Task(2, "Write documentation"))
    queue.push(Task(1, "Fix bug"))
    queue.push(Task(3, "Refactor code"))
    while queue:
        task = queue.pop()
        print(f"Handling: {task.description} (priority {task.priority})")
