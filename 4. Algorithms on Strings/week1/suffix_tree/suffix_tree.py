# python3
import sys

sys.setrecursionlimit(15000)

def build_suffix_tree(text):
    result = []
    tree = {}
    if len(set(text)) == 2:
        result = [text[0] for i in range(len(text)-2)]
        result.append(text[-2:])
        result.extend(['$']*(len(text)-1))
        return result
        
    
    for i in range(len(text)):
        d = tree
        j = i
        while j<len(text):
            for k,l in d:
                if text[k]==text[j]:
                    index = 0
                    while text[k+index]==text[j] and index <l and j<len(text):
                        index += 1
                        j+=1
                    
                    if index != l:
                        newk = (k,index)
                        newv = {(k+index,l-index):d[(k,l)]}
                        d.pop((k,l))
                        d[newk] = newv
                        d = d[newk]
                    else:
                        d = d[(k,l)]
                    break
            else:
                d[(j,len(text)-j)]={}
                break
    
    def printf(d):
        for i in d:
            s,l = i
            result.append(text[s:s+l])
            if len(d[i]) != 0:
                printf(d[i])
    
    printf(tree)
    
    return result

build_suffix_tree('AAAAACCCCAAAAAAAA$')                  
                
            
            
    
    
#    # Implement this function yourself
#    for i in range(len(text)):
#        d = tree
#        for j in range(i,len(text)):
#            if text[j] not in d:
#                d[text[j]] = {}
#            d = d[text[j]]
#    def compress(d,pre):
#        for i in d:
#            if len(d[i])==1:
#                compress(d[i],pre+i)
#            else:
#                result.append(pre+i)
#                compress(d[i],'')
#                
#
#    compress(tree,'')




if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  result = build_suffix_tree(text)
  print("\n".join(result))