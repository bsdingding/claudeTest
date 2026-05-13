"""
问题：将一个升序数组在某个位置旋转（左边移到右边），在旋转后的数组中查找 target，
      返回其下标，不存在则返回 -1。要求 O(log n)。

思路：二分查找。每次取中点后，左半段和右半段中必有一段是有序的：
  - 若 nums[lo] <= nums[mid]，左半段有序
      · target 在 [nums[lo], nums[mid]) 内 → 收缩到左半段
      · 否则 → 收缩到右半段
  - 否则右半段有序
      · target 在 (nums[mid], nums[hi]] 内 → 收缩到右半段
      · 否则 → 收缩到左半段
"""


def search(nums: list, target: int) -> int:
    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid

        if nums[lo] <= nums[mid]:
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1

    return -1


if __name__ == "__main__":
    cases = [
        ([4, 5, 6, 7, 0, 1, 2], 0,  4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1],                   1,  0),
        ([1],                   0, -1),
        ([3, 1],                1,  1),
        ([5, 1, 3],             3,  2),
        ([1, 3],                3,  1),
        (list(range(100)),      99, 99),
        (list(range(1, 101)),   1,  0),
    ]

    for nums, target, expected in cases:
        result = search(nums, target)
        status = "OK" if result == expected else "FAIL"
        display = nums if len(nums) <= 8 else f"[0..{nums[-1]}]"
        print(f"[{status}] nums={display}  target={target}  got={result}  expected={expected}")
