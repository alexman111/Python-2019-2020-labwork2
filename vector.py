class Vector:

    def __init__(self, obj):
        self.__items = []
        for item in obj:
            self.__items.append(item)

    def __add__(self, other):

        if not isinstance(other, Vector):
            raise TypeError("Cannot add non-vector type to vector")

        if len(other.__items) != len(self.__items):
            raise IndexError("Cannot add two vectors with different length")

        result_vector = []
        for index in range(len(self.__items)):
            result_vector.append(self.__items[index] + other.__items[index])

        return Vector(result_vector)

    def __sub__(self, other):

        if not isinstance(other, Vector):
            raise TypeError("Cannot sub non-vector type to vector")

        if len(other.__items) != len(self.__items):
            raise IndexError("Cannot sub two vectors with different length")

        result_vector = []
        for index in range(len(self.__items)):
            result_vector.append(self.__items[index] - other.__items[index])

        return Vector(result_vector)

    def __mul__(self, other):
        if isinstance(other, (int, float)):

            result_vector = []
            for value in self.__items:
                result_vector.append(value * other)

            return Vector(result_vector)

        elif isinstance(other, Vector):

            if len(other.__items) != len(self.__items):
                raise IndexError("Cannot multiply vectors with different lengths")

            result = 0
            for index in range(len(self.__items)):
                result += self.__items[index] * other.__items[index]

            return result

        else:
            raise TypeError("Cannot multiply vector with " + type(other))

    def __eq__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Cannot equal with non-vector type")

        if len(self.__items) != len(other.__items):
            return False

        for index in range(len(self.__items)):
            if self.__items[index] != other.__items[index]:
                return False

        return True

    def __len__(self):
        return len(self.__items)

    def __getitem__(self, index):
        if index < 0 or index >= len(self.__items):
            raise IndexError("Wrong index")

        return self.__items[index]

    def __str__(self):
        result_str = "["

        is_begin = True
        for value in self.__items:
            if not is_begin:
                result_str += ", "
            else:
                is_begin = False

            result_str += str(value)

        result_str += "]"

        return result_str
