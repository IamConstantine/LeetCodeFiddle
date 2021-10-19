# https://leetcode.com/problems/is-subsequence/

def isSubsequence(s, t):
    len_s = len(s)
    len_t = len(t)

    i = j = 0

    while i < len_s and j < len_t:
        if s[i] == t[j]:
            i += 1
        j += 1

    return i == len_s


# NOTE: this is the solution that I first came up with without understanding complete requirements
# Here I assumed that there is multiple occurences of characters from s which is not the case
# Here I failed to clarify the requirments before I started solving it

def isSubsequence_not_right_version_for_this_case(s, t):
    len_s = len(s)
    len_t = len(t)

    def isSubsequenceInner(start_of_s, start_of_t, mem={}):
        if f'{start_of_s},{start_of_t}' in mem:
            return mem[f'{start_of_s},{start_of_t}']

        if len_s == start_of_s:
            return True

        if len_t == start_of_t:
            return False

        len_of_s = len(s[start_of_s])
        len_of_t = len(t[start_of_t])

        if len_of_s > len_of_t:
            return False

        if s[start_of_s] == t[start_of_t]:
            start_of_s = start_of_s + 1

        start_of_t = start_of_t + 1

        find = isSubsequenceInner(start_of_s, start_of_t)

        mem[f'{start_of_s},{start_of_t}'] = find
        return find

    return isSubsequenceInner(0, 0)
