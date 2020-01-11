#!/usr/bin/python3

import argparse
import os

base_dir = os.getcwd()
join = os.path.join
exists = os.path.exists


def main(filename):
    with open(filename, 'r') as file:
        a = [int(x) for x in file]
    (a, a_count) = sort_and_count(a, len(a))
    print(a_count)


def sort_and_count(a, n):
    if n==1:
        return a, 0

    midway = n//2
    b = a[:midway]
    c = a[midway:]

    (b, b_count) = sort_and_count(b, len(b))
    (c, c_count) = sort_and_count(c, len(c))
    (a, split_count) = count_split_inversions(b, c, len(b), len(c))
    return a, b_count + c_count + split_count


def count_split_inversions(b, c, m, n):
    a =[]
    i = 0
    j = 0
    count = 0
    for k in  range(0,m + n):
        if i<m and j<n:
            if b[i] < c[j]:
                a.append(b[i])
                i += 1
            else:
                a.append(c[j])
                j += 1
                count += len(b) - i
        elif i<m:
            a.append(b[i])
            i += 1
        elif j<n:
            a.append(c[j])
            j += 1
    return a, count


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Count the inversions in an array of integers from a file")
    parser.add_argument('--filename', default='IntegerArray.txt')
    args = parser.parse_args()
    filename = args.filename
    main(filename)