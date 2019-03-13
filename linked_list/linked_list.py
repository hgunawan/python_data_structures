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

    def print_list(self):
        "print item in list"
        current_node = self.head

        while current_node is not None:
            print(" - {}".format(current_node.data))

            current_node = current_node.next

        return

    def output_list(self):
        "outputs the list (the value of the node, actually)"

        current_node = self.head

        while current_node is not None:
            print(current_node.data)

            # jump to the linked node
            current_node = current_node.next

        return

    def search(self, value):
        "search the linked list"
        current_node = self.head

        node_id = 1

        results = []

        while current_node is not None:
            if current_node.has_value(value):
                results.append(node_id)

            current_node = current_node.next
            node_id+=1

        return results

    def remove_by_id(self, item_id):
        "remove item from list by item_id"

        current_id = 1
        current_node = self.head
        previous_node = None

        while current_node is not None:
            if current_id == item_id:
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
                    return

                if current_node.next is None:
                    print("set tail by id")
                    print(previous_node.data)
                    self.tail = previous_node


            previous_node = current_node
            current_node = current_node.next
            current_id+=1

        return


    def remove_by_value(self, value):
        current_node = self.head
        previous_node = None 

        while current_node is not None:
            if current_node.has_value(value):
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next

                if current_node.next is None:
                    print("set tail")
                    self.tail = previous_node

            previous_node = current_node
            current_node = current_node.next

            


if __name__ == "__main__":            
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node7 = ListNode(7)
    node8 = ListNode(5)
    node9 = ListNode(9)

    nodeA = ListNode("A")
    nodeB = ListNode("B")
    nodeC = ListNode("C")

    link1 = SingleLinkedList()
    link1.add_list_item(node1)
    link1.add_list_item(node2)
    link1.add_list_item(node3)
    link1.add_list_item(node4)
    link1.add_list_item(node5)
    link1.add_list_item(node6)
    link1.add_list_item(node7)
    link1.add_list_item(node8)
    link1.add_list_item(node9)

    
    print(link1.list_length())
    print(link1.length)
    
    print("remove value 5")
    link1.remove_by_value(5)
    link1.remove_by_value(9)
    link1.remove_by_value(1)
    link1.remove_by_value(7)
    print("head-tail")
    print(link1.head.data)
    print("list content")
    (link1.output_list())
    print("remove by id")
    link1.remove_by_id(4) 
    print("head-tail")
    print(link1.head.data)
    print(link1.tail.data)

    link1.add_list_item(nodeA)
    print("list content add A")
    (link1.output_list())
    
    print("head-tail")
    print(link1.head.data)
    print(link1.tail.data)

    #print("\nsearch")
    #print(link1.search(5))
    #
    #
    #print("remove")
    #link1.remove_by_id(5)
    #link1.print_list()
    #print("remove")
    #link1.remove_by_id(7)
    #link1.print_list()

    #print(link1.list_length())
