# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    p = l1
    q = l2
    dl = ListNode(0)
    
    r = dl
    carry = 0
    while(p != None or q != None):
        if p != None: 
            x = p.val 
        else:
            x = 0
        
        if q != None:
            y = q.val
        else:
            y = 0
        
        s = carry + x + y
        # This is where the magic happens! We encode the carry value the cary is going to be integer division
        # of the sum (we get the first digit or zero)
        carry = s // 10
        # The if we have a carry value we just take the second digits (this is why we mod 10 to cut off the front digit if we have carry over)
        r.next = ListNode(s % 10)
        
        r = r.next
        
        if (p != None):
            p = p.next
        if(q != None):
            q = q.next
        
    
    if carry > 0:
        r.next = ListNode(carry)
    
    # We basically padded the return with a 0 to make the rest of the algorithm simpler.
    # This way we don't have to worry about the current value of r just what it will be later.
    return dl.next