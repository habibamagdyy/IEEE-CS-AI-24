from typing import List
class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        count = list(map(int, input("Enter the list numbers separated by spaces: ").split()))

        minimum = next((i for i, num in enumerate(count) if num), None)
        maximum = next((i for i, num in reversed(list(enumerate(count))) if num), None)
        n = sum(count)
        mean = sum(i * c / n for i, c in enumerate(count))
        mode = count.index(max(count))
        numCount = 0
        leftMedian = 0
        for i, c in enumerate(count):
            numCount += c
            if numCount >= n / 2:
                leftMedian = i
                break

        return [minimum, maximum, mean, leftMedian, mode]
solution = Solution()
count = solution.sampleStats([])
print("Sample Stats:", count)