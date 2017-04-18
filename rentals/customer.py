class Customer:
    def __init__(self, name):
        self.__name = name
        self.__rentals = []

    @property
    def name(self):
        return self.__name

    def add_rental(self, rental):
        self.__rentals.append(rental)
