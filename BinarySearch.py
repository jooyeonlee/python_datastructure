# define binary_search()
def binary_search(sorted_list, target):
  if not sorted_list:
    return 'value not found'
  mid_idx = len(sorted_list)//2
  mid_val = sorted_list[mid_idx]
  if mid_val == target:
    return mid_idx
  elif mid_val > target:
    left_half = sorted_list[:mid_idx]
    return binary_search(left_half, target)
  else:
    right_half = sorted_list[mid_idx+1:]
    result = binary_search(right_half, target)
    if result == "value not found":
      return result
    return result + mid_idx + 1
# For testing:
sorted_values = [13, 14, 15, 16, 17]
print(binary_search(sorted_values, 16))

#refactor
def binary_search(sorted_list, left_pointer, right_pointer, target):
  # this condition indicates we've reached an empty "sub-list"
  if left_pointer >= right_pointer:
    return "value not found"
  
  # We calculate the middle index from the pointers now
  mid_idx = (left_pointer + right_pointer) // 2
  mid_val = sorted_list[mid_idx]
  if mid_val == target:
    return mid_idx
  if mid_val > target:
    # we reduce the sub-list by passing in a new right_pointer
    return binary_search(sorted_list, left_pointer, mid_idx, target)
  if mid_val < target:
    # we reduce the sub-list by passing in a new left_pointer
    return binary_search(sorted_list, mid_idx + 1, right_pointer, target)
  
values = [77, 80, 102, 123, 288, 300, 540]
start_of_values = 0
end_of_values = len(values)
result = binary_search(values, start_of_values, end_of_values, 288)
print("element {0} is located at index {1}".format(288, result))

# Iterative Binary Search
def binary_search(sorted_list, target):
  left_pointer = 0
  right_pointer = len(sorted_list)
  
  # fill in the condition for the while loop
  while left_pointer < right_pointer:
    # calculate the middle index using the two pointers
    mid_idx = (left_pointer + right_pointer)//2
    mid_val = sorted_list[mid_idx]
    if mid_val == target:
      return mid_idx
    if target < mid_val:
      # set the right_pointer to the appropriate value
      right_pointer = mid_idx
    if target > mid_val:
      # set the left_pointer to the appropriate value
      left_pointer = mid_idx + 1
  
  return "Value not in list"
# test cases
print(binary_search([5,6,7,8,9], 9))
print(binary_search([5,6,7,8,9], 10))
print(binary_search([5,6,7,8,9], 8))
print(binary_search([5,6,7,8,9], 4))
print(binary_search([5,6,7,8,9], 6))

# Iterative Binary Search to search through a sparsely sorted dataset
def sparse_search(data, search_val):
  print("Data: " + str(data))
  print("Search Value: " + str(search_val))
  first = 0
  last = len(data)-1
  while first <= last:
    mid = (first+last)//2
    if data[mid] == "":
      left = mid - 1
      right = mid + 1
      while True:
        if left < first and right > last:
          print("{0} is not in the dataset".format(search_val))
          return
        elif right <= last and data[right] != "":
          mid = right
          break
        elif left >= first and data[left] != "":
          mid = left
          break
        else:
          right += 1
          left -=1
    if data[mid] == search_val:
      print("{0} found at position {1}".format(search_val, mid))
      return
    if search_val < data[mid]:
      last = mid - 1
    if search_val > data[mid]:
      first = mid + 1
  print("{0} is not in the dataset".format(search_val))

#python -c 'import script; script.sparse_search(["A", "", "", "", "B", "", "", "", "C", "", "", "D"], "C")'
#python -c 'import script; script.sparse_search(["A", "B", "", "", "E"], "A")'
#python -c 'import script; script.sparse_search(["", "X", "", "Y", "Z"], "Z")'
#python -c 'import script; script.sparse_search(["A", "", "", "", "B", "", "", "", "C"], "D")'
#python -c 'import script; script.sparse_search(["Apple", "", "Banana", "", "", "", "", "Cow"], "Banana")'
#python -c 'import script; script.sparse_search(["Alex", "", "", "", "", "Devan", "", "", "Elise", "", "", "", "Gary", "", "", "Mimi", "", "", "Parth", "", "", "", "Zachary"], "Parth")'