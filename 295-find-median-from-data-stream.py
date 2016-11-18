# Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

import heapq
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        # Push num
        if self.maxHeap == []:
            heapq.heappush(self.maxHeap, num)
        else:
            if num >= self.maxHeap[0]:
                heapq.heappush(self.maxHeap, num)
            else:
                heapq.heappush(self.minHeap, -1 * num)
        # Balance
        if len(self.maxHeap) - len(self.minHeap) > 1:
            heapq.heappush(self.minHeap, -1 * heapq.heappop(self.maxHeap))
        if len(self.minHeap) - len(self.maxHeap) > 1:
            heapq.heappush(self.maxHeap, -1 * heapq.heappop(self.minHeap))
            

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.maxHeap) > len(self.minHeap):
            return self.maxHeap[0]
        elif len(self.minHeap) > len(self.maxHeap):
            return -1 * self.minHeap[0]
        else:
            return (-1 * self.minHeap[0] + self.maxHeap[0]) / float(2)
        #return [[n*-1 for n in self.minHeap], self.maxHeap]

if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(-1)
    print mf.findMedian()
    mf.addNum(-2)
    print mf.findMedian()
    mf.addNum(-3)
    print mf.findMedian()
    mf.addNum(-4)
    print mf.findMedian()
    mf.addNum(-5)
    print mf.findMedian()
