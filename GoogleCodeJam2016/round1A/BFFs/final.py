#!/usr/bin/env python

def function(bffs, n):
    result = []
    for i in xrange(n):
        circle = []
        cont = 0
        circle.append(i)
        while bffs[circle[-1]] not in circle:
            circle.append(bffs[circle[-1]])
            cont += 1 + (1 if circle[-2] == bffs[circle[-1]] else 0)
            if bffs[circle[-1]] in circle:
                for n in xrange(len(bffs)):
                    if circle[-1] == bffs[n] and n not in circle:
                        circle.append(n)
                        cont += 1
        if bffs[circle[-1]] == circle[0]:
            cont += 1
        result.append(cont)



    return result

if __name__ == '__main__':
    t = int(raw_input())
    for t_i in xrange(1, t+1):
        n = int(raw_input())
        bffs = ([int(x) - 1 for x in raw_input().split(' ')])
        result = max(function(bffs, n))
        print 'Case #{}: {}'.format(t_i, result)
