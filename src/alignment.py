from sequence import *

class Alignment(Sequence):

    def list_of_sequence_classes(*args):
        list_of_classes = []
        for i in range(len(args)):
            #single_class = Sequence(args[i]).in_seq ## tu nie byłam pewna czy mam zwracać output tych klas, czy  klasy same w sobie? 
            single_class = Sequence(args[i])
            list_of_classes.append(single_class)
        return list_of_classes

if __name__ == "__main__":
    print(Alignment.list_of_sequence_classes('TCgA', 'CCAAGT', 'AttTGC', 'TTTGGCTG'))
    my_seq = Alignment('TAAGT')
    print(my_seq.in_seq)
    print(my_seq.transcript())