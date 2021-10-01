from typing import List


# https://leetcode.com/explore/interview/card/google/66/others-4/3097/

def candy(ratings: List[int]) -> int:
    length_of_ratings = len(ratings)
    l_to_r = [1] * length_of_ratings

    for i in range(length_of_ratings - 1):
        if ratings[i] > ratings[i + 1] and l_to_r[i] <= l_to_r[i + 1]:
            l_to_r[i] = l_to_r[i + 1] + 1
        elif ratings[i] < ratings[i + 1] and l_to_r[i] >= l_to_r[i + 1]:
            l_to_r[i + 1] = l_to_r[i] + 1

    r_to_l = [1] * length_of_ratings
    for i in list(reversed(range(1, length_of_ratings))):
        if ratings[i] > ratings[i - 1] and r_to_l[i] <= r_to_l[i - 1]:
            r_to_l[i] = r_to_l[i - 1] + 1
        elif ratings[i] < ratings[i - 1] and r_to_l[i] >= r_to_l[i - 1]:
            r_to_l[i - 1] = r_to_l[i] + 1

    sumOf = 0
    for i in range(length_of_ratings):
        sumOf += max(l_to_r[i], r_to_l[i])
    return sumOf
