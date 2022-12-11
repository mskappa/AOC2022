
# Damn Elf u gave me wrong informations, i will find you and than.... huahuauha

# INFOS

# A or 1 = Rock
# B or 2 = Paper
# C or 3 = Scissors

# X = Must lose
# Y = Must draw
# Z = Must win

# 6 = Win
# 3 = Draw
# 0 = Lose

# VARS

input_file = open('input.txt', 'r')
lines = input_file.readlines()
total_score = 0

def letter_to_num(l):

    match l:

        case "A": # ROCK
            return 1
        case "B": # PAPER
            return 2
        case "C": # SCISSORS
            return 3

def calc_right_play(a, mod):

    r = a + mod
    if r > 3:
        r = r - 3
    return r


def calc_right_play_score(a, b):

    if b == "X": # LOSE
        return calc_right_play(a, 2) + 0

    if b == "Y": # DRAW
        return a + 3

    if b == "Z": # WIN
        return calc_right_play(a, 1) + 6

    return "?"

for line in lines:

    x = line.split(" ")
    x[1] = x[1].rstrip('\n')

    x[0] = letter_to_num(x[0])

    right_play_score = calc_right_play_score(x[0], x[1])

    total_score += right_play_score

    print("{} - {}".format(x, right_play_score))

print(total_score)