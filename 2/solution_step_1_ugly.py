
# I have a better idea lets swap Scissors with a Shotgun! Come here! lovely bastards XD LMAO

# INFOS

# 1 = Rock
# 2 = Paper
# 3 = Scissors or Shotgun

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
        case _:
            return 0

def result_check(a, b):

    if (a == b):
        
        return "draw"

    match a:

        case 1:

            if b == 3:
                
                return "win"

        case 2:

            if b == 1:
        
                return "win"
        
        case 3:
        
            if b == 2:
        
                return "win"
        
        case _:
        
            return 0

    return "lose"

def score_check(r):

    match r:
        case "win":
            return 6
        case "lose":
            return 0
        case "draw":
            return 3
        case _:
            return 0

# CODE

for line in lines:

    x = line.split(" ")
    x[1] = x[1].rstrip('\n')

    x[1] = letter_to_num(x[1])
    x[0] = letter_to_num(x[0])

    result = result_check(x[1], x[0])

    score = score_check(result)
    score += x[1]

    print("{} - Result: {} - Score: {}".format(x, result, score))

    total_score += score

print("Total Score: {}".format(total_score))
