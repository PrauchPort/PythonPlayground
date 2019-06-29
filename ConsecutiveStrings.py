# https://www.codewars.com/kata/consecutive-strings/train/python

import unittest


def longest_consec(strarr, k):
    if strarr == '' or strarr == [] or k <= 0 or k > len(strarr):
        return ''
    longest = [(len(''.join(strarr[i:i+k])), ''.join(strarr[i:i+k])) for i, x in enumerate(strarr)]
    return [longest[i][1] for i in range(len(longest)) if longest[i][0] == max([i[0] for i in longest])][0]


test = unittest.TestCase()


def testing(actual, expected):
    test.assertEqual(actual, expected)


testing(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta")
testing(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1), "oocccffuucccjjjkkkjyyyeehh")
testing(longest_consec([], 3), "")
testing(longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2), "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck")
testing(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2), "wlwsasphmxxowiaxujylentrklctozmymu")
testing(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2), "")
testing(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3), "ixoyx3452zzzzzzzzzzzz")
testing(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15), "")
testing(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0), "")
