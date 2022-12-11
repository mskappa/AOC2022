
# Damn disorganized elves, go back packing chocolate!

# 
# https://stackoverflow.com/a/5931537
alfa = "abcdefghijklmnopqrstuvwxyz"
rdict = dict([ (x[1],x[0]) for x in enumerate(alfa) ])

# CODE

input_file = open('input.txt', 'r')
lines = input_file.readlines()
priority_total = 0

clean_lines = []

for line in lines:

    line = line.rstrip('\n')
    clean_lines.append(line)

#
# https://www.geeksforgeeks.org/break-list-chunks-size-n-python/
def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

splitted_lines = divide_chunks(clean_lines, 3)

def find_common_letters(l):

    common_letters = []

    for c in list(l[0]):

        if c in list(l[1]) and c in list(l[2]) and c not in common_letters:

            common_letters.append(c)

    return common_letters

total_common_leters = []
for lines in splitted_lines:
    
    common_letters = find_common_letters(lines)

    for l in common_letters:
    
        total_common_leters.append(l)

    print("{} - Common letters: {}".format(lines, common_letters))    
    
print(total_common_leters)

priority_total = 0
for c in total_common_leters:

    if c.islower():

        priority = rdict[c] + 1
        priority_total += priority
        print("Letter: {} Priority: {}".format(c, priority))
    
    else:

        priority = rdict[c.lower()] + 1 + 26
        priority_total += priority
        print("Letter: {} Priority: {}".format(c, priority))

print(priority_total)