# The Elves begin to set up camp on the beach. To decide whose tent gets to be closest to the snack storage, a giant Rock Paper Scissors tournament is already in progress.

# Rock Paper Scissors is a game between two players. Each game contains many rounds; in each round, the players each simultaneously choose one of Rock, Paper, or Scissors using a hand shape. Then, a winner for that round is selected: Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. If both players choose the same shape, the round instead ends in a draw.

# Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that they say will be sure to help you win. "The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.

# The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.

# The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

# Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you would get if you were to follow the strategy guide.



# get the data
day2_input = open("day2_input.txt")
rounds = day2_input.read()
each_round = rounds.split("\n")
day2_input.close()

# make the function
initial_score = 0
your_move_options = ["X", "Y", "Z"]
their_move_options = ["A", "B", "C"]
def calculate_points_pt1(data):
    # get the two moves
    move = data.split(" ")
    # add pts for your move
    score = (your_move_options.index(move[1]))+1

    # find the outcome
    your_move = your_move_options.index(move[1])
    their_move = their_move_options.index(move[0])
    win_conditions = {"0": "2", "1": "0", "2": "1"}

    # see if its a draw
    if your_move == their_move:
        score += 3
        return score 
    # see of you won
    if str(their_move) == win_conditions[str(your_move)]:
        score += 6
        return score
    # otherwise you lost
    else: return score

"""
final_score = 0
for i in each_round:
    final_score += calculate_points_pt1(i)
print(final_score)
"""

## pt2
results_move_options = ["X", "Y", "Z"]
def calculate_points_pt2(data):
    # get the two values
    move = data.split(" ")
    their_move = their_move_options.index(move[0])
    results = results_move_options.index(move[1])
    win_conditions = {"0": "2", "1": "0", "2": "1"}
    score = initial_score
    # find your move
    if results == 1:
                your_move = their_move # draw
                score += 3
    if results == 2: # win
        your_move = [k for k, v in win_conditions.items() if v == str(their_move)][0]
        score += 6
    if results == 0: # lose
        your_move = int(win_conditions[str(their_move)])
    
    # add pts for your move like pt1
    score += int(your_move)+1
    return score

final_score = 0
for i in each_round:
    final_score += calculate_points_pt2(i)
print(final_score)
