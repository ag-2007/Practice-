catNames=[]

while True:
    print ('Enter the name of cat '+ str(len(catNames)+1) + ' (Or Press the space bar and enter key to stop.):')
    name=input()
    if name == ' ':
        break
    catNames=catNames+[name]   
print ('The cat names are:')
for name in catNames:
    print(' '+ name)
