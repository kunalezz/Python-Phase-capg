class Solution:
    def find_duplicate_words(self, sentence):
        words = sentence.lower().split()
        duplicates = []
        
        for i in range(len(words) - 1):
            if words[i] == words[i + 1]:
                duplicates.append(words[i])
        
        return duplicates