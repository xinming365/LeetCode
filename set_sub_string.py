
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lens = len(s)
        best=0
        if lens <=1: return lens
        window = set()
        left=right=0
        while right < lens:
            if s[right] not in window:
                window.add(s[right])
                best = max(best, right-left+1)
                right+=1
            else:
                window.remove(s[left])
                left+=1
        return best


def lengthOfLongestSubstring2(self, s: str) -> int:
    lens = len(s)
    best=0
    if lens <=1: return lens
    for i in range(lens):
        for j in range(i, lens):
            sub_string = s[i:j]
            a = set(sub_string)
            next = s[j]
            if next in a:
                break
            else:
                if len(a)+1>best:
                    best=len(a)+1

    return best
# 2. 滑动窗口
# 时间复杂度：O(2n) = O(n)，最坏的情况是 left 和 right 都遍历了一遍字符串
# 空间复杂度：O(n)
def lengthOfLongestSubstring1(s: str) -> int:
    n = len(s)
    if n <= 1: return n
    max_len, window = 0, set()
    left = right = 0
    while right < n:
        if s[right] not in window:
            max_len = max(max_len, right - left + 1)
            window.add(s[right])
            right += 1
        else:
            window.remove(s[left])
            left += 1
    return max_len


if __name__=='__main__':
    s = "abcabcbb"
    # s = "bbbbb"
    # s = "au"
    out = Solution().lengthOfLongestSubstring(s)
    print(out)
    out2 = lengthOfLongestSubstring1(s)
    print(out2)