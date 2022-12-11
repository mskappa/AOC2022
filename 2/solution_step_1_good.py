
# I have a better idea lets swap Scissors with a Shotgun! Come here! lovely bastards XD LMAO

# INFOS

# 1 = Rock
# 2 = Paper
# 3 = Scissors

# 6 = Win
# 3 = Draw
# 0 = Lose

# VARS

input_file = open('input.txt', 'r')
lines = input_file.readlines()
total_score = 0

# UTILITY FUNCTIONS

def letter_to_num(l):

    match l:

        case "X" | "A": # ROCK
            return 1
        case "Y" | "B": # PAPER
            return 2
        case "Z" | "C": # SCISSORS
            return 3

def calc_right_play(a):

    r = a + 2
    if r > 3:
        r = r - 3
    return r

def calc_result(me, opponent):

    if (me == opponent):
        
        return 3

    required_to_win = calc_right_play(me)

    if opponent == required_to_win:

        return 6

    else:

        return 0

# CODE

for line in lines:

    x = line.split(" ")
    x[1] = x[1].rstrip('\n')

    x[1] = letter_to_num(x[1])
    x[0] = letter_to_num(x[0])

    score = calc_result(x[1], x[0])
    score += x[1]

    total_score += score

print(total_score)