# https://poteblog.com/2020/04/15/post-914/
# 配列と比較した際のメリット
# ・単方向リストは配列の順番をポインタで管理。配列から削除・追加したい際には前後のノードのポインタを
# 帰るだけで済む。O(1)の時間しかかからない。
#
# デメリット
# ・インデックスの概念がなく、ポインタを通ってノードまで到達する必要あり。各データへのアクセスに時間がかかる（O(N))。

# class ListNode():
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#
# def show(node):
#     while True:
#         if node and node.next:
#             print(node.val + "-", end="")
#             node = node.next
#         if node.next is None:
#             print(node.val)
#             break
#
# def delete_C(node):
#     tmp = node
#     while tmp and tmp.next:
#         if tmp.next.val == "C":
#             tmp.next = tmp.next.next
#         else:
#             tmp = tmp.next
#     return show(node)

class Node():
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node #行き先を示す目印？実際の行き先は別のNodeオブジェクトで作成。

class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert(self, data):
        new_node = Node(data)
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
            self.head = current_node.next
            current_node = None
            return

        previous_node = None
        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return

        previous_node.next = current_node.next
        current_node = None

    def reverse_iterative(self):
        previous_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node

            previous_node = current_node
            current_node = next_node

        self.head = previous_node

    def reverse_recursive(self):
        def _reverse_recursive(current_node, previous_node):
            if not current_node:
                return previous_node

            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
            return _reverse_recursive(current_node, previous_node)

        self.head = _reverse_recursive(self.head, None)



if __name__ == "__main__":
    l = LinkedList()
    l.append(0)
    l.append(1)
    l.append(2)
    l.append(3)
    # l.insert(0)
    # l.remove(2)
    l.print()
    print("#################")
    l.reverse_iterative()
    l.print()
    print("#################")
    l.reverse_recursive()

    # n1 = ListNode('A')
    # n2 = ListNode('B')
    # n3 = ListNode('C')
    # n4 = ListNode('D')
    # n1.next = n2
    # n1.next.next = n3
    # n1.next.next.next = n4
    # show(n1)
    # delete_C(n1)

