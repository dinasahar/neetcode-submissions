class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for elem in nums:
            if elem in count:
                count[elem]+=1
            else:
                count[elem]=1
        
        sorted_count = dict(sorted(count.items(), key= lambda item:item[1], reverse=True))
        sorted_list= list(sorted_count.keys())
        print(sorted_list)
        return sorted_list[:k]


        