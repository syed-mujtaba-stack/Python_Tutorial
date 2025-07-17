# Day 39 Solution: Advanced Design Patterns
from abc import ABC, abstractmethod

# Strategy Interface
class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass

# Concrete Strategies
class BubbleSort(SortStrategy):
    def sort(self, data):
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
        return data

class QuickSort(SortStrategy):
    def sort(self, data):
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.sort(left) + middle + self.sort(right)

# Context
class Sorter:
    def __init__(self, strategy=QuickSort()):
        self._strategy = strategy
    
    def set_strategy(self, strategy):
        self._strategy = strategy
    
    def sort(self, data):
        return self._strategy.sort(data.copy())

# Usage
data = [64, 34, 25, 12, 22, 11, 90]
sorter = Sorter()
print("Quick Sort:", sorter.sort(data))
sorter.set_strategy(BubbleSort())
print("Bubble Sort:", sorter.sort(data))
