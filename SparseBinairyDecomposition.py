'''
my own submission to the Sparse Binairy Decomposition problem
'''
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def to_bin_int(list_bin_n):
    str_n = ''.join(n for n in list_bin_n)
    return int(str_n, 2)


def solution(N):
    n = "{0:b}".format(N)

    binary_n = list(str(n))
    binary_r = ['0' for i in range(len(binary_n))]

    for i in range(len(binary_n) -1):
        if binary_n[i] == '1':
            if binary_n[i + 1] == '1':
                binary_n[i + 1] = '0'
                binary_r[i + 1] = '1'

    return to_bin_int(binary_n)
