def mirror_world(x:str):
    split_list = x.split()
    reversed_list=split_list[::-1]
    final= " ".join(reversed_list)
    return (final)

usr_inp=str(input("Enter a sentence and I shall reverse it : "))
mirror = mirror_world(usr_inp)
print(mirror)


