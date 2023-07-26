# # QUESTION 1

# A Linked List Node
class ListNode:
	def __init__(self, val):
		self.val = val
		self.next = None

# Function to create Node
def getNode(data):
	temp = ListNode(data)
	temp.next = None
	return temp

# Function to print the Linked List
def printList(head):
	while (head.next):
		print(head.val, end=' -> ')
		head = head.next
	print(head.val, end='')

# Function that removes continuous nodes
# whose sum is K
def removeZeroSum(head, K):

	# Root node initialise to 0
	root = ListNode(0)

	# Append at the front of the given
	# Linked List
	root.next = head

	# Map to store the sum and reference
	# of the Node
	umap = dict()

	umap[0] = root

	# To store the sum while traversing
	sum = 0

	# Traversing the Linked List
	while (head != None):

		# Find sum
		sum += head.val

		# If found value with (sum - K)
		if ((sum - K) in umap):

			prev = umap[sum - K]
			start = prev

			# Delete all the node
			# traverse till current node
			aux = sum

			# Update sum
			sum = sum - K

			# Traverse till current head
			while (prev != head):
				prev = prev.next
				aux += prev.val
				if (prev != head):
					umap.remove(aux)

			# Update the start value to
			# the next value of current head
			start.next = head.next

		# If (sum - K) value not found
		else:
			umap[sum] = head

		head = head.next

	# Return the value of updated
	# head node
	return root.next


# Driver Code
if __name__ == '__main__':

	# Create Linked List
	head = getNode(1)
	head.next = getNode(2)
	head.next.next = getNode(-3)
	head.next.next.next = getNode(3)
	head.next.next.next.next = getNode(1)

	# Given sum K
	K = 5

	# Function call to get head node
	# of the updated Linked List
	head = removeZeroSum(head, K)

	# Print the updated Linked List
	if(head != None):
		printList(head)

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