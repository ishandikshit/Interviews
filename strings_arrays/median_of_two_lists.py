class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = []
        i=0
        j=0
        while (i<len(nums1) and j<len(nums2)):
            if(nums1[i]<=nums2[j]):
                nums3.append(nums1[i])
                i=i+1
            else:
                nums3.append(nums2[j])
                j=j+1
        
        if len(nums1)>i:
            for m in range(i, len(nums1)):
                nums3.append(nums1[m])
        if len(nums2)>j:
            for m in range(j, len(nums2)):
                nums3.append(nums2[m])
        print nums3
        if len(nums3)%2==0:
            return (nums3[len(nums3)/2]+nums3[len(nums3)/2 - 1])/2.0
        else:
            return nums3[len(nums3)/2]
            
        
