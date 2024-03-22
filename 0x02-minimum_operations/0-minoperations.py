#!/usr/bin/python3
'''The minimum operations coding challenge.
'''


def minOperations(n):
    '''Computes the fewest number of operations needed to result
    in exactly n H characters in a text editor. The operations are:
    1. Copy All
    2. Paste

    Parameters:
    n (int): The target number of 'H' characters.

    Returns:
    ops_count (int): The minimum number of operations to reach n 'H' characters.
    '''

    # Check if input is an integer
    if not isinstance(n, int):
        return 0

    ops_count = 0  # Initialize operations count
    # Initialize clipboard (stores the current number of 'H' characters)
    clipboard = 0
    done = 1  # Initialize 'done' with 1 'H' character already in the text editor

    # Loop until 'done' is less than target 'n'
    while done < n:
        if clipboard == 0:
            # The first operation is always a copy all and paste
            clipboard = done
            done += clipboard
            ops_count += 2
        elif n - done > 0 and (n - done) % done == 0:
            # If the remaining 'H' characters needed is a multiple of 'done',
            # perform a copy all and paste
            clipboard = done
            done += clipboard
            ops_count += 2
        elif clipboard > 0:
            # If clipboard is not empty, perform a paste
            done += clipboard
            ops_count += 1

    return ops_count  # Return the minimum number of operations
