class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findKthLargest(start1,end1,start2,end2,nums1,nums2,k):
            if start1 > end1:
                return nums2[k-start1]
            if start2 > end2:
                return nums1[k-start2]
            middle1 = (start1 + end1)//2
            middle2 = (start2 + end2)//2
            middle1_value = nums1[middle1]
            middle2_value = nums2[middle2]
            if middle1 + middle2 < k:
                if middle1_value < middle2_value:
                    return findKthLargest(middle1+1,end1,start2,end2,nums1,nums2,k)
                else:
                    return findKthLargest(start1,end1,middle2+1,end2,nums1,nums2,k)
            else:
                if middle1_value < middle2_value:
                    return findKthLargest(start1,end1,start2,middle2-1,nums1,nums2,k)                    
                else:
                    return findKthLargest(start1,middle1-1,start2,end2,nums1,nums2,k)
        l1 = len(nums1)
        l2 = len(nums2)
        if (l1+l2)%2 == 1:
            return findKthLargest(0,l1-1,0,l2-1,nums1,nums2,(l1+l2)//2)
        else:
            left = findKthLargest(0,l1-1,0,l2-1,nums1,nums2,(l1+l2)//2)
            right = findKthLargest(0,l1-1,0,l2-1,nums1,nums2,(l1+l2)//2-1)
            return (left + right)/2
