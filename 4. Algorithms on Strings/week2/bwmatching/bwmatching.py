# python3
import sys


def PreprocessBWT(bwt):
  """
  Preprocess the Burrows-Wheeler Transform bwt of some text
  and compute as a result:
    * starts - for each character C in bwt, starts[C] is the first position 
        of this character in the sorted array of 
        all characters of the text.
    * occ_count_before - for each character C in bwt and each position P in bwt,
        occ_count_before[C][P] is the number of occurrences of character C in bwt
        from position 0 to position P inclusive.
  """
  # Implement this function yourself
  first_pos = {"A":0,"C":0,"G":0,"T":0,"$":0}
#  occ_counts_before = {("A",0):0,("C",0):0,("G",0):0,("T",0):0,("$",0):0}
  occ_counts_before = {"A":{0:0},"C":{0:0},"G":{0:0},"T":{0:0},"$":{0:0}}
  for i in bwt:
      first_pos[i]+=1
  s = sorted(first_pos.keys())
  cum = 0
  for i in range(len(s)):
      t = first_pos[s[i]]
      first_pos[s[i]] = cum
      cum += t
  
  for i,c in enumerate(bwt):
      for j in s:
#          occ_counts_before[(j,i+1)] = occ_counts_before[(j,i)]
          occ_counts_before[j][i+1] = occ_counts_before[j][i]
#      occ_counts_before[(c,i+1)] += 1
      occ_counts_before[c][i+1] += 1
  
  return first_pos, occ_counts_before
starts, occ_counts_before = PreprocessBWT("AT$TCTATG")

def CountOccurrences(pattern, bwt):
  """
  Compute the number of occurrences of string pattern in the text
  given only Burrows-Wheeler Transform bwt of the text and additional
  information we get from the preprocessing stage - starts and occ_counts_before.
  """
  # Implement this function yourself
  
  pattern = list(pattern)
  top,bottom = 0,len(bwt)-1
  while top<=bottom:
      if pattern:
          cur = pattern.pop()
          top = starts[cur]+occ_counts_before[cur][top]
          bottom = starts[cur]+occ_counts_before[cur][bottom+1]-1
      else:
          return bottom-top+1
        
  return 0

#CountOccurrences('GA',"AGGGAA$",starts,occ_counts_before)


if __name__ == '__main__':
  bwt = sys.stdin.readline().strip()
  pattern_count = int(sys.stdin.readline().strip())
  patterns = sys.stdin.readline().strip().split()
  # Preprocess the BWT once to get starts and occ_count_before.
  # For each pattern, we will then use these precomputed values and
  # spend only O(|pattern|) to find all occurrences of the pattern
  # in the text instead of O(|pattern| + |text|).  
  starts, occ_counts_before = PreprocessBWT(bwt)
  occurrence_counts = []
  for pattern in patterns:
    occurrence_counts.append(CountOccurrences(pattern, bwt))
  print(' '.join(map(str, occurrence_counts)))
