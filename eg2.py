#  2. Sorting Method: ACCEPTED
def containsDuplicate(nums):
        nums = sorted(nums)
        print(nums)
        for i in range(len(nums)):
                if i+1 == len(nums):
                    return False
                if nums[i] == nums[i+1]:
                    return True
input = [1,2,3,1]
res = containsDuplicate(input)
print(res)