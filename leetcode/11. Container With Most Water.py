# Problem description --> https://leetcode.com/problems/container-with-most-water/description
# level --> hard
def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        max_area=0
        while left<right:
            width=right-left
            ht=min(height[left],height[right])
            area=width*ht
            if area>max_area:
                max_area=area
            if ht==height[left]:
                left+=1
            else:
                right-=1
        return max_area
