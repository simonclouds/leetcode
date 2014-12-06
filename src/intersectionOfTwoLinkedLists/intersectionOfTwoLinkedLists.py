# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        heada = headA
        headb = headB

        
        lengthA = self.getListLen(headA);
        lengthB = self.getListLen(headB);
        if lengthA * lengthB == 0:
            return None;
            
        lastStatus = '='
        
       
        if lengthA > lengthB:
            while lengthA != lengthB:
                heada = heada.next;
                lengthA = lengthA - 1;
        else:
            while lengthA != lengthB:
                headb = headb.next;
                lengthB = lengthB - 1;
        
        intersectionNode = heada
         
        while heada != None:
            if heada.val != headb.val:
                heada = heada.next;
                headb = headb.next;
                intersectionNode = heada;
                lastStatus = 'x'
            else :
                heada = heada.next;
                headb = headb.next;
                lastStatus = '='
        
        return intersectionNode;
        
    def getListLen(self, head):
        length = 0;
        while head != None:
            length  = length + 1;
            head = head.next;
        return length;
