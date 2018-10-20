#!/bin/python3

import sys
import math

def buyMaximumProducts(n, k, a):
    # Complete this function
    total_price = k
    count = 0
    count_per_price = 1
    while count_per_price != 0:
        lowest_price = min(a)
        if lowest_price == 200:
            return count
        lowest_indicies = [index for index, element in enumerate(a) if element == lowest_price]
        count_per_price = min(sum(lowest_indicies)+len(lowest_indicies), math.floor(total_price / lowest_price))
        count += count_per_price
        for index in lowest_indicies:
            a[index] = 200
        total_price = total_price - count_per_price * lowest_price

    return count

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    k = int(input().strip())
    result = buyMaximumProducts(n, k, arr)
    print(result)