def isWinner(x, nums):
    """Function to calculate all primes up to the maximum n in nums
using Sieve of Eratosthenes"""
    def sieve_of_eratosthenes(max_n):
        is_prime = [True] * (max_n + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
        for i in range(2, int(max_n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, max_n + 1, i):
                    is_prime[j] = False
        return is_prime

    # Function to determine the winner for a single round
    def simulate_game(n, is_prime):
        primes = [i for i in range(1, n + 1) if is_prime[i]]
        count = 0  # Number of prime picks
        for prime in primes:
            if n < prime:  # If no more primes to pick, end
                break
            count += 1
            # Simulate removing multiples of the chosen prime
            for multiple in range(prime, n + 1, prime):
                is_prime[multiple] = False
        return "Maria" if count % 2 == 1 else "Ben"

    if x < 1 or not nums:
        return None

    # Precompute prime numbers up to the maximum number in nums
    max_n = max(nums)
    is_prime = sieve_of_eratosthenes(max_n)

    # Count wins for each player
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Copy the prime state for the game
        game_primes = is_prime[:]
        winner = simulate_game(n, game_primes)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
