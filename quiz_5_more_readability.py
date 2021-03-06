# Prompts the user for a nonnegative integer that codes a set S as follows:
# - Bit 0 codes 0
# - Bit 1 codes -1
# - Bit 2 codes 1
# - Bit 3 codes -2
# - Bit 4 codes 2
# - Bit 5 codes -3
# - Bit 6 codes 3
# ...
# Computes a derived nonnegative number that codes the set of running sums
# of the members of S when those are listed in increasing order.
#
# Computes the ordered list of members of a coded set.
#
# Written by *** and Eric Martin for COMP9021


import sys

try:
    # encoded_set = 9999999999999999999999
    encoded_set = int(input('Input a nonnegative integer: '))
    if encoded_set < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()


def display(L):
    print('{', end='')
    print(', '.join(str(e) for e in L), end='')
    print('}')


def decode(encoded_set):
    """
    >>> decode(0)
    []
    >>> decode(1)
    [0]
    >>> decode(2)
    [-1]
    >>> decode(3)
    [-1, 0]
    >>> decode(4)
    [1]
    >>> decode(5)
    [0, 1]
    >>> decode(6)
    [-1, 1]
    >>> decode(7)
    [-1, 0, 1]
    >>> decode(100)
    [-3, 1, 3]
    >>> decode(123)
    [-3, -2, -1, 0, 2, 3]
    >>> decode(1234)
    [-4, -1, 2, 3, 5]
    """
    list_encode_set = []
    str_bin = bin(encoded_set)[2:][::-1]
    for i in range(len(str_bin)):
        if int(str_bin[i]):
            d, m = divmod(i, 2)
            if m == 0:
                list_encode_set.append(d)
            else:
                list_encode_set.append((d + m) * -1)
    return sorted(list_encode_set)


def code_derived_set(encoded_set):
    n = 0
    set_derived = set()
    for i in encoded_set:
        n = n + i
        set_derived.add(n)
    result = 0
    for n in sorted(set_derived):
        if n < 0:
            result = pow(2, abs(n) * 2 - 1) + result
        else:
            result = pow(2, n * 2) + result
    return result


encoded_set = decode(encoded_set)

print('The encoded set is: ', end='')
display(encoded_set)

code_of_derived_set = code_derived_set(encoded_set)

print('The derived encoded set is: ', end='')
display(decode(code_of_derived_set))

print('It is encoded by:', code_of_derived_set)

