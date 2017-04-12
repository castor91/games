#!/usr/bin/env python

def function(rows):
    tmp_rows = [item for sublist in rows for item in sublist]
    rows_dict = {n: tmp_rows.count(n) for n in set(tmp_rows)}
    missing_number = sorted([k for k, v in rows_dict.iteritems() if v % 2 != 0])
    return missing_number

if __name__ == '__main__':
    t = int(raw_input())
    for t_i in xrange(1, t+1):
        n = int(raw_input())
        rows = []
        for _ in xrange(2*n - 1):
            rows.append([int(x) for x in raw_input().split(' ')])
        result = function(rows)
        print 'Case #{}: {}'.format(t_i, ' '.join(map(str, result)))
