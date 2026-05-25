class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list_map = {}
        for i in strs:
            key = ''.join(sorted(i))
            if key not in list_map:
                list_map[key] = []
            list_map[key].append(i)
        return list(list_map.values())