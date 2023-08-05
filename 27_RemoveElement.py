# since the remaining order of the elements does not matter, we can just swap the elements, only the ones we need will be right, for this case the first 2 places\
# The hint here to swap is that they don't need to care about the remaining elements
def removeElement(nums, val):
    index = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1
    return index

nums = [3,2,2,3]
val = 3
print(removeElement(nums, val))