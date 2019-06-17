def poisonousPlants(arr):
    s=[len(arr)-1] #stack s stores plant indices from right to left
    killc=[0 for i in arr] #no of days it takes ith plant to kill all plants at its right side
    for i in range(len(arr)-2,-1,-1):
        while len(s)>0 and arr[i]<arr[s[-1]]:
            out=s.pop()
            if killc[out]>killc[i]: killc[i]=killc[out]
            else:killc[i]+=1
        s.append(i)
    return max(killc)