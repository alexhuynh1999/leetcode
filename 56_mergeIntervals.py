class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1: return intervals
        
        intervals.sort(key=lambda s:s[0])
        
        out = [intervals[0]]
        for i, intv in enumerate(intervals):
            if i == 0: continue
            if intv[0] <= out[-1][1]:
                out[-1][1] = max(out[-1][1], intv[1])
            else:
                out.append(intv) 
        return out
