# Define a procedure, find_second, that takes
# two strings as its inputs: a search string
# and a target string. It should return a
# number that is the position of the second
# occurrence of the target string in the
# search string.

def find_second(search_string,target_string):
    start_search = search_string.find(target_string) +1
    return search_string.find(target_string,start_search)


#marker_start = (line.find(marker))
#marker_end = (line.find(marker) + len(marker))

#print (marker_start, marker_end)
#replaced = line[:marker_start] + replacement + line[marker_end:]
#print(replaced)'''

danton = "De l'audace, encore de l'audace, toujours de l'audace"
print find_second(danton, 'audace')
#>>> 25

twister = "she sells seashells by the seashore"
print find_second(twister,'she')
#>>> 13
