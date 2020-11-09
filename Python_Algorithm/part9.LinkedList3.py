class Node:
    
    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = None
        self.head.next = self.tail


    def traverse(self):
        result = []
        curr = self.head
        while curr.next:
            curr = curr.next
            result.append(curr.data)
        return result


    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        i = 0
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    def insertAfter(self, prev, newNode):
        newNode.next = prev.next
        if prev.next is None:
            self.tail = newNode
        prev.next = newNode
        self.nodeCount += 1
        return True


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos != 1 and pos == self.nodeCount + 1:
            prev = self.tail
        else:
            prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)


    def popAfter(self, prev):
        
        # 추가1. 삭제하려는 노드 선언
        curr = prev.next

        # 원소가 하나일 때
        if prev.next is None:
            return curr.data

        # 현재값이 tail을 가리킬 때
        if curr.next is None:
            # Dummy node만 존재하는 유일한 노드일 경우
            if self.nodeCount == 1:
                self.tail = None
            
            # Dummy node 이외의 다른 노드가 tail일 경우
            else:
                self.tail = prev
        
        # 이전값의 다음 링크를 삭제하려는 노드의 다음 값으로 변경
        prev.next = curr.next
        
        # 노드카운트 -1
        self.nodeCount -= 1

        return curr.data


    def popAt(self, pos):

        # 잘못된 pos값이 들어온 경우
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        
        # popAfter에 prev 전달
        prev = self.getAt(pos-1)

        return self.popAfter(prev)
                


def solution(x):
    return 0