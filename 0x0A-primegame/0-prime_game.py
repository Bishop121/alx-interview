#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """Maria and Ben are playing a game.
    Given a set of consecutive integers starting from 1 up to and including n,
    they take turns choosing a prime number from the set and removing that
    number and its multiples from the set. The player that cannot make a move
    loses the game. They play x rounds of the game, where n may be different
    for each round. Assuming Maria always goes first and both players play
    optimally, determine who the winner of each game is.

    Args:
        x (int): number of rounds
        nums (list): an array of n
    """
    if not nums or x < 1:
        return None

    players = {'Maria': 0, 'Ben': 0}
    win = {}

    for i in range(x):
        limit = nums[i]
        if limit in win:
            if win[limit] == 'Ben':
                players['Ben'] += 1
            else:
                players['Maria'] += 1
            continue

        primes = sieve_of_eratosthenes(limit)
        full_nums = [j for j in range(1, nums[i] + 1)]

        firstPlayer = True
        while has_prime(full_nums):
            firstPlayer = not firstPlayer
            if firstPlayer:
                current_player = 'Maria'
            else:
                current_player = 'Ben'

            for prime in primes:
                if prime in full_nums:
                    full_nums = [num for num in full_nums if num % prime != 0]
                    break

        if firstPlayer:
            win[limit] = 'Ben'
            players['Ben'] += 1
        else:
            win[limit] = 'Maria'
            players['Maria'] += 1
    winner = max(players, key=players.get)
    return winner


def has_prime(lst):
    """Checks if a list contains a prime number.

    Args:
        lst: A list of integers.

    Returns:
        True if the list contains a prime number, False otherwise.
    """
    for n in lst:
        if n <= 1:
            continue
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                break
        else:
            return True
    return False


def sieve_of_eratosthenes(limit):
    """Implements the Sieve of Eratosthenes algorithm to find
        prime numbers up to a given limit.

    Args:
        limit: The upper limit for finding prime numbers.

    Returns:
        A list of prime numbers up to the given limit.
    """
    if limit < 2:
        return []
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(sqrt(limit)) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return [i for i in range(2, limit + 1) if primes[i]]


def sqrt(x):
    """Calculates the square root of a number using the Babylonian method.

    Args:
        x: The number to find the square root of.

    Returns:
        The square root of x as a float.
    """
    if x == 0:
        return 0

    guess = x / 2
    while abs(guess**2 - x) > 0.00001:
        guess = (guess + x / guess) / 2

    return guess
