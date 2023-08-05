nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3

# remember to compute last before m and n else the last value would be wrong
last = m + n - 1 # starting from the end of nums1
m = m - 1 # since m denotes length and not the index
n = n - 1 # since n denotes length and not the index

while n >= 0:
    if nums1[m] > nums2[n] and m >= 0:
        nums1[last] = nums1[m]
        m -= 1
    else:
        nums1[last] = nums2[n]
        n -= 1
    last -= 1

print(nums1)