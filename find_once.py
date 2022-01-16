from functools import reduce
from typing import List

def xor(a, b):
    return a^b


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(xor, nums)

def single_number( nums: List[int]) -> int:
    my_set = set()
    for i in nums:
        if i not in my_set:
            my_set.add(i)
        else:
            my_set.remove(i)
    return my_set.pop()

if __name__=='__main__':
    s = [2,1,2,3,5,5,3]
    out = Solution().singleNumber(s)
    print(out)

    o = single_number(s)
    print(o)

