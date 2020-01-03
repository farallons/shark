#!/usr/bin/python3

import argparse


def main(x, y, algo):
    if algo:
        print("algo")
        product = calculate_product(x,y)
    else:
        print("no algo")
        product = x * y
    print(product)


def bits(a):
    return [int(bit) for bit in format(a, 'b')]


def smallest_multiple_of_two(n):
    i = 0
    n -= 1
    m = 1
    while n > 0:
        n >>= 1
        i += 1
        m <<= 1
    return m


def left_pad(a, n):
    return [0]*(n-len(a)) + a


def calculate_product(x, y):
    x = bits(x)
    y = bits(y)

    if len(y) > len(x):
        x, y = y, x

    n = smallest_multiple_of_two( len(x) )

    x = left_pad(x, n)
    y = left_pad(y, n)

    return karatsuba(x, y, n)


def add(a, b, n):
    c = [0]*n
    carry = False
    for i in range(0,n):
        index = n - i - 1
        sum = a[index] + b[index]
        if carry:
            sum += 1
        if sum > 1:
            carry = True
            c[index] = sum - 2
        else:
            carry = False
            c[index] = sum
    return carry, c


def add_zeroes_on_right(x, n):
    while n > 0:
        x <<= 1
        n -= 1
    return x


def number(a):
    n = len(a)
    acc = 0
    for i in range(0, len(a)):
        acc <<= 1
        if a[i] == 1:
            acc += 1
    return acc


def karatsuba(x, y, n):
    if n == 1:
        return x[0] * y[0]
    else:
        n >>= 1
        a = x[:n]
        b = x[n:]
        c = y[:n]
        d = y[n:]

        ac = karatsuba(a, c, n)
        bd = karatsuba(b, d, n)

        step1 = ac
        step2 = bd

        carry_a_b, sum_a_b = add(a, b, n)
        carry_c_d, sum_c_d = add(c, d, n)

        partial_product = karatsuba(sum_a_b, sum_c_d, n)
        if carry_a_b and carry_c_d:
            product3 = add_zeroes_on_right(1, n<<1) + add_zeroes_on_right(number(sum_a_b), n) + add_zeroes_on_right(number(sum_c_d), n) + partial_product
        elif carry_a_b:
            product3 = add_zeroes_on_right(number(sum_c_d), n) + partial_product
        elif carry_c_d:
            product3 = add_zeroes_on_right(number(sum_a_b), n) + partial_product
        else:
            product3 = partial_product
        step3 = product3

        step4 = step3 - step1 - step2

        step5 = add_zeroes_on_right(step1, n<<1) + add_zeroes_on_right(step4, n) + step2

        return step5


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Calculate the product of two numbers using Karatsuba's algorithm")
    parser.add_argument('x', type=int)
    parser.add_argument('y', type=int)
    parser.add_argument('--no_algo', action="store_true")
    args = parser.parse_args()
    x = args.x
    y = args.y
    no_algo = args.no_algo
    main(x, y, not no_algo)