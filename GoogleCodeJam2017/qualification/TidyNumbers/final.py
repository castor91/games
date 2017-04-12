#!/usr/bin/env python

def d(n):
    l = map(int, list(str(n)))
    while True:
        flag = False
        for i in range(1,len(l)):
            if l[i] < l[i-1]:
                l[i-1] = l[i-1] - 1
                for j in range(i, len(l)): l[j] = 9
                flag = True
        if not flag:
            return int(''.join(map(str, l)))


def c(n):
    sort_n = int(''.join(sorted(str(n))))
    for i in xrange(n, sort_n, -1):
        if int(''.join(sorted(str(i)))) == i: return i
    return sort_n

if __name__ == '__main__':
    t = int(raw_input())
    for i in xrange(1, t + 1):
        n = [int(s) for s in raw_input().split(" ")][0]
        print 'Case #{}: {}'.format(i, d(n))

