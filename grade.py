def grading_grades(grades):
    result = []
    for i in grades:
        if i >= 38:
            if i % 5 >= 3:
                i += (5 - (i % 5))
        result.append(i)
    return result
