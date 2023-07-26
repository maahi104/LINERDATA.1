# # QUESTION 1


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_zero_sum_sublists(head):
    dummy = Node(0)
    dummy.next = head
    prefix_sum = 0
    prefix_sums = {prefix_sum: dummy}
    while head:
        prefix_sum += head.data
        if prefix_sum in prefix_sums:
            node = prefix_sums[prefix_sum].next
            sum_to_delete = prefix_sum + node.data
            while sum_to_delete != prefix_sum:
                del prefix_sums[sum_to_delete]
                node = node.next
                sum_to_delete += node.data
            prefix_sums[prefix_sum].next = head.next
        else:
            prefix_sums[prefix_sum] = head
        head = head.next
    return dummy.next

def print_list(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

# Example usage
def create_list():
    head = Node(6)
    head.next = Node(-6)
    head.next.next = Node(8)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(-12)
    head.next.next.next.next.next = Node(9)
    head.next.next.next.next.next.next = Node(8)
    return head

head = create_list()
print("Original list:")
print_list(head)

head = delete_zero_sum_sublists(head)
print("List after deleting zero-sum sublists:")
print_list(head)

# # QUESTION 2

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
  
# Reverses the linked list in groups
# of size k and returns the pointer
# to the new head node.
  
  
def reverse(head, k):
  # If head is NULL or K is 1 then return head
    if not head or k == 1:
        return head
    dummy = Node(-1)  # creating dummy node
    dummy.next = head
    # Initializing three points prev, curr, next
    prev = dummy
    curr = dummy
    next = dummy
    count = 0
    toLoop = 0
    i = 0
  
    # Calculating the length of linked list
    while curr:
        curr = curr.next
        count += 1
  
    # Iterating till next is not none
    while next:
        curr = prev.next  # Curr position after every reversed group
        next = curr.next  # Next will always next to curr
        # toLoop will set to count - 1 in case of remaining element
        toLoop = count > k and k or count - 1
        for i in range(1, toLoop):
                # 4 steps as discussed above
            curr.next = next.next
            next.next = prev.next
            prev.next = next
            next = curr.next
        # Setting prev to curr
        prev = curr
        # Update count
        count -= k
  
     # dummy -> next will be our new head for output linked list
    return dummy.next
  
# Function to print linked list
  
  
def printList(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.next
  
  
# Created Linked list is 1->2->3->4->5->6->7->8->9
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)
head.next.next.next.next.next.next.next.next = Node(9)
  
print("Given linked list")
printList(head)
head = reverse(head, 3)
  
print("\nReversed Linked list")
printList(head)
