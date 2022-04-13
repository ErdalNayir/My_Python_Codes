#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None


    def printList(self):

        temp=self.head

        while(temp):
            print(temp.val)
            temp=temp.next


    def length(self):

        lenght =0
        temp = self.head

        while(temp):
            lenght+=1
            temp = temp.next

        return lenght


liste =LinkedList()

liste.head = ListNode(1)

second =ListNode(2)

third = ListNode(4)

liste.head.next =  second

second.next = third


liste.printList()

print("\n")

print(liste.length())
