class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):

            for elem in s:
                print(elem)
                if s.count(elem)!=t.count(elem):
                    return False
            else:
                return True
        return False

        # if len(s)==len(t):
        #     s_set = set(s)
        #     t_set = set(t)
        #     if s_set == t_set:
        #         return True
        #     else:
        #         return False
        # else:
        #     return False