def remove_duplicates(a : list):
    b=[]
    for element in a:
        if element not in b:
            b.append(element)
    return (b)


my_list=[1,1,2,2,4,5,8,7,5,6,6,3,8,9]
final= remove_duplicates(my_list)
print(final)