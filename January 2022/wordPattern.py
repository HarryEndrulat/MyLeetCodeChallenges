class Solution(object):
    def wordPattern(self, pattern, s):
        wordDict={}
        words=s.split()
        if len(pattern)!= len(words):
            return False
        for x,y in zip(pattern,words):
            if y in wordDict.values() and x not in wordDict.keys():
                return False
            if x not in wordDict.keys():
                wordDict[x]=y
            elif wordDict.get(x)!=y:
                return False
        return True

