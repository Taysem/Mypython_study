#如何在排序数组中
# ，找出给定数字出现次数？ 比如：{0,1,2,3,3,3,3,3,3,3,3,4,5,6,7,13,19}
k = {0,1,2,3,3,3,3,3,3,3,3,4,5,6,7,13,19}
def binFindUp(arr, key):
    low = 0
    high = len(arr) -1
    while(low < high):
        print("%d,%d" % (low, high))
        mid = (low + high) / 2
        if (arr[mid] <= key):
            low = mid
        else:
            high = mid - 1
    return low

def binFindDown(arr, key):
    low = 0
    high = len(arr) -1
    while(low < high):
        print("%d,%d" % (low, high))
        mid = (low + high) / 2
        if (arr[mid] >= key):
            high = mid
        else:
            low = mid + 1
    return high

binFindUp(k, 3)