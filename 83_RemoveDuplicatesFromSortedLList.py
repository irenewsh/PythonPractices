class Solution:
	# 44ms, 13.1 M (best)
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        
        current = head.next
        prev = head
        
        while current != None:
            if current.val == prev.val:
                prev.next = current.next #只有这一行会对head进行改变
                current = current.next
            else:
                current = current.next
                prev = prev.next
        
        return head

    # 44ms, 13.2M 
    def deletDuplicates2(self, head):
        curr = head # head itself works as sentinel
        while curr!=None and curr.next!=None:
            if (curr.val == curr.next.val):
                curr.next = curr.next.next #pointer.next update
            else:
                curr = curr.next #update pointer location
        return head

    # similar to the second method
        def deleteDuplicates3(self, head):
        curr = head
        if curr == None:
            return []
        while curr.next!=None:
            if (curr.val == curr.next.val):
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

