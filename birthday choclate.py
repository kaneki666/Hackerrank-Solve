
def birthday(s, d, m, n):
    s = [2,2,1,3,2]
    d = 4
    m = 2
    count = 0
    for i in range(n-m+1):
        if(sum(s[i:m+i])==d):
            count = count + 1
    return count
    print(count) 