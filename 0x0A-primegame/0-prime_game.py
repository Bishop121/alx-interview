#!/usr/bin/python3
""" select winner prime game"""


def isWinner(x, nums):
    """Determine the winner of the prime game."""
    if not nums or x < 1:
        return None

    # Precompute primes using Sieve of Eratosthenes
    max_n = max(nums)
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime
    for i in range(2, int(max_n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_n + 1, i):
                sieve[j] = False

    # Precompute the number of primes up to each index
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if sieve[i] else 0)

    # Determine the winner for each round
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        # Count primes up to n
        primes_up_to_n = prime_count[n]
        if primes_up_to_n % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
