
def containsDuplicate(nums):
        # 1. Brute Force Method
        elements = len(nums)
        for i in range(elements):
                for j in range((elements - i - 1)):
                    j += i + 1
                    print('i:', i, 'j:', j)
                    if nums[i] == nums[j]:
                        return True
        return False
input = [1,2,3,1]
res = containsDuplicate(input)
print(res)