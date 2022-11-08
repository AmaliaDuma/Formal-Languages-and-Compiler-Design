from domain.fa import FiniteAutomaton
from domain.scanner import Scanner


def printOptions():
    print("1. Display states. \n"
          "2. Display alphabet. \n"
          "3. Display initial state \n"
          "4. Display final states. \n"
          "5. Display transitions. \n"
          "6. Check if sequence is accepted. \n"
          "7. Scan file. \n"
          "0. Quit.")


if __name__ == '__main__':
    scanner = Scanner()
    fa = FiniteAutomaton()
    fa.readFromFile("fa.in")

    done = False
    while not done:
        printOptions()
        option = int(input("Option: "))
        if option == 1:
            fa.printStates()
        elif option == 2:
            fa.printAlphabet()
        elif option == 3:
            fa.printInitialState()
        elif option == 4:
            fa.printFinalStates()
        elif option == 5:
            fa.printTransitions()
        elif option == 6:
            sequence = input("Enter sequence: ")
            result = fa.isAccepted(sequence)
            if result:
                print("Sequence[" + sequence + "] is accepted by the current FA. \n")
            else:
                print("Sequence[" + sequence + "] is not accepted by the current FA. \n")
        elif option == 7:
            filename = input("Enter filename: ")
            scanner.scanFile(filename)
        elif option == 0:
            done = True
        else:
            print("Invalid option")
