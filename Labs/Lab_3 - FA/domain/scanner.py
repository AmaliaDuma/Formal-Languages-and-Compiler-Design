import re

from domain.fa import FiniteAutomaton
from domain.hash_table import HashTable
from domain.pif import PIF
from utils.tokens import *


class Scanner:
    def __init__(self):
        self._st = HashTable(10)
        self._pif = PIF()
        self._faIdentifier = FiniteAutomaton()
        self._faIntConst = FiniteAutomaton()

        self._faIdentifier.readFromFile("utils/fa_identifier.in")
        self._faIntConst.readFromFile("utils/fa_intConst.in")

    def _isIdentifier(self, token):
        """
        Checks if token is an identifier. \n
        :param token:
        :return: true | false
        """
        return re.match(identifier, token) is not None

    def _isConstant(self, token):
        """
        Checks if token is a constant. \n
        :param token:
        :return: true | false
        """
        return self._faIntConst.isAccepted(token) or re.match(constant, token) is not None

    def _isOperatorPart(self, char):
        """
        Checks if the given char is a part of an operator. \n
        :param char: char
        :return: true | false
        """
        for op in operators:
            if char in op:
                return True
        return False

    def _getOperator(self, line, index):
        """
        Finds the next operator in the given line. \n
        :param line: line in the file
        :param index: crt position in line
        :return: (operator, new position in line)
        """
        token = ''

        while index < len(line) and self._isOperatorPart(line[index]):
            token += line[index]
            index += 1

        return token, index

    def _getStringConst(self, line, index):
        """
        Find the next string constant in the given line. \n
        :param line: line in the file
        :param index: crt position in line
        :return: (string constant, new position in line)
        """
        token = ''
        qoutes = 0

        while index < len(line) and qoutes < 2:
            if line[index] == '\"':
                qoutes += 1
            token += line[index]
            index += 1

        return token, index

    def tokenize(self, line):
        """
        Splits the given line into tokens and adds them to a list \n
        :param line: line in the file
        :return: list of tokens
        """
        token = ''
        index = 0
        tokens = []

        while index < len(line):
            if self._isOperatorPart(line[index]):
                # If crt char is a possible operator
                if token:
                    tokens.append(token)
                # Get the operator
                token, index = self._getOperator(line, index)
                tokens.append(token)
                token = ''

            elif line[index] == '\"':
                # If crt char is " we have a string constant following
                if token:
                    tokens.append(token)
                token, index = self._getStringConst(line, index)
                tokens.append(token)
                token = ''

            elif line[index] in separators:
                # If crt char is a separator
                if token:
                    tokens.append(token)
                token, index = line[index], index + 1
                tokens.append(token)
                token = ''

            else:
                token += line[index]
                index += 1
        if token:
            tokens.append(token)
        return tokens

    def scanFile(self, filename):
        """
        Scans the file, detects, classifies and codifies the tokens. \n
        :param filename: name of the file
        """
        exception = ''
        with open(filename, 'r') as file:
            crt_line = 0
            for line in file:
                crt_line += 1
                tokens = self.tokenize(line.strip())
                for i in range(len(tokens)):
                    # If token is a reserved word | operator | separator -> genPIF(token, -1)
                    if tokens[i] in keywords + separators + operators:
                        if tokens[i] == ' ':
                            continue
                        self._pif.add(tokens[i], -1)
                    # If token is identifier or constant -> insert in ST if not already there and return pos;
                    #                                       genPIF(token, pos)
                    elif self._faIdentifier.isAccepted(tokens[i]):
                        self._pif.add("identifier", self._st.add(tokens[i]))
                    elif self._isConstant(tokens[i]):
                        self._pif.add("constant", self._st.add(tokens[i]))
                    else:
                        exception += 'lexical error at token[' + tokens[i] + '] at line[' + str(crt_line) + "] : token can't be classified\n"

        with open("st.out", 'w') as writer:
            writer.write(str(self._st))

        with open("pif.out", 'w') as writer:
            writer.write(str(self._pif))

        if exception == '':
            print("lexically correct")
        else:
            print(exception)
