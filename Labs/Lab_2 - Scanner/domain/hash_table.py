from collections import deque


class HashTable:
    def __init__(self, size):
        self.size = size
        self.position = 0
        self.table = list(deque() for _ in range(self.size))

    def hash(self, element):
        """
        :param element: string
        :return: hash value of given element
        """
        codes_sum = 0

        for char in element:
            codes_sum += ord(char)

        return codes_sum % self.size

    def size(self):
        """
        :return: size of the table
        """
        return self.size()

    def search(self, element):
        """
        :param element: string
        :return: element position if element already present, otherwise -1
        """
        key = self.hash(element)

        for item in self.table[key]:
            if item[0] == element:
                return item[1]
        return -1

    def add(self, element):
        """
        :param element: string
        :return: if element already present - its position, otherwise the position of newly added element
        """
        pos = self.search(element)

        if pos != -1:
            return pos
        else:
            key = self.hash(element)
            self.table[key].append((element, self.position))
            self.position += 1
            return self.position-1

    def __str__(self):
        table_str = ""
        for itemList in self.table:
            for item in itemList:
                table_str += str(item) + "\n"
        return table_str
