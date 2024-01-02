def mirror_world(x:str):
    return (" ".join(x.split()[::-1]))

usr_inp=str(input("Enter a sentence and I shall reverse it : "))
mirror = mirror_world(usr_inp)
print(mirror)
