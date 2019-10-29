import math
def squares(a, b):
    n = math.ceil(math.sqrt(b))
    listt = []
    for i in range(1,n+1):
        sq = i*i
        if sq >= a and sq <= b:
            listt.append(sq)
    return len(listt)

print(squares(3,10))