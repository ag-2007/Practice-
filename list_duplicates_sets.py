def remove_duplicates(a : list):
    return list(set (a))

my_list=[1,2,3,3,4,4,4,5,6,7,7,8,9]
final=remove_duplicates(my_list)
print(final)
