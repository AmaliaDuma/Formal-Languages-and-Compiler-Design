class FiniteAutomaton:
    def __init__(self):
        self._states = []
        self._alphabet = []
        self._initial_state = None
        self._final_states = []
        self._transitions = {}

    def readFromFile(self, filename):
        """
        Reads the elements of the fa from the file given as parameter. \n
        :param filename: name of file
        """
        with open(filename) as file:
            # 1st line - states separated by ,
            self._states = file.readline().strip().split(',')

            # 2nd line - alphabet symbols separated by ,
            self._alphabet = file.readline().strip().split(',')

            # 3rd line - initial state
            self._initial_state = file.readline().strip()

            # 4th line - final states
            self._final_states = file.readline().strip().split(',')

            # 5th line to end of file - transitions with form:
            #     src state, dest state, values
            for line in file:
                tokens = line.strip().split(',')
                src_state = tokens[0]
                dest_state = tokens[1]
                values = tokens[2:]
                self._transitions[(src_state, dest_state)] = values

    def isAccepted(self, sequence):
        """
        Checks if sequence is accepted. \n
        :return: true | false
        """
        crt_state = self._initial_state

        for symbol in sequence:
            crt_state = self._getNextState(crt_state, symbol)
            if crt_state == -1:
                return False
        return crt_state in self._final_states

    def _getNextState(self, state, value):
        """
        Gets next state reachable from the crt state and the value we want to read.
        """
        for key in self._transitions.keys():
            if key[0] == state:
                if value in self._transitions[key]:
                    return key[1]
        return -1

    def printStates(self):
        print("Q = " + str(self._states))

    def printAlphabet(self):
        print("Σ = " + str(self._alphabet))

    def printInitialState(self):
        print("q0 = " + str(self._initial_state))

    def printFinalStates(self):
        print("F = " + str(self._final_states))

    def printTransitions(self):
        for key in self._transitions.keys():
            for value in self._transitions[key]:
                print("δ(" + key[0] + "," + value + ")=" + key[1])
