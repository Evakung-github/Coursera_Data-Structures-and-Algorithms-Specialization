# python3
import sys

def BWT(text):
    l = []
    l.append(text)
    for i in range(1,len(text)):
        l.append(text[i:]+text[:i])

    l.sort()
    ans = ''
    for i in l:
        ans+=i[-1]
    

    
    return ans



a = BWT(k)

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))