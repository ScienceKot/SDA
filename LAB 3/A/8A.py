true_sequence = input("Enter the true sequence of flags:")
first = input("Enter the sequence that Peter saw first:")
second = input("Enter the sequence that Peter saw second:")
reversed_sequence = true_sequence[::-1]
if first in true_sequence:
    if second in true_sequence:
        if first in reversed_sequence:
            if second in reversed_sequence:
                if second in true_sequence[true_sequence.index(first)+1:] and second in true_sequence[reversed_sequence.index(first)+1:] :
                    print("both")
                elif true_sequence.index(first) < true_sequence.index(second) and not reversed_sequence.index(first) < reversed_sequence.index(second):
                    print("forward")
                elif not true_sequence.index(first) < true_sequence.index(second) and reversed_sequence.index(first) < reversed_sequence.index(second):
                    print('backward')
    else:
        print('fantasy')
else:
    print('fantasy')
