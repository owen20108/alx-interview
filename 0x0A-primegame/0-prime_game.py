#!/usr/bin/python3
'''
Prime Game
'''

def get_primes(nums):
    '''
    Get the count of primes up to each number in nums
    '''
    n = max(nums)
    if n < 1:
        return None

    # Sieve of Eratosthenes
    prime = [True] * (n + 1)
    prime[0], prime[1] = False, False  # 0 and 1 are not prime numbers
    p = 2

    while (p * p <= n):
        if prime[p]:
            for j in range(p * p, n + 1, p):
                prime[j] = False
        p += 1

    # Create a list of prime counts up to each number in nums
    prime_cnt = []
    for num in nums:
        cnt = sum(prime[:num + 1])
        prime_cnt.append(cnt)

    return prime_cnt

def isWinner(x, nums):
    '''
    Determine the winner of the prime game
    '''
    if x <= 0 or nums is None or min(nums) < 0:
        return None

    prime_cnt = get_primes(nums)
    if prime_cnt is None:
        return None

    # Count the number of rounds won by Maria
    maria_wins = sum(1 for cnt in prime_cnt if cnt % 2 == 1)

    if maria_wins > x / 2:
        return "Maria"
    elif maria_wins < x / 2:
        return "Ben"
    else:
        return None

# Example usage
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

