def factors(n): # traditional function that computes factors
    results = [ ] # store factors in a new list
    for k in range(1,n+1):
        if n % k == 0: # divides evenly, thus k is a factor
            results.append(k) # add k to the list of factors
    return results


def factors_of_num(n): # generator that computes factors
    for k in range(1, n+1):
        if n % k == 0: # divides evenly, thus k is a factor
            yield k


def factors_of(n): # generator that computes factors
    k=1
    while k * k < n: # while k < sqrt(n)
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n: # special case if n is perfect square
        yield k


def factors_list(n):
    return [k for k in range(1, n+1) if n % k == 0]


def main():
    a = factors(12)
    print(a)
    print("".center(20, '-'))

    b = factors_of_num(63)
    for i in b:
        print(i)
    print("".center(20, '-'))


    c = factors_of(42)
    for i in c:
        print(i)
    print("".center(20, '-'))

    d = factors_list(56)
    print(d)


if __name__ == '__main__':
    main()
