class ListNode:
    def __init__(self, data):
         "constructor to initiate this object"

         self.data = data
         # store reference (next item)
         self.next = None

         return

    def has_value(self, value):
         if self.data == value:
             return True
         else:
             return False


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        return

    def add_list_item(self, item):
        "add item to the end of the list as tail"
        if not isinstance(item, ListNode):
            item = ListNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item
        self.length += 1

        return

    def list_length(self):
        "return number of list item"
        count = 0
        current_node = self.head

        while current_node is not None:
            count += 1

            current_node = current_node.next

        return count


if __name__ == "__main__":            
    node1 = ListNode(1)
    node2 = ListNode(5)
    node3 = ListNode(8)
    
    link1 = SingleLinkedList()
    link1.add_list_item(node1)
    link1.add_list_item(node2)
    link1.add_list_item(node3)
    
    print(link1.list_length())
    print(link1.length)
