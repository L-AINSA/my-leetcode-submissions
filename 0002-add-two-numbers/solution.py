# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        newList = ListNode(0, None)
        def findLinkedLen(list):
            length = 0
            currNode = list
            while currNode is not None:
                length += 1
                currNode = currNode.next
            return length
        if(findLinkedLen(l1) >= findLinkedLen(l2)):
            longerList = l1
            shorterList = l2
        else:
            longerList = l2
            shorterList = l1
        carryLast = False
        currentNodeLong = longerList
        currentNodeShort = shorterList
        currentNodeSelf = newList
        while currentNodeShort is not None:
            sumCurrVals = currentNodeLong.val + currentNodeShort.val
            if carryLast:
                sumCurrVals += 1
            if sumCurrVals >= 10: 
                currentNodeSelf.val = sumCurrVals - 10
                carryLast = True
            else:
                currentNodeSelf.val = sumCurrVals
                carryLast = False
            currentNodeLong = currentNodeLong.next
            currentNodeShort = currentNodeShort.next
            if currentNodeLong is not None or currentNodeShort is not None or carryLast:
                newNode = ListNode(0, None)
                currentNodeSelf.next = newNode
                currentNodeSelf = currentNodeSelf.next
        while currentNodeLong is not None:
            sumCurrVals = currentNodeLong.val
            if carryLast:
                sumCurrVals += 1
            if sumCurrVals >= 10: 
                currentNodeSelf.val = sumCurrVals - 10
                carryLast = True
            else:
                currentNodeSelf.val = sumCurrVals
                carryLast = False
            currentNodeLong = currentNodeLong.next
            if currentNodeLong is not None or carryLast:
                newNode = ListNode(0, None)
                currentNodeSelf.next = newNode
                currentNodeSelf = currentNodeSelf.next
        if carryLast:
            currentNodeSelf.val = 1
        return newList
        

