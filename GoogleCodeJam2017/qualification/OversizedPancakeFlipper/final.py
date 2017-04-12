#!/usr/bin/env python

if __name__ == "__main__":
    t = int(raw_input())
    for case in xrange(1, t+1):
        s, k = [s for s in raw_input().split(' ')]
        s = list(s)
        k = int(k)
        ans = 0
        for i in range(len(s) - k + 1):
            if s[i] == "-":
                ans += 1
                for j in range(k):
                    s[i + j] = "-" if s[i + j] == "+" else "+"
        print 'Case #{}: {}'.format(case, ans if '-' not in s else 'IMPOSSIBLE')
