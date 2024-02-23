from abc import ABC, abstractmethod


class Reservation(ABC):

    @property
    @abstractmethod
    def total_cost(self):
        pass


class FlightReservation(Reservation):
    def __init__(self, cost):
        self.cost = cost

    @property
    def total_cost(self):
        return self.cost


class HotelReservation(Reservation):
    def __init__(self, total_nights, price_per_night):
        self.total_nights = total_nights
        self.price_per_night = price_per_night

    @property
    def total_cost(self):
        return self.total_nights * self.price_per_night


class Itinerary(Reservation):
    def __init__(self, reservation=None):
        self.reservation = [] if reservation is None else reservation

    @property
    def total_cost(self):
        return sum([reserve.total_cost for reserve in self.reservation])


if __name__ == '__main__':
    iti = Itinerary(FlightReservation(450))
    # iti.reservation.append(FlightReservation(450))
    # iti.reservation.append(FlightReservation(955))
    # iti.reservation.append(HotelReservation(7, 50))
    print(iti.total_cost)
