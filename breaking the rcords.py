def breaking_the_record(score):
    max = min = score[0]
    max_count = 0
    min_count = 0
    for i in score[1:]:
        if i > max:
            max_count += 1
            max = i
        if i < min:
            min_count += 1
            min = i
    return max_count,min_count

