nums = [20,5,7,8,3,2,10,11]


def sort (nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1] : 
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
def sortSelect (nums):
    for i in range(len(nums)):
        minpos= i
        for j in range(i, len(nums)):
            if nums[j] < nums[minpos]:
                minpos = j
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos]= temp 
        print(nums)

# sort(nums)
# print(nums)
sortSelect(nums)