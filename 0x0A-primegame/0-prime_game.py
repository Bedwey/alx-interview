#!/usr/bin/python3
"""
Prime Game Module.

This module contains the implementation
of a prime game. The game is played in `x` rounds, 
with each round having a maximum prime number.
The `isWinner` function determines the winner 
of the game based on the rules of the game.

Functions:
    isWinner(x, nums): Determines the winner
    of a prime game session.

Example:
    To use this module, import it and call
    the `isWinner` function:

        import prime_game
        winner = prime_game.isWinner(3, [5, 6, 7])
        print(winner)  # Outputs: 'Maria'
        or 'Ben' or None

This module requires Python 3.5 or later.
"""


def isWinner(x, nums):
    """
    Determines the winner of a prime game session
    with `x` rounds.

    Parameters:
    x (int): The number of rounds in the game.
    nums (list): A list of integers representing the maximum
    prime number for each round.

    Returns:
    str: The name of the winner ('Maria' or 'Ben') or None
    if there's a tie.
    """
    if x < 1 or not nums:
        return None
    marias_wins, bens_wins = 0, 0
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'