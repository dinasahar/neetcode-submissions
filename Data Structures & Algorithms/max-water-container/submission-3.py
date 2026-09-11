class Solution:
    def maxArea(self, heights: List[int]) -> int:

        r=len(heights)-1
        l=0

        areas=[]
        while r>l:

            if heights[r]<= heights[l]:
                area = (r-l) * heights[r]
                areas.append(area)
                r=r-1
            
            else:
                area = (r-l) * heights[l]
                areas.append(area)
                l=l+1
    

        return max(areas)





        