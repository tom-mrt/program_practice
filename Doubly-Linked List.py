class Node():
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node # 前のノードも指せる＝双方向


class DoublyLinkedList():
    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        new_node.prev = current_node

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def remove(self, data):
        current_node = self.head
        if current_node and current_node.data == data:
            if current_node.next is None: # headのみ存在する場合
                current_node = None
                self.head = None
                return
            else: # 先頭を削除
                next_node = current_node.next
                next_node.prev = None
                current_node = None
                self.head = next_node
                return

        # 途中を削除する
        while current_node and current_node.data != data:
            current_node = current_node.next

        if current_node is None: # 削除対象がなかった場合
            return

        if current_node.next is None: # 最後尾を削除する場合
            prev = current_node.prev
            prev.next = None
            current_node = None
            return
        else: # 途中を削除
            next_node = current_node.next
            prev_node = current_node.prev
            prev_node.next = next_node
            next_node.prev = prev_node
            current_node = None
            return

    def reverse_iterative(self): # 逆順にリンクをはる
        previous_node = None
        current_node = self.head
        while current_node:
            previous_node = current_node.prev
            current_node.prev = current_node.next
            current_node.next = previous_node

            current_node = current_node.prev

        if previous_node:
            self.head = previous_node.prev




if __name__ == "__main__":
    d = DoublyLinkedList()
    d.append(0)
    d.append(1)
    d.append(2)
    d.append(3)
    # print(d.head.data)
    # print(d.head.next.data)
    print("############")
    d.reverse_iterative()
    d.print()