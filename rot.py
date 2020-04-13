#!/usr/bin/env python
import  unittest

# In-place array rotation. Uses the following observations:
# A rotation ABC -> CAB is equivalent to:
# - first swapping (in place) A and C: ABC -> CBA
# - then recursibely shifting BA -> AB
# A left rotation by more than half can be replaced by right rotation by less than half.

def swap(arr, start, end, shift):
    """Swaps `shift`-lenght prefix and suffix of `arr[start:end]`"""
    for i in range(0, shift):
        arr[start + i],   arr[end-shift+i] = \
        arr[end-shift+i], arr[start+i]

def rott(right, arr, start, end, shift):
    """Rotates `arr[start:end]` by `shift` places left or right depending on `right`."""
    length = end - start

    if shift > length / 2:
        return rott(not right, arr, start, end, length - shift)
    elif length > 1 and shift != 0: 
        swap(arr, start, end, shift)

        if right: end -= shift
        else: start += shift

        rott(right, arr, start, end, shift)
    
def rot(arr, n):
    """Rotates array `arr` left by `n` in place."""
    l = len(arr)
    n =( (n%l)+l)%l
    rott(False, arr, 0, l, n)



class RotTest(unittest.TestCase):
    def test(self):
        for l in range(0, 40):
            for r in range(0, l):
                # test for rotation outside [0, l) too
                for s in [-1, 0, 1]:
                    arr = range(0, l)
                    original = arr[:]
                    rot(arr, r + l * s)
                    self.assertEqual(arr, original[-r:] + original[0:-r])



if __name__ == '__main__':
    unittest.main()
