from sequence import *

class Alignment:

    def list_of_sequence_classes(*args):
        list_of_classes = []
        for i in range(len(args)):
            #single_class = Sequence(args[i]).in_seq ## tu nie byłam pewna czy mam zwracać output tych klas, czy  klasy same w sobie? 
            single_class = Sequence(args[i])
            list_of_classes.append(single_class)
        print(list_of_classes)

if __name__ == "__main__":
    Alignment.list_of_sequence_classes('TCGA', 'CCAAGT', 'ATTTGC', 'TTTGGCTG')

