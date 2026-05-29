class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            for elem in s:
                if s.count(elem) != t.count(elem):
                    return False
            return True
        return False

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        strs_cp = strs.copy()

        if len(strs) == 1:
            output.append(strs)
            return output

        for elemi in strs:
            inside_output = []

            for elem in strs_cp:
                if self.isAnagram(elemi, elem):
                    inside_output.append(elem)

            if inside_output not in output:
                output.append(inside_output)

        return output