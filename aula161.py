class MyList:
    def __init__(self):
        self._data = {}
        self._index = 0

    def append(self, value):
        self._data[self._index] = value
        self._index += 1

if __name__ == "__main__":
    my_list = MyList()
    my_list.append('Maria')
    my_list.append('Luiz')
    print(my_list._data)  # Output: {0: 'Luiz'}