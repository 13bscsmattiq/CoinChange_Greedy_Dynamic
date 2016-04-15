def dynamicCoinChange( denoms, target ):
    Opt = [0 for i in range(0, target+1)]
    n = len(denoms)
    for i in range(1, target+1):
        smallest = float("inf")
        for j in range(0, n):
            if (denoms[j] <= i):
                smallest = min(smallest, Opt[i - denoms[j]]) 
            Opt[i] = 1 + smallest 
    return Opt[target]

problems = [
    [[1, 5, 10, 25],  30],
    [[1, 5, 10, 25],  220],
    [[1, 5, 10, 25],  300],
    [[1, 5, 10, 25],  440],
    [[1, 5, 10, 25],  550],
    [[1, 5, 10, 25],  600],
    [[1, 5, 10, 25],  745],
    [[1, 5, 10, 25],  920],
    [[1, 5, 10, 25],  978],
    [[1, 5, 10, 25],  1000]
]


for denoms, target in problems:
    S = dynamicCoinChange(denoms, target)
    print "Denoms =", denoms
    print "Target =", target
    print "No of minimum coins =", S

    
    
