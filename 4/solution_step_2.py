
# Location! Location! Location! Clean that location!

input_file = open('input.txt', 'r')
lines = input_file.readlines()

parsed_lines = []
for line in lines:

    line = line.rstrip('\n')

    splitted_line = line.split(",")
    splitted_line[0] = splitted_line[0].split("-")
    splitted_line[1] = splitted_line[1].split("-")

    parsed_lines.append(splitted_line)

target_count = 0
for line in parsed_lines:

    print(line)

    found = 0

    for i in range(int(line[0][0]), int(line[0][1]) + 1):

        if i >= int(line[1][0]) and i <= int(line[1][1]) and found == 0:

            print("found")
            found = 1
            target_count += 1
            continue

print(target_count)