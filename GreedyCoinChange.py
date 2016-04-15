def GreedyCoinChange(denoms, target):
    def min_coins(i, aC):
        if aC == 0:
            return 0
        elif i == -1 or aC < 0:
            return float('inf')
        else:
            return min(min_coins(i-1, aC), 1 + min_coins(i, aC-denoms[i]))
    return min_coins(len(denoms)-1, target)

problems = [
    [[1, 5, 10, 25],  30],
    [[1, 5, 10, 25],  100],
    [[1, 5, 10, 25],  220],
    [[1, 5, 10, 25],  300],
    [[1, 5, 10, 25],  460],
    [[1, 5, 10, 25],  550],
    [[1, 5, 10, 25],  600],
    [[1, 5, 10, 25],  720],
    [[1, 5, 10, 25],  740],
    [[1, 5, 10, 25],  800]
]

for denoms, target in problems:
    S = GreedyCoinChange(denoms, target)
    print "Denoms =", denoms
    print "Target =", target
    print "No of minimum coins =", S
