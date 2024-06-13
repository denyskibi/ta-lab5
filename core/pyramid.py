# Standard Libraries
from typing import List, Union, Tuple
import heapq


class Pyramid:
    def get_medians(self, numbers: List[int]) -> list:
        medians = []
        lowers = []
        highers = []

        for number in numbers:
            self._add_number(number, lowers, highers)
            self._rebalance(lowers, highers)
            retrieved_median = self._get_median(lowers, highers)
            medians.append(retrieved_median)

        return medians

    def get_heaps(self, numbers: List[int], iteration: int):
        lowers, highers = [], []

        for i, number in enumerate(numbers):
            self._add_number(number, lowers, highers)
            self._rebalance(lowers, highers)

            if i == iteration:
                lowers = [-x for x in lowers[:5]]
                return lowers, highers[:5]

    @staticmethod
    def _add_number(num, lowers, highers) -> None:
        if not lowers or num < -lowers[0]:
            heapq.heappush(lowers, -num)
        else:
            heapq.heappush(highers, num)

    @staticmethod
    def _rebalance(lowers, highers) -> None:
        lowers_len = len(lowers)
        highers_len = len(highers)

        if lowers_len > highers_len + 1:
            heapq.heappush(highers, -heapq.heappop(lowers))
        elif highers_len > lowers_len:
            heapq.heappush(lowers, -heapq.heappop(highers))

    @staticmethod
    def _get_median(lowers, highers) -> Union[float, Tuple[int, int]]:
        lowers_len = len(lowers)
        highers_len = len(highers)

        if lowers_len == highers_len:
            return -lowers[0], highers[0]

        if lowers_len > highers_len:
            return float(-lowers[0])
        else:
            float(highers[0])
