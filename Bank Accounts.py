#!/bin/python3

import sys

def feeOrUpfront(n, k, x, d, p):

    if __name__ == "__main__":
        q = int(input().strip())
        for a0 in range(q):
            n, k, x, d = input().strip().split(' ')
            n, k, x, d = [int(n), int(k), int(x), int(d)]
            p = list(map(int, input().strip().split(' ')))
            result = feeOrUpfront(n, k, x, d, p)
            print(result)


