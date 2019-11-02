
def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1>y2:
        return 10000
    if y1==y2:
        if m1>m2:
            return (m1-m2)*500
        if m1==m2 and d1>d2:
            return (d1-d2)*15
    return 0
print(libraryFine(10,12,2017, 1,1 ,2017))