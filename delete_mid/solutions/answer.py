%run ../linked_list/linked_list.py
class MyLinkedList(LinkedList):

    def delete_node(self, node):
        if node is None:
            return
        if node.next is None:
            node.data = None
        else:
            node.data = node.next.data
            node.next = node.next.next
