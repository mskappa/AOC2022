
# Still no boozie on my sight, Grrrrrrr

input_file = open('input.txt', 'r')
lines = input_file.readlines()

calories_sum = 0
tot_calories_list = []

for line in lines:

    if not line.strip():

        tot_calories_list.append(calories_sum)
        calories_sum = 0

    else:

        calories_sum += int(line.strip())

tot_calories_list.append(calories_sum)
tot_calories_list.sort(reverse = True)

print()
print(tot_calories_list)

solution = tot_calories_list[0] + tot_calories_list[1] + tot_calories_list[2]

print()
print("solution: {}\n".format(solution))