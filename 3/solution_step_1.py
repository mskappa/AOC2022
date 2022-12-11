
# Damn disorganized elves, go back packing chocolate!

# 
# https://stackoverflow.com/a/5931537
alfa = "abcdefghijklmnopqrstuvwxyz"
rdict = dict([ (x[1],x[0]) for x in enumerate(alfa) ])
#
#

input_file = open('input.txt', 'r')
lines = input_file.readlines()
priority_total = 0

for line in lines:

    line = line.rstrip('\n')

    n_of_chars = len(line)
    half_of_characters = int(n_of_chars / 2)

    first_half = line[ 0 : half_of_characters]
    second_half = line[ half_of_characters : n_of_chars]

    x = [line, n_of_chars, first_half, second_half]
    print(x)

    common_item_types = []
    for c in list(first_half):

        if c in list(second_half):
            
            if c not in common_item_types:

                common_item_types.append(c)

                if c.islower():

                    priority = rdict[c] + 1
                    priority_total += priority
                    print("Letter: {} Priority: {}".format(c, priority))
                
                else:

                    priority = rdict[c.lower()] + 1 + 26
                    priority_total += priority
                    print("Letter: {} Priority: {}".format(c, priority))

            else:
            
                continue

print(priority_total)