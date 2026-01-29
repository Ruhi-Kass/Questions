class Solution:
    def findUnion(self, a, b):
        seen = set()
        result = []
        
        for num in a:
            if num not in seen:
                seen.add(num)
                result.append(num)
                
        for num in b:
            if num not in seen:
                seen.add(num)
                result.append(num)
                
        return result
