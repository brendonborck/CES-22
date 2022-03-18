#PROBLEM 4

def is_prime(n):

    if n == 1:

        return False

    for i in range(n-1):

        if (i+1) == 1:

            continue

        if n%(i+1) == 0:

            return False

    return True
