def isIsomorphic_2(s: str, t: str) -> bool:
    len_s = len(s)
    len_t = len(t)

    if len_s != len_t:
        return False

    d1, d2 = [0] * 256, [0] * 256
    i = 0
    while i < len_s:
        if d1[ord(s[i])] != d2[ord(t[i])]:
            return False
        d1[ord(s[i])] = i + 1
        d2[ord(t[i])] = i + 1
        i += 1

    return True


def isIsomorphic_3(s: str, t: str) -> bool:
    return len(set(zip(s, t))) == len(set(s)) and len(set(zip(t, s))) == len(set(t))


def isIsomorphic(s: str, t: str) -> bool:
    len_s = len(s)
    len_t = len(t)

    if len_s != len_t:
        return False

    mapping_s = {}
    mapping_t = {}

    i = 0

    while i < len_s:
        if (s[i] in mapping_s and mapping_s[s[i]] != t[i]) or (t[i] in mapping_t and mapping_t[t[i]] != s[i]):
            return False
        mapping_s.update({s[i]: t[i]})
        mapping_t.update({t[i]: s[i]})
        i += 1
    return True
