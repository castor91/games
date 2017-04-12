#!/usr/bin/env python
import sys

def final_2(n):
    solution = set()
    tmp_n = n
    k = 1
    cont = 0
    while len(solution) < 10 and cont < 100:
        tmp_len = len(solution)
        solution.update([x for x in str(tmp_n)])
        k += 1
        tmp_n = n * k
        cont = cont + (1 if tmp_len == len(solution) else -cont)
    if cont == 100: return "INSOMNIA"
    return (k-1) * n


def final(n):
    solution = set()
    cont = 0
    while len(solution) < 10 and cont < 100:
        cont += 1
        tmp = len(solution)
        solution.update([x for x in str(n)])
        cont = cont + (1 if tmp == len(solution) else -cont )
        n *= 2
    if cont == 100: return "INSOMNIA"
    return n/2

if __name__ == '__main__':
    f = open(sys.argv[1], 'r')
    out = open(sys.argv[2], 'w')
    tot_number = f.readline()[:-1] #rimosso lo \n
    for i in range(1, int(tot_number) + 1):
        r = final_2(int(f.readline()[:-1]))
        out.write('Case #{}: {}\n'.format(i, r))
    f.close()
    out.close()
    print "FINITO"
