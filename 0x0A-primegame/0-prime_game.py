#!/usr/bin/python3
"""Module for solving prime game question"""

def isWinner(x, nums):
    """Function that determines the winner of the prime game"""
    
    if not nums or x < 1:
        return None
    
    max_num = max(nums)
    
    # Step 1: Generate the prime numbers using Sieve of Eratosthenes
    sieve = [True] * (max(max_num + 1, 2))
    sieve[0], sieve[1] = False, False  # 0 and 1 are not prime numbers
    
    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if sieve[i]:
            for j in range(i * i, max_num + 1, i):
                sieve[j] = False
    
    # Step 2: Create an array of prime counts up to each index
    prime_count = [0] * (max_num + 1)
    count = 0
    for i in range(len(sieve)):
        if sieve[i]:
            count += 1
        prime_count[i] = count
    
    # Step 3: Determine the number of rounds won by Maria
    maria_wins = 0
    for num in nums:
        if prime_count[num] % 2 == 1:
            maria_wins += 1
    
    # Step 4: Determine the overall winner
    if maria_wins > x / 2:
        return "Maria"
    elif maria_wins < x / 2:
        return "Ben"
    else:
        return None

# Example usage:
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

