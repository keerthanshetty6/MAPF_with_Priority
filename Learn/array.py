class Solution(object):
    @staticmethod
    def mergeAlternately( word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        A,B=len(word1),len(word2)
        """op=[]
        for i,j in zip(word1,word2):
            op.append(i)
            op.append(j)
        
        op.append(word1[B:] or word2[A:])
        return ''.join(op)"""
        a,b=0,0
        op=[]
        word=1

        while a < A and b < B:
            if word==1:
                op.append(word1[a])
                a+=1
                word=2
            else:
                op.append(word2[b])
                b+=1
                word=1
        print(op)
        if a<A:
            op.extend(word1[a:]) 
        else:
            op.extend(word2[b:]) 
        print(op)   
        return ''.join(op)
    
print(Solution.mergeAlternately("ab","dsgsbh"))