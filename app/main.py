class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_center = distance_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        if self.clean_power > car.clean_mark:
            diferent = car.comfort_class * (self.clean_power - car.clean_mark)
            price = diferent * self.average_rating / self.distance_center
            return round(price, 1)
        return 0.0

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> float:
        total_income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                wash_price = self.calculate_washing_price(car)
                total_income += wash_price
                self.wash_single_car(car)
        return round(total_income, 1)

    def rate_service(self, new_rating: float) -> None:
        self.count_of_ratings += 1
        total_rating = self.average_rating * (self.count_of_ratings
                                              - 1) + new_rating
        self.average_rating = round(total_rating / self.count_of_ratings, 1)
