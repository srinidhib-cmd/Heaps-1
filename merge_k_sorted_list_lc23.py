"""
Author: Srinidhi
Did it run on LC: Yes
Time Complexity: O(number of elements x log k) - construction of heap will take log K - but we have
                                                N elements in total - Where N is the total number of elements

Space Complexity: O(k) - Where k is the number of lists. - At a given point of time, not more than k elements
                         will be present in the heap

Logic: Inital logic is to maintain pointers and iterate throught the list and keep comparision going on
Instead of maintaining "k pointers" we can maintain heap of size k, which gives us the min element always

This will take O(k) extra space. Also, since we want the minimum element at a given time, we maintain a 
min heap
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        """
        Note: V.V.Imp - From Python3 on wards, for custom comparision, we need to override the folowing functions
         __eq__ and __lt__ which will help in compating node objects
        """

        ListNode.__eq__ = lambda self,other: self.val == other.val
        ListNode.__lt__ = lambda self,other: self.val < other.val
        

        
        heap = []
        head = tail = ListNode(0)
        dummyHead = head
        for i in lists:
            
            if i:
                heapq.heappush(heap,(i.val,i))
        
        print(heap)
        
        while heap:
            node = heapq.heappop(heap)[1]
            dummyHead.next = node
            dummyHead = dummyHead.next
            
            if node.next:
                heapq.heappush(heap,(node.next.val,node.next))
        return head.next