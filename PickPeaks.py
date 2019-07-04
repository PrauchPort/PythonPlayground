# https://www.codewars.com/kata/pick-peaks/train/python

import unittest


def pick_peaks(arr):
    prev, cur = 0, 0
    pos = []
    peaks = []
    for next in range(1, len(arr)):
        if arr[next] > arr[cur]:
            prev = cur
            cur = next
        else:
          if arr[next] < arr[cur]:
              if arr[prev] < arr[cur]:
                  pos.append(cur)
                  peaks.append(arr[cur])
              prev = cur
              cur = next
    return {"pos": pos, "peaks": peaks}


test = unittest.TestCase()


test.assertEquals(pick_peaks([1,2,3,6,4,1,2,3,2,1]), {"pos":[3,7], "peaks":[6,3]})
test.assertEquals(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,3]), {"pos":[3,7], "peaks":[6,3]})
test.assertEquals(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1]), {"pos":[3,7,10], "peaks":[6,3,2]})
test.assertEquals(pick_peaks([2,1,3,1,2,2,2,2,1]), {"pos":[2,4], "peaks":[3,2]})
test.assertEquals(pick_peaks([2,1,3,1,2,2,2,2]), {"pos":[2], "peaks":[3]})