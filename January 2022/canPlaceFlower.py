class Solution:
    def canPlaceFlowers(self, pot, n):
        i=0
        cnt=0
        length=len(pot)
        if length==1 and pot[0]==0:
            return True
        elif length==0:
            return False
        while i<length:
            if i==0:
                if pot[i]==0 and pot[i+1]==0:
                    cnt+=1
                    pot[i]=1
            elif i==length-1:
                if pot[length-1]==0 and pot[length-2]==0:
                    cnt+=1
                    pot[length -1]=1
            elif pot[i-1]==0 and pot[i]==0 and pot[i+1]==0:
                cnt+=1
                pot[i]=1
            i+=1
        if cnt>=n:
            return True
        return False
