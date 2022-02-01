from sequence import Sequence

class Alignment:

    def __init__(self, *args) -> None:
        list_of_classes = []
        for i in range(len(args)):
            single_class = Sequence(args[i])
            list_of_classes.append(single_class)
        self.list_of_seq = list_of_classes

    def __str__(self):
        return str([str(i) for i in self.list_of_seq])

    def __iter__(self):
        for i in self.list_of_seq:
            yield i

if __name__ == "__main__":
    al = Alignment('TCgA', 'CCAAGT', 'AttTGC', 'TTTGGCTG')
    print(al.__str__())

    for sequence in al:
        print(sequence.transcript())
