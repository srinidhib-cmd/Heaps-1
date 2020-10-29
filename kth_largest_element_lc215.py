"""
Author: Srinidhi
Did it run on LC: yes
Time Complexity: O(k logN)
Space Complexity: O(N) - pushing all elements in heap

Logic: Naive Solution - Sort and return the element at kth position from the end (O(N logN))

Better Solution - Using heap data structure- Maintain a min heap with N size, and pop put k elements, 
the top element now should be the kth min element

"""
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        if len(nums)==0:
            return []
        
        if len(nums) == k:
            return min(nums)
        
        heap = []
        for num in nums:
            heapq.heappush(heap,num)
        
        for _ in range(len(nums)-k):
            heapq.heappop(heap)
        
        return heapq.heappop(heap)