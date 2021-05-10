# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        head.next = self.deleteDuplicates(head.next)
        if head.val != head.next.val:
            return head
        else:
            return head.next
        return answer


# other solution

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        currentNode = head
        while currentNode:
            nextDistinctNode = currentNode.next
            while nextDistinctNode and nextDistinctNode.val == currentNode.val:
                nextDistinctNode = nextDistinctNode.next
            
            currentNode.next = nextDistinctNode
            currentNode = nextDistinctNode
            
        return head