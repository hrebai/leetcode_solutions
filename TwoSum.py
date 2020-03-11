class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = {}
        for index, num in enumerate(nums):
            n = target - num
            if n not in result:
                result[num] = index
            else:
                return [result[n], index]
                
if __name__ == '__main__':
    a = Solution()
    arr = [2, 7, 11, 15]
    x = 9
    test = a.twoSum(nums=arr, target=x)
    print(test)      
