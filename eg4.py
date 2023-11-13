#4, Hash Map: ACCEPTED
def containsDuplicate(nums):
        res = {
                '1': [],
                '2': []
        }
        store = {}
        for i in range(len(nums)):
                element = nums[i]
                if str(element) in store:
                        res['2'].append(element)
                # return True
                else:
                        store[str(element)] = element
                        res['1'].append(element)
                        return False
        print(res)
        print(store)
        if len(res['2']) > 0:
                # print('Yes')
                return True
        else: 
                # print('No')
                return False
input = [1,2,3,1]
res = containsDuplicate(input)
print(res)