
class Sequence:

    def __init__(self, in_seq: str) -> None:
        self.in_seq = in_seq.upper()
        if any(c not in 'ATCG' for c in self.in_seq):
            raise ValueError("Your sequence is not correct - contains letter which is not allowed (A, T, C, G)")
    
    
    def transcript(self, in_seq: str) -> str:
        DNA_Nucleotides = ['A', 'C', 'G','T']
        DNA_ReverseComplement = {'A':'T', 'T':'A', 'G':'C','C':'G'}
        in_seq = list(in_seq)
        return ''.join([DNA_ReverseComplement[nuc]for nuc in in_seq])[::-1]


'''
my_seq = Sequence("TGGCcAT")
print(my_seq.in_seq)
my_seq.transcript(my_seq)
print(my_seq.in_seq)
'''