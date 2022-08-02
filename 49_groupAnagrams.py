class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      # go through each word
      # get the frequency map of all the characters
      # store all the frequency maps in a dictionary
      # -- each key is the frequency map or anagram group (this is true because all anagrams should have the same # of chars)
      # -- the values of the keys will be a list containing every word that fits that frequency map
      # return the values of the dictionary
      
      
      anagramGroups = defaultdict(list)

      for word in strs:
          alphabet = set(map(chr, range(97, 123)))
          freqMap = dict.fromkeys(alphabet, 0)
          for char in word: freqMap[char] += 1

          anagramGroups[tuple(freqMap.values())].append(word)

      return anagramGroups.values()
