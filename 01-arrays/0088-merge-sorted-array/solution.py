class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # Start filling from the VERY BACK to avoid overwriting nums1 data
        p1, p2, p = m - 1, n - 1, m + n - 1
        
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # If nums2 still has elements, copy them (nums1 elements are already there)
        nums1[:p2 + 1] = nums2[:p2 + 1]

