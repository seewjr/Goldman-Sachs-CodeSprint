import sys
import math

# Returns number of pairs in arr[0..n-1]
# with sum equal to 'sum'
def getPairsCount(arr):
    mode = [num%60 for num in arr]
    n =len(mode)
    m = [0] * 100000
    for i in range(0, n):
        m[mode[i]] += 1

    twice_count = 0

    for i in range(0, n):

        twice_count += m[60 - mode[i]]

        if (60 - mode[i] == mode[i]):
            twice_count -= 1
    count = twice_count/2
    if m[0] == 1 and m[0] ==0:
        return count
    elif m[0] == 2:
        return count+1
    elif m[0] >=3:
        fact_n = math.factorial(m[0])
        fact_n_2 = math.factorial(m[0]-2)
        count += fact_n/fact_n_2/2
        return count
    return count

print(getPairsCount([50,10,60]))