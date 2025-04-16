class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        self.nums = nums
        nums_dict = {}
        for x in self.nums:
            if x in nums_dict:
                nums_dict[x] += 1
            else:
                nums_dict[x] = 1
        for x in nums_dict:
            if nums_dict[x] == 1:
                return x


if __name__ == "__main__":
    sol = Solution()
    print(sol.singleNumber([4,1,2,2,1]))