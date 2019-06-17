def array_advanced(A):
    furthest_reached = 0
    last_index = len(A) - 1
    i = 0
    while i <= furthest_reached and furthest_reached < last_index:
        furthest_reached = max(furthest_reached,A[i] + i)
        i += 1
    if furthest_reached >= last_index:
        print("It's Reachable.")
    else:
        print("It's not Reachable.")

A1 = [3,3,1,0,2,0,1]
A2 = [3,2,0,0,2,0,1]
##array_advanced(A1)
array_advanced(A1)