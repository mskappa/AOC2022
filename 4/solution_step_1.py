
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

    if (int(line[0][0]) <= int(line[1][0]) and int(line[0][1]) >= int(line[1][1])):

        target_count += 1
        print(line)
        print("hey!")
        continue

    if (int(line[0][0]) >= int(line[1][0]) and int(line[0][1]) <= int(line[1][1])):

        target_count += 1
        print(line)
        print("hey!")
        continue

print(target_count)