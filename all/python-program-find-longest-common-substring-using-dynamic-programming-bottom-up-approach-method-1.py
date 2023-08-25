def lcw(u, v):
    """Return length of an LCW of strings u and v and its starting indexes.
�
    (l, i, j) is returned where l is the length of an LCW of the strings u, v
    where the LCW starts at index i in u and index j in v.
    """
    # c[i][j] will contain the length of the LCW at the start of u[i:] and
    # v[j:].
    c = [[-1]*(len(v) + 1) for _ in range(len(u) + 1)]
�
    for i in range(len(u) + 1):
        c[i][len(v)] = 0
    for j in range(len(v)):
        c[len(u)][j] = 0
�
    lcw_i = lcw_j = -1
    length_lcw = 0
    for i in range(len(u) - 1, -1, -1):
        for j in range(len(v)):
            if u[i] != v[j]:
                c[i][j] = 0
            else:
                c[i][j] = 1 + c[i + 1][j + 1]
                if length_lcw < c[i][j]:
                    length_lcw = c[i][j]
                    lcw_i = i
                    lcw_j = j
�
    return length_lcw, lcw_i, lcw_j
�
�
u = input('Enter first string: ')
v = input('Enter second string: ')
length_lcw, lcw_i, lcw_j = lcw(u, v)
print('Longest Common Subword: ', end='')
if length_lcw > 0:
    print(u[lcw_i:lcw_i + length_lcw])