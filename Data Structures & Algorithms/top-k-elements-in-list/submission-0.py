class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        result = []

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        bucket = [[] for _ in range(len(nums) + 1)]

        for num, frequency in count.items():
            bucket[frequency].append(num)

        for i in range(len(bucket) -1, 0, -1 ):
            for num in bucket[i]:
                result.append(num)
                
                if len(result) == k:
                    return result