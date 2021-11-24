# q2 Veyor take-home
# See README.md for why this algorithm is correct.

def max_money(n, k):
    """
    Finds the maximum money that can be received for given 
    number of classmates, n, and unlucky number, k.
    """
    mod = 10**9 + 7
    max_dollars = (n * (n+1)) / 2
    cum_sum = 0
    i = 1
    while i <= n:
        cum_sum += i
        if cum_sum == k:
            return int((max_dollars - 1) % mod)
        i += 1
    return int(max_dollars % mod)
 

if __name__ == '__main__':
    try:
        n = int(input())
        k = int(input())
    except ValueError:
        print('Please input integers only.')
        exit(1)    
    else:
        print(max_money(n, k))
    
    # print(max_money(2, 2))  # 3
    # print(max_money(2, 1))  # 2
    # print(max_money(3, 3))  # 5