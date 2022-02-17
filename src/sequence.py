class Sequence:

    def validator(where_arg):
        def actual_decorator(func):
            def sequence_validation(*args, **kwargs):
                '''
                This function validates sequence of DNA provided by user: converts to uppercase if needed and verificates 
                if string contains only allowed signs: A, T, C, G. 
                '''
                if where_arg=='IN':
                    in_seq = args[1]
                    if any(c not in 'ATCG' for c in in_seq.upper()):
                        raise ValueError("Your sequence is not correct - contains letter which is not allowed (A, T, C, G)")
                elif where_arg =='OUT':
                    out_seq = func(*args, **kwargs)
                    if any(c not in 'ATCG' for c in out_seq):
                        raise ValueError("Your sequence is not correct - contains letter which is not allowed (A, T, C, G)")
                    return out_seq  
            
                return func(*args, **kwargs)
            return sequence_validation
        return actual_decorator
        
    @validator("IN")
    def __init__(self, in_seq) -> None:
        '''
        This function reads sequence of DNA provided by user. 
        Default format of provided sequence is str.
        '''
        self.in_seq = in_seq.upper()

    def __str__(self):
        return str(self.in_seq)    

    def __repr__(self):
        return f"Seq({str(self.in_seq)})"  
    
    def __len__(self):
        return len(self.in_seq)
    
    def __getitem__(self, index):
        return self.in_seq[index]

    @validator("OUT")
    def transcript(self) -> str:
        '''
        This function transcript sequence of DNA. The goal of transcription is to make a RNA copy of a gene's DNA sequence.
        * As part of learning we convert A to T. 
        '''
        DNA_ReverseComplement = {'A':'T', 'T':'A', 'G':'C','C':'G'}
        in_seq = list(self.in_seq)
        return ''.join([DNA_ReverseComplement[nuc]for nuc in in_seq])

if __name__ == "__main__":
    my_seq = Sequence("TGCcAT")
    print(my_seq.in_seq)
    print(my_seq.transcript())
