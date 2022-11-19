#Lab 4 Exercise.3.4 1630902656 Kanokporn Hudsree
class Node():
    def __init__(self,value):
        self.value = value
        self.Next = ""
        
class list():
    def __init__(self):
        self.Header = ""
        
    def list_append(self,Value):
        if self.Header != "":
            self = self.Header
        while self.Next != "" :
            self = self.Next
        self.Next = Node(Value)
           
    def insert(self,index,Value):
        if index > 0:
            count = 1
            TempNode = self.Header.Next
            while count < index-1:
                if TempNode. Next!= "" :
                    TempNode = TempNode.Next
                    count += 1
                else:
                    break
                old_node = TempNode
                new_node = Node(Value)
                new_node.Next = TempNode.Next
                old_node.Next = new_node
        elif index == 0:
            new_node = Node(Value)
            new_node.Next = self.Header
            self.Header = new_node
    def remove(self,index):
        count = 0
        TempNode = self.Header
        if index > 0 and index < (self.findlength()-1):
            while count < index-1:
                if TempNode.Next != "":
                    TempNode = TempNode.Next
                    count += 1
                else:
                    break
            TempNode.Next = TempNode.Next.Next
        elif index == 0:
            self.Header = self.Header.Next
        else:
            if index == self.findlength()-2:
                limit = 1
            else:
                limit = 2
            while count < self.findlength()-limit:
                if TempNode.Next != "":
                    TempNode = TempNode.Next
                    count += 1
                else:
                    break
            TempNode.Next = ""
            
        
    def findlength(self):
        TempNode = self.Header
        count = 1
        while TempNode.Next!= "":
            count += 1
            TempNode = TempNode.Next
        return count
    
    def printList(self):
        ListValue = str(self.Header.value)
        TempNode = self.Header
        while TempNode.Next != "":
            TempNode = TempNode.Next
            ListValue += " --> " + str(TempNode.value)
            print(ListValue)


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
list_A.insert(0,104)
list_A.list_append(57)
list_A.remove(4)
list_A.printList()

