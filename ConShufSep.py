import random

with open("randomMultiIds.txt") as ids:
	id_array = ids.readlines()

id_array = [x.strip() for x in id_array]

with open("artistNames.txt") as names:
	name_array = names.readlines()

name_array = [x.strip() for x in name_array]

file = open("concat.txt","w")
i = 0
for id in id_array:
	file.write(str(id) + '-' + name_array[i] + "\n")
	i += 1
file.close()

lines = open("concat.txt").readlines()
random.shuffle(lines)
open("ConcatenatedAndShuffled.txt", "w").writelines(lines)


file2 = open("shuffledMultiIds.txt","w")
file3 = open("shuffledArtistNames.txt", "w")
with open("ConcatenatedAndShuffled.txt") as f:
	for line in f:
		key, value = line.strip().split("-")
		file2.write(key + "\n")
		file3.write(value + "\n")
file2.close()
file3.close()