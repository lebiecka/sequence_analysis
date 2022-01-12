
class Sequence:

    def __init__(self, in_seq: str) -> None:
        '''
        This function reads and validates sequence of DNA provided by user. 
        Default format of provided sequence is str.
        Change to uppercase is needed and verification if string contains only allowed signs: A, T, C, G. 
        '''
        self.in_seq = in_seq.upper()
        if any(c not in 'ATCG' for c in self.in_seq):
            raise ValueError("Your sequence is not correct - contains letter which is not allowed (A, T, C, G)")
    
    
    def transcript(self, in_seq: str) -> str:
        '''
        This function transcript sequence of DNA. The goal of transcription is to make a RNA copy of a gene's DNA sequence.
        '''
        DNA_Nucleotides = ['A', 'C', 'G','T']
        DNA_ReverseComplement = {'A':'U', 'T':'A', 'G':'C','C':'G'}
        in_seq = list(in_seq)
        self.in_seq = ''.join([DNA_ReverseComplement[nuc]for nuc in in_seq])[::-1]

 
    def aligment(self, in_seq_1: str, in_seq_2: str) -> str:

        '''
        The Needleman-Wunsch algorithm is a dynamic programming algorithm for finding the optimal alignment of
        two strings. In our case that will be two sequences (in_seq_1, in_seq_2). 
        '''
        from itertools import product
        from collections import deque

        N, M = len(in_seq_1), len(in_seq_2)
        s = lambda a, b: int(a == b)

        DIAG = -1, -1
        LEFT = -1, 0
        UP = 0, -1

        # Create tables F and Ptr
        F = {}
        Ptr = {}

        F[-1, -1] = 0
        for i in range(N):
            F[i, -1] = -i
        for j in range(M):
            F[-1, j] = -j

        option_Ptr = DIAG, LEFT, UP
        for i, j in product(range(N), range(M)):
            option_F = (
                F[i - 1, j - 1] + s(in_seq_1[i], in_seq_2[j]),
                F[i - 1, j] - 1,
                F[i, j - 1] - 1,
            )
            F[i, j], Ptr[i, j] = max(zip(option_F, option_Ptr))

        # Work backwards from (N - 1, M - 1) to (0, 0)
        # to find the best alignment.
        alignment = deque()
        i, j = N - 1, M - 1
        while i >= 0 and j >= 0:
            direction = Ptr[i, j]
            if direction == DIAG:
                element = i, j
            elif direction == LEFT:
                element = i, None
            elif direction == UP:
                element = None, j
            alignment.appendleft(element)
            di, dj = direction
            i, j = i + di, j + dj
        while i >= 0:
            alignment.appendleft((i, None))
            i -= 1
        while j >= 0:
            alignment.appendleft((None, j))
            j -= 1

        return "".join("-" if j is None else in_seq_2[j] for _, j in alignment)
 

my_seq = Sequence("TGCcAT")

print("DNA sequence: {}".format(my_seq.in_seq))
my_seq.transcript(my_seq.in_seq)
print("RNA copy of a gene's DNA sequence: {}".format(my_seq.in_seq))

my_seq_1 = Sequence("CATAGCTACGT")
print("DNA sequence no. 1: {}".format(my_seq_1.in_seq))
my_seq_2 = Sequence("CTGT")
print("DNA sequence no. 2: {}".format(my_seq_2.in_seq))
print("Sequence aligment: {}".format(my_seq_1.aligment(my_seq_1.in_seq, my_seq_2.in_seq)))



