from rentals.movie import Movie
from rentals.rental_type import RentalType
from rentals.rental import Rental


class Customer:
    def __init__(self, name):
        self.__name = name
        self.__rentals = []

    @property
    def name(self):
        return self.__name

    def add_rental(self, rental):
        self.__rentals.append(rental)

    def statement(self):
        pass
