names={'Darth':0, 'Luke':0, 'Lea':0}
darth_counter = names['Darth']
luke_counter=names['Luke']
lea_counter=names['Lea']
filepath= 'D:/Anika Gupta/Others/IAMNEO/Coding/Practice python/Exercises/read_from_file/list_to_use.txt'
with open(filepath, 'r') as open_file:
    line = open_file.readline()
    while line:
        line = line.strip()
        if line=='Darth':
            darth_counter+=1
            names['Darth']=darth_counter
        elif line=='Luke':
            luke_counter+=1
            names['Luke']=luke_counter
        elif line=='Lea':
            lea_counter+=1
            names['Lea']=lea_counter
        line = open_file.readline()
        
        

print(names)