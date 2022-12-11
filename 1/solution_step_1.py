
# Damn elves >:( gimme boozie !!!

input_file = open('input.txt', 'r')
lines = input_file.readlines()

somma = 0
max = 0

for line in lines:

    if not line.strip():

        print("tot: "+str(somma))
        print("--\n")

        if somma > max:
            max = somma

        somma = 0

    else:

        somma += int(line.strip())

        print("{}".format(line.strip()))


print("tot: "+str(somma))
print("--\n")

if somma > max:
    max = somma

print()
print("solution: {}\n".format(max))
