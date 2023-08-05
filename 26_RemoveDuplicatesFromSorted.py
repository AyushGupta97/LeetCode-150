# consider the inplace swapping mechansim here, all you have to do is maintain a pointer to the last index of the unique elements and keep progressing it
def removeDuplicates(nums):
    prev = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[prev]:
            prev += 1
            nums[prev] = nums[i]
    return prev + 1

nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))