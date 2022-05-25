class Solution:
    def isPalindrome2(self, x: int) -> bool:
        x = str(x)
        flag = True
        for i in range(len(x)):
            if x[i] != x[len(x) - i - 1]:
                flag = False
        return flag

    def isPalindrome3(self, x: int) -> bool:
        i = 1
        y = 0
        original = x
        while x > 0:
            y = y * 10 + (x % 10)
            i = i + 1
            x = x // 10
        return original == y

    def isPalindrome(self, x: int) -> bool:
        i = 1
        y = 0
        original = x
        while y < x:
            y = y * 10 + (x % 10)
            i = i + 1
            x = x // 10
        return True if (x == y or x == y // 10) else False


ret = Solution()
print(ret.isPalindrome(12421))
