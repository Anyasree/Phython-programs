import sys

MOD = 998244353

def mul(a, b):
    c = [[0] * 3 for i in range(3)]
    for i in range(3):
        ai = a[i]
        for k in range(3):
            if ai[k]:
                t = ai[k]
                bk = b[k]
                c[i][0] = (c[i][0] + t * bk[0]) % MOD
                c[i][1] = (c[i][1] + t * bk[1]) % MOD
                c[i][2] = (c[i][2] + t * bk[2]) % MOD
    return c

def mpow(e):
    res = [[1,0,0],[0,1,0],[0,0,1]]
    mat = [
        [2,2,MOD-2],
        [1,0,0],
        [0,1,0]
    ]
    while e:
        if e & 1:
            res = mul(res, mat)
        mat = mul(mat, mat)
        e >>= 1
    return res

def solve(n):
    if n == 1:
        return 2
    if n == 2:
        return 12
    if n == 3:
        return 30
    m = mpow(n - 3)
    return (
        m[0][0] * 30 +
        m[0][1] * 12 +
        m[0][2] * 2
    ) % MOD

input = sys.stdin.readline

t = int(input())
for i in range(t):
    print(solve(int(input())))

