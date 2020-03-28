# python3
import sys

NA = -1

class Node:
    def __init__ (self):
        self.next = [None] * 4
        self.isend = False

def solve (text, n, patterns):
    result = []
    p = Node()
    match = {"A":0,"T":1,"C":2,"G":3}
    

#     write your code here
    for pattern in patterns:
        temp = p
        for c in pattern:
            if not temp.next[match[c]]:
                temp.next[match[c]] = Node()
            temp = temp.next[match[c]]
        temp.isend = True

    for i in range(len(text)):
        temp = p
        
        j = i
        while temp and j<len(text):       
            temp = temp.next[match[text[j]]]
            if not temp:
                break
            if temp.isend:
                result.append(i)
                break
            else:
                j+=1
    return result

result = solve('AAA',1,['AA'])



text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
