from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        h_map = {} #sort -> str_data

        for i in strs:

            sort_str = ''.join(sorted(i))

            if sort_str in h_map:
                h_map[sort_str].append(i)
            else:
                h_map[sort_str] = [i]
        
        return [v for k,v in h_map.items()]
