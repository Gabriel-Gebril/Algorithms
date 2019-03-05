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
        carry = s // 10
        r.next = ListNode(s % 10)
        
        r = r.next
        
        if (p != None):
            p = p.next
        if(q != None):
            q = q.next
        
    
    if carry > 0:
        r.next = ListNode(carry)
    
    return dl.next