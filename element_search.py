def find(ordered_list, element_to_find):
  start_index = 1
  end_index = len(ordered_list) - 1
  
  while True:
    middle_index = (end_index - start_index) / 2
    
    if middle_index < start_index or middle_index > end_index or middle_index < 0:
      return False
    
    middle_element = ordered_list[middle_index]
    if middle_element == element_to_find:
      return True
    elif middle_element < element_to_find:
      end_index = middle_index
    else:
      start_index = middle_index
    