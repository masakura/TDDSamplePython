class Movie:
    def __init__(self, name, rental_type):
        self.__name = name
        self.__rental_type = rental_type

    @property
    def name(self):
        return self.__name

    @property
    def rental_type(self):
        return self.__rental_type
