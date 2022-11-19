#Lab 4 Exercise.3.1 1630902656 Kanokporn Hudsree
class list():
    def __init__(self):
        self.Header = ""
    def printList(self):
        ListValue = str(self.Header.value)
        TempNode = self.Header
        while TempNode.Next != "":
            TempNode = TempNode.Next
            ListValue += " --> " + str(TempNode.value)
            print(ListValue)
class Node():
    def __init__(self,value):
        self.value = value
        self.Next = ""

list_A = list()
Node_1 = Node(44)
list_A.Header = Node_1

Node_2 = Node(36)
Node_1.Next = Node_2

Node_3 = Node(90)
Node_2.Next = Node_3

Node_4 = Node(10)
Node_3.Next = Node_4

Node_5 = Node(60)
Node_4.Next = Node_5

Node_6 = Node(99)
Node_5.Next = Node_6
list_A.printList()
