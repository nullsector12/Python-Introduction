class Node:
    
    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None


    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr is not None:
            s += repr(curr.data)
            if curr.next is not None:
                s += ' -> '
            curr = curr.next
        return s


    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True


    def getLength(self):
        return self.nodeCount
    
    def popAt(self, pos):

        # pos가 0일때     
        if pos < 1 or pos > self.nodeCount:
            raise IndexError

        # 원소가 하나일 때
        if pos == 1 and pos == self.nodeCount:
            node = self.head.data
            self.head = None
            self.tail = None
            self.nodeCount = 0
            return node

        # pos가 tail을 가리킬 때
        elif pos == self.nodeCount:
            node = self.tail.data
            prev = self.getAt(pos-1)
            self.tail = prev
            prev.next = None
            self.nodeCount = self.nodeCount-1
            return node

        # pos가 head를 가리킬 때
        elif pos == 1:
            node = self.head.data
            self.head = self.head.next
            self.nodeCount = self.nodeCount-1
            return node

        # pos가 노드 중간에서 삭제
        else:
            node = self.getAt(pos).data
            prev = self.getAt(pos-1)
            nextNode = self.getAt(pos+1)
            prev.next = nextNode
            self.nodeCount = self.nodeCount-1
            return node


    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result


    def concat(self, L):
        self.tail.next = L.head
        if L.tail:
            self.tail = L.tail
        self.nodeCount += L.nodeCount
