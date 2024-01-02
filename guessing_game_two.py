def find(ordered_list):
  start_index = 0
  end_index = len(ordered_list) - 1
  guesses=0
  
  while True:
    middle_index = (end_index + start_index) // 2
    middle_element = ordered_list[middle_index]
    print(middle_element)
    usr_reply=input('Enter too high, too low or correct : ')
    if usr_reply == "correct":
      print("Yay!! I guessed it in "+str(guesses)+" tries")
      break
    elif usr_reply=="too high":
      end_index = middle_index
    elif usr_reply=="too low":
      start_index = middle_index
    guesses+=1

print("Let's play the guessing game, pick a number between 1 and 100 and I'll guess it")
a=[x for x in range(100)]
find(a)





    