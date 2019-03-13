from linked_list import ListNode, SingleLinkedList
import pytest

def test_single_linked_list():
    # FillConstant
    @pytest.fixture
    def element_A():
        return {
            "event_tracking_name": "VISIT",
            "event_trigger": "HOMEPAGE",
            "client_timestamp": 12879818279387,
        }


    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node7 = ListNode(7)
    node8 = ListNode(8)
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

    assert link1.list_length() == 9

    print("remove value 5")
    link1.remove_by_value(5)
    assert link1.list_length() == 8
    assert link1.head.data == 1
    assert link1.tail.data == 9

    link1.remove_by_value(9)
    assert link1.list_length() == 7
    assert link1.head.data == 1
    assert link1.tail.data == 8

    res = link1.search(3)
    assert res == [3]