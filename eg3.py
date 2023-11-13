#  3. Hash Set: ACCEPTED
def containsDuplicate(nums):
        set_list = set(nums)
        result = len(nums) != len(set_list)
        return result
input = [1,2,3,1]
res = containsDuplicate(input)
print(res)