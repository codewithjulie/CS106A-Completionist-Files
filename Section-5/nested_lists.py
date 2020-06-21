def enumerate(lst):
    """
    returns a nested list where each element is a list containing 
    the index of an element in the original list and the element itself. 
    These lists should appear in increasing order of indices.

    >>> enumerate(['cs106a', 'is', 'super', 'fun'])
    [[0, 'cs106a'], [1, 'is'], [2, 'super'], [3, 'fun']]
    >>> enumerate(['hello'])
    [[0, 'hello']]
    >>> enumerate([])
    []
    """
    new_lst = []
    for i in range(len(lst)):
        embed_lst = [i, lst[i]]
        new_lst.append(embed_lst)
    return new_lst


def matrix_constant_multiply(c, m):
    """
    Multiplies the 2-dimensional matrix m (represented as a list of lists)
    by a constant factor c and returns the result. m should not be modified.

    >>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> matrix_constant_multiply(2, m)
    [[2, 4, 6], [8, 10, 12], [14, 16, 18]]
    """
    multiplied_matrix = []
    for row in m:
        multiplied_row = []
        for elem in row:
            elem *= c
            multiplied_row.append(elem)
        multiplied_matrix.append(multiplied_row)
    return multiplied_matrix


def matrix_add(m1, m2):
    """
    Adds matrices m1 and m2 together and returns the result. m1 and m2 are
    guaranteed to be the same size. Neither m1 nor m2 should be modified.

    >>> m1 = [[1, 2], [3, 4], [5, 6]]
    >>> m2 = [[2, 3], [4, 5], [6, 7]]
    >>> matrix_add(m1, m2)
    [[3, 5], [7, 9], [11, 13]]
    """
    row = len(m1)
    col = len(m1[0])
    m1_m2_added = []
    for i in range(row):
        row1_row2_added = []
        for j in range(col):
            row1_row2_added.append(m1[i][j]+m2[i][j])
        m1_m2_added.append(row1_row2_added)
    return m1_m2_added


def make_times_table(m, n):
    """
    Makes and returns a list of m rows, each with n columns.
    Each element is found by multiplying its row number by
    its column number, where we start counting rows and columns
    from 1.

    >>> make_times_table(3, 4)
    [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12]]
    """
    lst = []
    for i in range(1, m+1):
        row = []
        for j in range(1, n+1):
            elem = i * j
            row.append(elem)
        lst.append(row)
    return lst


def main():
    m1 = [[1, 2], [3, 4], [5, 6]]
    m2 = [[2, 3], [4, 5], [6, 7]]
    new_lst = make_times_table(3, 4)
    print(new_lst)


if __name__ == "__main__":
    main()
