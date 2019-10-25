
def climbingLeaderboard(scores, alice):
    new_position = []
    scores_sorted = sorted(set(scores), reverse = True)
    old_position = len(scores_sorted)
    for i in alice:
        while (old_position > 0) and (i >= scores_sorted[old_position-1]):
            old_position -= 1
        new_position.append(old_position + 1)
    return new_position

print(climbingLeaderboard([120,100,80,60],[40,67,80,130]))