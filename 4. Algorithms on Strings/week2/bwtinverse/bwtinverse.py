# python3
import sys

def InverseBWT(bwt):
    # write your code here
#    f = sorted(bwt)
    cache = {"A":0,"C":0,"G":0,"T":0,"$":0}
    match = {}
    a = []
    for i in bwt:
        cache[i] += 1
        a.append((i,cache[i]))
    l = ["$","A","C","G","T"]
    i,j = 4,len(a)-1
    while i >= 0:
        while cache[l[i]] >0:
            match[(l[i],cache[l[i]])] = a[j]
            j-=1
            cache[l[i]]-=1
        i-=1
    
    ans = '$'
    cur = ('$',1)
    while match[cur] != ('$',1):
        ans += match[cur][0]
        cur = match[cur]
        
  
    return ans[::-1]
#import random
#s = list('A'*50+'T'*100+'C'*100)
#l = random.shuffle(s)
#k = ''.join(s)+'$'
#a = BWT(k)
#
#InverseBWT(a) == k

if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))