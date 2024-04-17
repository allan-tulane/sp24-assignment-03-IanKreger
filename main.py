import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))


def fast_align_MED(S, T, MED={}):
    if (S, T) in MED:
      return MED[(S, T)]
    if S == "":
      return ("-" * len(T), T)
    elif T == "":
      return [S, "-" * len(S)]
    
    if S == "":
      return ("-" * len(T), T)
    if T == "":
      return (S, "-" * len(S))
  
    if S[0] == T[0]:
      A_S, A_T = fast_align_MED(S[1:], T[1:], MED)
      result = (S[0] + A_S, T[0] + A_T)
      
    else:
      I_S, I_T = fast_align_MED(S, T[1:], MED)
      D_S, D_T = fast_align_MED(S[1:], T, MED)

      I_C = 1 + len(I_S)
      D_C = 1 + len(D_S)

      if I_C <= D_C:
        result = ("-" + I_S, T[0] + I_T)
      else:
        result = (S[0] + D_S, "-" + D_T)
    
    MED[(S, T)] = result
    return result
    
