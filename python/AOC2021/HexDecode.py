binary_str = bin(int(x := open('./inputs/HexDecode').read()[:-1], 16))[2:].zfill(len(x) * 4)

split_array = lambda d, n: (d[:n], d[n:])
extract_bits = lambda d, n: (int((D := split_array(d, n))[0], 2), D[1])


def multiply(v):
    p = 1
    for i in v:
        p *= i
    return p


def P(d):
    v, d = extract_bits(d, 3);
    t, d = extract_bits(d, 3)
    if t == 4:
        n, p = "", 1
        while p:
            p, d = extract_bits(d, 1)
            N, d = split_array(d, 4)
            n += N
        return int(n, 2), v, d
    S = []
    L, d = extract_bits(d, 1)
    if L:
        l, d = extract_bits(d, 11)
        for i in range(l):
            V, Z, d = P(d)
            S += [V]
            v += Z
    else:
        l, d = extract_bits(d, 15)
        s, d = split_array(d, l)
        while len(s) and int(s, 2):
            V, Z, s = P(s)
            S += [V]
            v += Z
    return [sum, multiply, min, max, 4, lambda x: x[0] > x[1], lambda x: x[0] < x[1], lambda x: x[0] == x[1]][t](S), v, d


print((x := P(binary_str))[1], x[0])
