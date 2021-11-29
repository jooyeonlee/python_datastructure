class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list
  
  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None
        else:
          current_node = next_node
    
  def find_node_iteratively(self, value):
    current_node = self.head_node
    
    while current_node:
      if current_node.value == value:
        return current_node
      current_node = current_node.get_next_node()
      
    return None

  def find_node_recursively(self, value, current_node):
    if current_node == None:
      return None
    elif current_node.value == value:
      return current_node
    else:
      return self.find_node_recursively(value, current_node.get_next_node())


my_list = LinkedList()

my_list.insert_beginning("Node 1")
my_list.insert_beginning("Node 2")
my_list.insert_beginning("Node 3")
my_list.insert_beginning("Node 4")

# Find Node iteratively:
found_node = my_list.find_node_iteratively("Node 3")
# Print node value to the console:
print(found_node.value)

# Add code here:
found_node = my_list.find_node_recursively("Node 2", my_list.head_node)
print(found_node)