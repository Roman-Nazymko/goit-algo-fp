class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)
# Функція, яка реалізує реверсування однозв'язного списку
    def reverse(self):
        previous = None
        current = self.head
        while current:
            next_node = current.next  # зберігаємо посилання на наступний вузол
            current.next = previous  # змінюємо посилання на попередній вузол
            previous = current  # просуваємося вперед на один вузол
            current = next_node
        self.head = previous  # новий головний вузол - це колишній останній вузол

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


    # Сортування злиттям
    def _split(self, head):
        if not head or not head.next:
            return head, None
        
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        middle = slow.next
        slow.next = None
        
        return head, middle

    def _merge_sorted(self, left, right):
        if not left:
            return right
        if not right:
            return left
        
        if left.value < right.value:
            result = left
            result.next = self._merge_sorted(left.next, right)
        else:
            result = right
            result.next = self._merge_sorted(left, right.next)
        
        return result

    def merge_sort(self, head=None):
        if head is None:
            head = self.head
            
        if not head or not head.next:
            return head
        
        left, right = self._split(head)
        left = self.merge_sort(left)
        right = self.merge_sort(right)
        
        return self._merge_sorted(left, right)
    
    def sort(self):
        self.head = self.merge_sort(self.head)
    
    # Об'єднання двох відсортованих списків в один
    def merge_sorted_lists(self, list1, list2):
        dummy = Node(0)
        tail = dummy
    
        while list1 and list2:
            if list1.value < list2.value:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        # Якщо один із списків закінчився, додаємо залишок іншого списку
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next
    
# Перевірка функцій
list1 = LinkedList()
list1.append(1)
list1.append(3)
list1.append(5)

print("Перший список:")
list1.print_list()

print("Реверсований перший список:")
list1.reverse()
list1.print_list()

print("Відсортований перший список:")
list1.sort()
list1.print_list()

list2 = LinkedList()
list2.append(2)
list2.append(4)
list2.append(6)

print("Другий список:")
list2.print_list()

print("Реверсований другий список:")
list2.reverse()
list2.print_list()

print("Відсортований другий список:")
list2.sort()
list2.print_list()

merged_list = LinkedList()
merged_list.head = merged_list.merge_sorted_lists(list1.head, list2.head)

print("Об'єднаний відсортований список:")
merged_list.print_list()
