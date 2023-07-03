class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    # Head = None means list is empty
    self.head = None
    self.list_len = 0
    #insert new node at the head
  def insert_at_head(self, data):
    
    # new node
    new_node = Node(data)
    
    # create connection
    new_node.next = self.head
    
    # re-asign head
    self.head = new_node
    
    # increment list size
    self.list_len = self.list_len + 1
      
  # Traverse the list 
  def __str__(self):
    
    curr = self.head

    result = ''
    
    while curr != None:
      
      result = result + str(curr.data) + '->'
      curr = curr.next
    return result[:-2]
      
      
  
  def len(self):
    return self.list_len

ll = LinkedList()

ll.insert_at_head(1)
ll.insert_at_head(2)
ll.insert_at_head(3)
ll.insert_at_head(4)

print(ll)

