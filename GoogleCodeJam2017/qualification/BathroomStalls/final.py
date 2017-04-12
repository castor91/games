#!/usr/bin/env python
import sys
from math import log, ceil, floor

def main2(n,k):
    cont = 1
    while k > 0 and k - cont > 0:
        k -= cont
        cont *= 2
        n /= 2


    r = 0
    return (max(l,r),min(l,r))


def main(n, k):
    if n <= k: return (0,0)
    sol = [(0,n+1)]
    for i in range(1, n+1):
        l, r = sol[i-1]
        sol.append((l + 1, r - 1))
    sol += [(n+1,0)]

    return_l, return_r = 0, 0

    while k > 0:
        pos = []
        tmp_min = 0
        tmp_max = n+1
        for i in xrange(len(sol)):
            pp = min(sol[i][0], sol[i][1])
            if pp > tmp_min:
                tmp_min = pp
                pos = [i]
            elif pp == tmp_min:
                pos.append(i)


        current_pos = pos[0]
        for i in pos:
            if max(sol[i][0], sol[i][1]) > max(sol[current_pos][0], sol[current_pos][1]):
                current_pos = i
        tmp_sol = sol
        tmp_sol[current_pos] = (0,0)

        for i in range(current_pos - 1, -1, -1):
            if tmp_sol[i][0] == 0 and tmp_sol[i][1] == 0: break
            tmp_sol[i] = tmp_sol[i][0], tmp_sol[i+1][1] +1

        for i in range(current_pos + 1, len(tmp_sol)):
            if tmp_sol[i][0] == 0 and tmp_sol[i][1] == 0: break
            tmp_sol[i] = tmp_sol[i-1][0] + 1, tmp_sol[i][1]

        sol = tmp_sol
        return_l = max(sol[current_pos - 1][0], sol[current_pos + 1][1])
        return_r = min(sol[current_pos - 1][0], sol[current_pos + 1][1])

        k -= 1

    return (return_l, return_r)

if __name__ == '__main__':
    t = int(raw_input())
    for i in xrange(1, t + 1):
        n, k = [int(s) for s in raw_input().split(" ")]
        l, r = main2(n,k)
        print 'Case #{}: {} {}'.format(i, l ,r)

