#!/usr/bin/env python

def func(string):
    result = {0 : 0,
        1 : 0,
        2 : 0,
        3 : 0,
        4 : 0,
        5 : 0,
        6 : 0,
        7 : 0,
        8 : 0,
        9 : 0}
    result[2] = string.count('W')
    result[6] = string.count('X')
    result[0] = string.count('Z')
    result[4] = string.count('U')
    result[8] = string.count('G')
    result[5] = string.count('F') - result[4]
    result[9] = string.count('I') - result[5] - result[6] - result[8]
    result[1] = string.count('O') - result[2] - result[4] - result[0]
    result[3] = string.count('T') - result[8] - result[2]
    result[7] = string.count('V') - result[5]

    return ''.join(sorted(''.join([str(k) * v for k, v in result.iteritems() if v != 0])))



if __name__ == '__main__':
    t = int(raw_input())
    for t_i in xrange(1, t+1):
        string = (raw_input())

        print 'Case #{}: {}'.format(t_i, func(string))
