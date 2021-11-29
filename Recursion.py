def sum_to_one_iter(n):
  result = 1
  call_stack = []
  
  while n != 1:
    execution_context = {"n_value": n}
    call_stack.append(execution_context)
    n -= 1
    print(call_stack)
  print("BASE CASE REACHED")
  while len(call_stack) != 0:
    return_value = call_stack.pop()
    print(return_value)
    result = result + return_value["n_value"]
    print(result)
  return result, call_stack

sum_to_one_iter(4)

def sum_to_one(n):
  result = 0
  for num in range(n, 0, -1):
    result += num
  return result
 
sum_to_one(4)

def power_set(set):
    power_set_size = 2**len(set)
    result = []

    for bit in range(0, power_set_size):
        sub_set = []
        for binary_digit in range(0, len(set)):
            if((bit & (1<<binary_digit))>0):
                sub_set.append(set[binary_digit])
        result.append(sub_set)
    return result

print(power_set(['a','b','c']))

def power_set_recursion(my_list):
    if len(my_list) == 0:
        return [[]]
    power_set_without_first = power_set_recursion(my_list[1:])
    with_first = [[my_list[0]] + rest for rest in power_set_without_first]
    return with_first + power_set_without_first

print(power_set_recursion(['a','b','c','d']))

#flatten
def flatten(my_list):
  result = []
  for item in my_list:
    if isinstance(item, list):
      print("List found!")
      flat_list = flatten(item)
      for x in flat_list:
        result.append(x)
    else:
      result.append(item)
  return result

### reserve for testing...
planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]

print(flatten(planets))

# define the fibonacci() function below
def fibonacci(n):
  if n == 1:
    return 1
  if n == 0:
    return 0
  
  return fibonacci(n-2) + fibonacci(n-1)

fibonacci(5)
# set the appropriate runtime:
# 1, logN, N, N^2, 2^N, N!
fibonacci_runtime = "2^N"

# Define build_bst()
def build_bst(my_list):
  if len(my_list) == 0:
    return "No Child"
  middle_idx = len(my_list) // 2
  middle_value = my_list[middle_idx]
  print("Middle index: {0}".format(middle_idx))
  print("Middle value: {0}".format(middle_value))
  tree_node = {"data": middle_value}
  tree_node["left_child"] = build_bst(my_list[:middle_idx])
  tree_node["right_child"] = build_bst(my_list[middle_idx+1:])
  return tree_node

# For testing
sorted_list = [12, 13, 14, 15, 16]
binary_search_tree = build_bst(sorted_list)
print(binary_search_tree)

# fill in the runtime as a string
# 1, logN, N, N*logN, N^2, 2^N, N!
runtime = "N*logN"
