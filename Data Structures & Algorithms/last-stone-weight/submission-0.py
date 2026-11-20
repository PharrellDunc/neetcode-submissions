class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        negative_stones = [-stone for stone in stones]

        heapq.heapify(negative_stones)

        while len(negative_stones) >= 2:
            first = -heapq.heappop(negative_stones)
            second = -heapq.heappop(negative_stones)

            difference = first - second
            if difference > 0:
                heapq.heappush(negative_stones, -difference)

        if len(negative_stones) == 0:
            return 0

        return -negative_stones[0]
        