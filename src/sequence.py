
class Sequence:
    def validator(func):
        def sequence_validation(self, in_seq: str):
            '''
            This function validates sequence of DNA provided by user: converts to uppercase if needed and verificates 
            if string contains only allowed signs: A, T, C, G. '''
            self.in_seq = in_seq.upper()
            if any(c not in 'ATCG' for c in self.in_seq):
                raise ValueError("Your sequence is not correct - contains letter which is not allowed (A, T, C, G)")
        return sequence_validation
    @validator
    def __init__(self, in_seq: str) -> None:
        '''
        This function reads sequence of DNA provided by user. 
        Default format of provided sequence is str.
        '''
    
    def transcript(self) -> str:
        '''
        This function transcript sequence of DNA. The goal of transcription is to make a RNA copy of a gene's DNA sequence.
        * As part of learning we convert A to T. 
        '''
        DNA_Nucleotides = ['A', 'C', 'G','T']
        DNA_ReverseComplement = {'A':'T', 'T':'A', 'G':'C','C':'G'}
        in_seq = list(self.in_seq)
        self.in_seq = ''.join([DNA_ReverseComplement[nuc]for nuc in in_seq])[::-1]

if __name__ == "__main__":
    my_seq = Sequence("TGCcAT")
    print("DNA sequence: {}".format(my_seq.in_seq))
    my_seq.transcript()
    print("RNA copy of a gene's DNA sequence: {}".format(my_seq.in_seq))




