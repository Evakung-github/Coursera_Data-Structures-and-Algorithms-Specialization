#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
    tree = {0:{}}
    # write your code here
#    print(patterns)
    k = 1
    for p in patterns:
        d = 0
        for c in p:
            if c not in tree[d]:
                tree[d][c] = k
                tree[k] = {}
                k+=1
            d = tree[d][c]

            
            
    
    
    return tree

build_trie(['ATAGA', 'ATC', 'GAT'])

if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
