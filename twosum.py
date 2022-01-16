from typing import List

def twoSum( nums: List[int], target: int) -> List[int]:
    my_dict={}
    for i, ele in enumerate(nums):
        s = target-ele
        if s in my_dict.keys():
            return [i, my_dict[s]]
        if s in nums:
            my_dict[s]=nums.index(s)
    return []

if __name__=='__main__':
    nums=[3,2,4]
    target = 6
    out = twoSum(nums, target)
    print(out)