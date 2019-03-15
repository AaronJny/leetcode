class Solution:
    def groupAnagrams(self, strs):
        if len(strs) == 0:
            return [[], ]
        result = {}
        for xstr in strs:
            tmp_str = ''.join(sorted(xstr))
            result.setdefault(tmp_str, []).append(xstr)
        return [value for key, value in result.items()]