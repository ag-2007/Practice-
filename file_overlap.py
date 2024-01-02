happy='d:/Anika Gupta/Others/IAMNEO/Coding/Practice python/Exercises/file_overlap/happy.txt'
prime='d:/Anika Gupta/Others/IAMNEO/Coding/Practice python/Exercises/file_overlap/prime.txt'

primes_list=[]
with open(prime, 'r') as prime_file:
    line = prime_file.readline()
    while line:
        primes_list.append(int(line))
        line = prime_file.readline()


happy_list=[]
with open(happy, 'r') as happy_file:
    line = happy_file.readline()
    while line:
        happy_list.append(int(line))
        line = happy_file.readline()
    

overlap_list = []
for elem in primes_list:
	if elem in happy_list:
		overlap_list.append(elem)
		
print(overlap_list)