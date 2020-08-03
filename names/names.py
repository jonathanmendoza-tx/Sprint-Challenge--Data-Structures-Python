import time

from singly_linked_list import *

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replaced the nested for loops with improvements
# Original nested loops would yield a quadriatic runtime: O(n^2)

all_names =list(set(names_1) )+ list(set(names_2))
all_names.sort()

storage = LinkedList()

for name in all_names:
	storage.add_to_tail(name)

cur_node = storage.head

while cur_node.next_node is not None:

	if cur_node.value == cur_node.next_node.value:
		duplicates.append(cur_node.value)

	cur_node = cur_node.get_next()
	
#achieved 0.058 seconds runtime with singly linked list method

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
# ------------------------------------

##I achieved a runtime of 0.02 seconds with the following code:


# index = 0 

## code running is inspired from the singly linked list method we learned
# while index < len(all_names)-1:

# 	if all_names[index] == all_names[index+1]:

# 		duplicates.append(all_names[index+1])
# 		index += 1

# 	index += 1