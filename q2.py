# q2 Veyor take-home

from math import sqrt


def max_money(n, k):
    """
    Finds the maximum money that can be received for given 
    number of classmates, n, and unlucky number, k. See README
    for why this algorithm is correct. Runs in O(1) time and 
    uses O(1) space.
    """
    mod = 10**9 + 7
    max_dollars = (n * (n+1)) / 2
    i = (-1 + sqrt(1 + 8*k)) / 2
    if i.is_integer() and i <= n:
        return int((max_dollars - 1) % mod)
    return int((max_dollars) % mod)
 

if __name__ == '__main__':
    try:
        n = int(input())
        k = int(input())
    except ValueError:
        print('Please input integers only.')
        exit(1)
    else:
        print(max_money(n, k))
