# For each element in the search_list
    # if element equal target value then
       # return its index
# if element is not found then 
    # raise a ValueError

number_list = [ 10, 14, 19, 26, 27, 31, 33, 35, 42, 44]
target_number = 33
def linear_search(search_list, target_value):
  for idx in range(len(search_list)):
    if search_list[idx] == target_value:
      return idx
  raise ValueError("{0} not in list".format(target_value))

try:
  # Call the function below...
  result = linear_search(number_list, 100)
  print(result)
except ValueError as error_message:
  print("{0}".format(error_message))

#Finding Duplicate
# For each element in the searchList
  # if element equal target value then
    # Add its index to a list of occurrences
# if the list of occurrences is empty
  # raise ValueError
# otherwise
  # return the list occurrences

# Search list and target value
tour_locations = [ "New York City", "Los Angeles", "Bangkok", "Istanbul", "London", "New York City", "Toronto"]
target_city = "New York City"
#Linear Search Algorithm
def linear_search(search_list, target_value):
  matches = []
  for idx in range(len(search_list)):
    if search_list[idx] == target_value:
      matches.append(idx)
  if matches:
    return matches
  else:
    raise ValueError("{0} not in list".format(target_value))
#Function call
tour_stops = linear_search(tour_locations, target_city)
print(tour_stops)

#Finding the Maximum Value
# Create a variable called max_value_index    
# Set max_value_index to the index of the first element of the search list
     # For each element in the search list
          # if element is greater than the element at max_value_index
               # Set max_value_index equal to the index of the element
# return max_value_index

# Search list
test_scores = [88, 93, 75, 100, 80, 67, 71, 92, 90, 83]
#Linear Search Algorithm
def linear_search(search_list):
  maximum_score_index = None
  for idx in range(len(search_list)):
    if maximum_score_index == None or search_list[idx] > maximum_score_index:
      maximum_score_index = idx
  return maximum_score_index
# Function call
highest_score = linear_search(test_scores)
#Prints out the highest score in the list
print(highest_score)
