#!/usr/bin/env python

if __name__ == '__main__':
    t = int(raw_input())
    for i in xrange(1, t + 1):
        string = raw_input()
        result = string[0]
        for s in string[1:]:
            if s < result[0]: result += s
            else: result = s + result
        print 'Case #{}: {}'.format(i, result)
