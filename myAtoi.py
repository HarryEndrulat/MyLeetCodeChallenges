
class Solution(object):
    def myAtoi(self, s):
        s=s.strip()
        sign = '+'
        result='0'
        if len(s)==0:
            return 0
        if s[0] =='-':
            sign = '-'

        for i, x in enumerate(s):
            if not(s[0].isdigit() or s[0]=='-' or s[0]=='+'):
                break
            if s[0].isdigit():
                if x.isdigit():
                    result += x
                else:
                    break
            elif (s[0]=='-'or'+') and i>0:
                if x.isdigit():
                    result += x
                else:
                    break

        num=int(result)
        if sign=='-':
            num=num*-1
        if num<-2147483648:
            num=-2147483648
        if num>2147483647:
            num=2147483647
        return num


s=Solution()
#s.myAtoi(" -0032 + 25")
s.myAtoi("1")