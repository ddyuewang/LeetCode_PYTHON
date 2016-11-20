### Search in Rotated Sorted Array - without duplicate
def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    l, h = 0, len(nums) - 1
    while (l <= h):
        m = l + ((h - l) >> 1)
        if nums[m] == target:
            return m
        elif (nums[m] > nums[l] and target < nums[m] and target >= nums[l]) or (
                nums[m] < nums[l] and not (target <= nums[h] and target > nums[m])):
            h = m - 1
        else:
            l = m + 1
    return -1


### Search in Rotated Sorted Array II - duplicate
def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: bool
    """

    l = 0;
    r = len(nums) - 1;
    while (l <= r):
        m = l + ((r - l) >> 1)
        if (nums[m] == target):
            return True
        if (nums[l] < nums[m]):
            if (target >= nums[l] and target <= nums[m]):
                r = m - 1
            else:
                l = m + 1
        elif (nums[l] > nums[m]):
            if (target >= nums[l] or target <= nums[m]):  # change > <  to >= or <=
                r = m - 1
            else:
                l = m + 1
        else:
            l = l + 1;  # case where equals 

    return False