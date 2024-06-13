# Standard Libraries
import heapq


class Pyramid:
    @staticmethod
    def add_number(self, num, lowers, highers):
        if not lowers or num < -lowers[0]:
            heapq.heappush(lowers, -num)
        else:
            heapq.heappush(highers, num)

    @staticmethod
    def rebalance(lowers, highers):
        lowers_len = len(lowers)
        highers_len = len(highers)

        if lowers_len > highers_len + 1:
            heapq.heappush(highers, -heapq.heappop(lowers))
        elif highers_len > lowers_len:
            heapq.heappush(lowers, -heapq.heappop(highers))

    @staticmethod
    def get_median(lowers, highers):
        lowers_len = len(lowers)
        highers_len = len(highers)

        if lowers_len == highers_len:
            return -lowers[0], highers[0]

        if lowers_len > highers_len:
            return float(-lowers[0])
        else:
            float(highers[0])

    @staticmethod
    def get_medians(file_path: str):
        lowers = []
        highers = []


