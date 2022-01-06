class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_set = set(words)
        freq = dict.fromkeys(word_set, 0)
        
        for word in words:
            freq[word] += 1
        
        freq_sorted = sorted(freq.items(), key=lambda x:(-x[1], x[0]))
        out = [x[0] for x in freq_sorted[:k]]
        
        return out
