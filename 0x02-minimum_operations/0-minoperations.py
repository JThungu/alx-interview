#!/usr/bin/python3
"""Module for minimum_operations"""


def minOperations(n)
    """
    min_operations_to_generate_h_characters
    Gets the fewest number of operations needed to result in exactly
    the specified number of 'H' characters
    """
    # Minimum input value for meaningful operations
    if n < 2:
        return 0

    n, divisor = 0, 2

    while divisor <= n:
        # Check if target_h_count evenly divides by divisor
        if n % divisor == 0:
            # Total even divisions by divisor equals total operations
            total_operations += divisor
            # Set target_h_count to the remainder
            n = n / divisor
            # Reduce divisor to find remaining smaller values that evenly divide target_h_count
            divisor -= 1

        # Increment divisor until it evenly divides target_h_count
        divisor += 1

    return total_operations
