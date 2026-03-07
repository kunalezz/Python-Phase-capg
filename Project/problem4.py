class Solution:
    def unique_products(self, products):
        result = []
        freq = {}
        
        for item in products:
            freq[item] = freq.get(item, 0) + 1
        
        for item in products:
            if freq[item] == 1:
                result.append(item)
        
        return result