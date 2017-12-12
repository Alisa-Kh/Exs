##########################################
# FILE : ex7.py
# WRITER : Alisa, alisa, 332678291
# EXERCISE : intro2cs ex7 2017-2018
# DESCRIPTION: 5 simple functions that use
# a recursion, and the hanoi game
##########################################


def print_to_n(n):
    """Prints all the numbers from 1 to n"""
    if n < 1:
        return
    print_to_n(n - 1)
    print(n)


def print_reversed(n):
    """Prints numbers from n to 1"""
    if n < 1:
        return
    print(n)
    print_reversed(n - 1)


def has_divisor_smaller_than(n, i):
    """Checks whether there are divisors smaller than n / 2"""
    if i > 1:
        if n % i == 0:
            return True
        return has_divisor_smaller_than(n, i - 1)
    else:
        return False


def is_prime(n):
    """Check whether the number is prime and returns a boolean value. Uses additional function:
    has_divisor_smaller_than(n, i)"""
    if n <= 2:
        return True
    return not has_divisor_smaller_than(n, int(n / 2))


def find_divisors(n, d, primers):
    """Recursive function, finds all the divisors of a given number and
    appends them to a list"""
    if d != 0:
        if n % d == 0:
            primers.append(d)
        find_divisors(n, d - 1, primers)


def divisors(n):
    """Uses recursive function "find_divisors" to find all the divisors, and returns a list
    of them"""
    primers = []
    if n > 0:
        primers.append(n)
        d = int(n / 2)
        find_divisors(n, d, primers)
    return primers


def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


def exp_n_x(n, x):
    """Calculate a value of exp in x degree???"""
    if n == 0 or x == 0:
        return 1
    return x**n / factorial(n) + exp_n_x(n - 1, x)

# Part 2 - Play Hanoi


def play_hanoi(hanoi, n, src, dest, temp):
    if n == 2:
        hanoi.move(src, temp)
        hanoi.move(src, dest)
        hanoi.move(temp, dest)
    elif n == 1:
        hanoi.move(src, dest)
    elif n <= 0:
        return
    else:
        play_hanoi(hanoi, n - 1, src, temp, dest)
        hanoi.move(src, dest)
        play_hanoi(hanoi, n - 1, temp, dest, src)


def bin_helper(n, i, seq_template):
    if i == len(seq_template):
        print(''.join(seq_template))
    else:
        seq_template[i] = '0'
        bin_helper(n, i + 1, seq_template)
        seq_template[i] = '1'
        bin_helper(n, i + 1, seq_template)


def print_binary_sequences(n):
    bin_seq = ['0'] * n
    if n > 0:
        bin_helper(n, 0, bin_seq)
    else:
        return ''


def sequence_helper(char_list, i, k, seq_temp):
    


def print_sequences(char_list, n):
    seq = ['0'] * n
    if n > 0:
        sequence_helper(char_list, 0, 0, seq)


def print_no_repetition_sequences(char_list, n):
    pass


def no_repetition_sequences_list(char_list, n):
    pass

