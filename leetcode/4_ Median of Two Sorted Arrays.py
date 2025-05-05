# Problem  --> https://leetcode.com/problems/median-of-two-sorted-arrays/
# level --> hard
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=[]
        i,j=0,0
        while i<=(len(nums1)-1) and j<=(len(nums2)-1):
            if nums1[i]<=nums2[j]:
                nums.append(nums1[i])
                i+=1
            else:
                nums.append(nums2[j])
                j+=1
        while i<=len(nums1)-1:
            nums.append(nums1[i])
            i+=1
        while j<=len(nums2)-1:
            nums.append(nums2[j])
            j+=1
        n=len(nums)
        if n%2==0:
            mid=n//2
            return (nums[mid-1]+nums[mid])/2
        else:
            mid=n//2
            return nums[mid]
