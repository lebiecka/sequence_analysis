from multiprocessing.dummy import Value
from sequence import Sequence
import numpy as np

class Alignment:

    def __init__(self, *args) -> None:

        list_of_classes = []
        align_scores= {}
        for i in range(len(args)):
            single_class = Sequence(args[i])
            list_of_classes.append(single_class)
        self.list_of_seq = list_of_classes

        self._align_scores = align_scores

    def __getitem__(self, index): 

        if isinstance(index, tuple):
            if len(index) > 2:
                raise ValueError("Number of sequences is not allowed!")
            seq1, seq2  = index
            return self.wunsch(self.list_of_seq[seq1], self.list_of_seq[seq2]).popitem()
        return self.list_of_seq[index]

    def __str__(self):
        return str(self.list_of_seq)

    def __iter__(self):
        for i in self.list_of_seq:
            yield i

    def __len__(self):
        return len(self.list_of_seq)

    def wunsch(self, seq1: Sequence, seq2: Sequence) -> dict:
       # Use these values to calculate scores
        gap_penalty = -1
        match_award = 1
        mismatch_penalty = -1

        # A function for making a matrix of zeroes
        def zeros(rows, cols):
            # Define an empty list
            retval = []
            # Set up the rows of the matrix
            for x in range(rows):
                # For each row, add an empty list
                retval.append([])
                # Set up the columns in each row
                for y in range(cols):
                    # Add a zero to each column in each row
                    retval[-1].append(0)
            # Return the matrix of zeros
            return retval

        # A function for determining the score between any two bases in alignment
        def match_score(alpha, beta):
            if alpha == beta:
                return match_award
            elif alpha == '-' or beta == '-':
                return gap_penalty
            else:
                return mismatch_penalty

        # Store length of two sequences
        n = len(seq1)
        m = len(seq2)
        
        # Generate matrix of zeros to store scores
        score = zeros(m+1, n+1)

        ## Calculate score table
        
        # Fill out first column
        for i in range(0, m + 1):
            score[i][0] = gap_penalty * i
        
        # Fill out first row
        for j in range(0, n + 1):
            score[0][j] = gap_penalty * j
        
        # Fill out all other values in the score matrix
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Calculate the score by checking the top, left, and diagonal cells
                match = score[i - 1][j - 1] + match_score(seq1[j-1], seq2[i-1])
                delete = score[i - 1][j] + gap_penalty
                insert = score[i][j - 1] + gap_penalty
                # Record the maximum score from the three possible scores calculated above
                score[i][j] = max(match, delete, insert)
        
        ## Traceback and compute the alignment 
        
        # Create variables to store alignment
        align1 = ""
        align2 = ""
        
        # Start from the bottom right cell in matrix
        i = m
        j = n
        
        # We'll use i and j to keep track of where we are in the matrix, just like above
        while i > 0 and j > 0: # end touching the top or the left edge
            score_current = score[i][j]
            score_diagonal = score[i-1][j-1]
            score_up = score[i][j-1]
            score_left = score[i-1][j]
            
            # Check to figure out which cell the current score was calculated from,
            # then update i and j to correspond to that cell.
            if score_current == score_diagonal + match_score(seq1[j-1], seq2[i-1]):
                align1 += seq1[j-1]
                align2 += seq2[i-1]
                i -= 1
                j -= 1
            elif score_current == score_up + gap_penalty:
                align1 += seq1[j-1]
                align2 += '-'
                j -= 1
            elif score_current == score_left + gap_penalty:
                align1 += '-'
                align2 += seq2[i-1]
                i -= 1

        # Finish tracing up to the top left cell
        while j > 0:
            align1 += seq1[j-1]
            align2 += '-'
            j -= 1
        while i > 0:
            align1 += '-'
            align2 += seq2[i-1]
            i -= 1
        
        # Since we traversed the score matrix from the bottom right, our two sequences will be reversed.
        # These two lines reverse the order of the characters in each sequence.
        align1 = align1[::-1]
        align2 = align2[::-1]
        result = {}
        result[(seq1, seq2)] = ( align1, np.array(score)[-1][-1])
        result[(seq2, seq1)] = ( align2,  np.array(score)[-1][-1])
 
        return result


    def align(self):

        pairs = [(self.list_of_seq[i], self.list_of_seq[j]) for i in range(len(self.list_of_seq)) for j in range(i+1,len(self.list_of_seq))]
        for p in range(len(pairs)):
            self.align_scores = self.align_scores | self.wunsch(pairs[p][0], pairs[p][1])

        return self.align_scores

if __name__ == "__main__":
    al = Alignment('TCgA', 'CCAAGT', 'AttTGC', 'TTTGGCTG')

    print("\n______Construction_______")
    print(str(al)) 
    print(al) 
    print(len(al))

    print("\n______Iter_transcript_______")
    for sequence in al:
        print(sequence.transcript())
    

    print("\n______Transcript_______")
    print(al[2]) 
    print(al[2].transcript()) 

    print("\n______Getter_______")
    print(al[2])    # to zwróci 3. sekwencje
    print(al[(2,0)])    # to zwróci alignment i score między 1 i 3 sekwencja


    print("\n______Align_______")
    al.align_scores #none
    al.align()
    print(al.align_scores)
    
    
