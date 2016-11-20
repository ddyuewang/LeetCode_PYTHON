### Search in Rotated Sorted Array II
def search(nums, target):
    l = 0;
    r = len(nums) - 1;
    while (l <= r):
        m = l + ((r - l) >> 1)
        print "middle position", m
        print "left position", l
        print "right position", r
        print "---------------"
        if (nums[m] == target):
            return True
        if (nums[l] < nums[m]):
            if (target >= nums[l] and target <= nums[m]):
                r = m - 1
            else:
                l = m + 1
        elif (nums[l] > nums[m]):
            if (target >= nums[l] or target <= nums[m]):
                r = m - 1
            else:
                l = m + 1
        else:
            l = l + 1;  # case where equals

    return False


if __name__ == "__main__":

    nums = [3,1,1]
    target = 3
    res = search(nums, target)
    print res